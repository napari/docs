# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "tqdm",
#   "PyGithub",
#   "gitpython",
#   "requests-cache",
#   "unidecode",
#   "pyyaml",
#   "argcomplete",
#   "packaging",
# ]
# ///
"""Generate the release notes automatically from GitHub pull requests."""
from __future__ import annotations

import argparse
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import NamedTuple

from packaging.version import parse as parse_version

import contextlib
import os
import threading
from contextlib import contextmanager
from datetime import datetime

from git import Repo
from github import Github, Milestone
from tqdm import tqdm
from unidecode import unidecode
from yaml import safe_load

PR_NUM_PATTERN = re.compile(r'\(#(\d+)\)(?:$|\n)')


@contextmanager
def short_cache(new_time):
    """
    context manager for change cache time in requests_cache
    """
    try:
        import requests_cache
    except ImportError:
        yield
        return

    import requests

    if requests_cache.get_cache() is None:
        yield
        return
    session = requests.Session()
    old_time = session.expire_after
    session.expire_after = new_time
    try:
        yield
    finally:
        session.expire_after = old_time


def setup_cache(timeout=3600):
    """
    setup cache for speedup execution and reduce number of requests to GitHub API
    by default cache will expire after 1h (3600s)
    """
    try:
        import requests_cache
    except ImportError:
        print('requests_cache not installed', file=sys.stderr)
        return

    """setup cache for requests"""
    requests_cache.install_cache(
        'github_cache',
        backend='filesystem',
        expire_after=timeout,
        allowable_methods=['GET', 'POST'],
    )


LOCAL_DIR = Path(__file__).parent
REPO_DIR_NAME = 'project_repo'
GH = os.environ.get('GH', 'github.com')
GH_USER = os.environ.get('GH_USER', 'napari')
GH_REPO = os.environ.get('GH_REPO', 'napari')
GH_DOCS_REPO = os.environ.get('GH_REPO', 'docs')
GH_TOKEN = os.environ.get('GH_TOKEN')

_thread_local = threading.local()


def get_github():
    if not hasattr(_thread_local, 'github'):
        if GH_TOKEN is None:
            raise RuntimeError(
                'It is necessary that the environment variable `GH_TOKEN` '
                'be set to avoid running into problems with rate limiting. '
                'One can be acquired at https://github.com/settings/tokens.\n\n'
                'You do not need to select any permission boxes while generating '
                'the token.'
            )
        _thread_local.github = Github(GH_TOKEN)
    return _thread_local.github


def get_repo(user=GH_USER, repo=GH_REPO):
    g = get_github()
    return g.get_repo(f'{user}/{repo}')


def get_local_repo(path=None):
    """
    get the local repository
    """
    from git import Repo

    if path is not None:
        return Repo(path)
    return Repo(REPO_DIR_NAME)


def get_common_ancestor(commit1, commit2):
    """
    find the common ancestor for two commits
    """
    local_repo = get_local_repo()
    return local_repo.merge_base(commit1, commit2)[0]


def get_commits_to_ancestor(ancestor, rev='main'):
    local_repo = get_local_repo()
    yield from local_repo.iter_commits(f'{ancestor.hexsha}..{rev}')


def get_commit_counts_from_ancestor(release, rev='main'):
    """
    get number of commits from ancestor to release
    """
    ancestor = get_common_ancestor(release, rev)
    return sum(
        PR_NUM_PATTERN.search(c.message) is not None
        for c in get_commits_to_ancestor(ancestor, rev)
    )


def get_milestone(
    milestone_name: str | None,
    repo: str = f'{GH_USER}/{GH_REPO}',
) -> Milestone.Milestone | None:
    if milestone_name is None:
        return None
    repository = get_repo(*repo.split('/'))
    with contextlib.suppress(ValueError):
        return repository.get_milestone(int(milestone_name))

    for milestone in repository.get_milestones(state='all'):
        if milestone.title == milestone_name:
            return milestone
    raise RuntimeError(f'Milestone {milestone_name} for {repo} not found.')


def get_split_date(previous_release, rev='main'):
    common_ancestor = get_common_ancestor(previous_release, rev)
    remote_commit = get_repo().get_commit(common_ancestor.hexsha)
    return datetime.strptime(remote_commit.last_modified, '%a, %d %b %Y %H:%M:%S %Z')


def iter_pull_request(additional_query, user=GH_USER, repo=GH_REPO):
    iterable = get_github().search_issues(
        f'repo:{user}/{repo} is:pr sort:created-asc {additional_query}'
    )
    print(
        f'Found {iterable.totalCount} pull requests on query: {additional_query}'
        f' for repo {user}/{repo}',
        file=sys.stderr,
    )
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=10) as executor:
        yield from tqdm(
            executor.map(lambda x: x.as_pull_request(), iterable),
            desc=f'Pull Requests ({user}/{repo})...',
            total=iterable.totalCount,
        )


def get_pr_commits_dict(repo: Repo, branch: str = 'main') -> dict[int, str]:
    """
    Calculate mapping from PR number in commit hash from a provided branch
    Parameters
    ----------
    repo: Repo
        Object representing local repository
    branch: str
        branch name
    Returns
    -------
    dict from PR number to commit hash
    """
    res = {}
    for commit in repo.iter_commits(branch):
        if (match := PR_NUM_PATTERN.search(commit.message)) is not None:
            pr_num = int(match[1])
            res[pr_num] = commit.hexsha
    return res


def get_consumed_pr(repo: Repo, target_branch: str) -> set[int]:
    """
    Get a set of commits that are already cherry-picked
    Parameters
    ----------
    repo: Repo
        object representing local repository
    target_branch: str
        branch to check for merged PR
    Returns
    -------
    """
    res = set()

    for commit in repo.iter_commits(target_branch):
        if (match := PR_NUM_PATTERN.search(commit.message)) is not None:
            pr_num = int(match[1])
            res.add(pr_num)
    return res


def existing_file(path: str) -> Path:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f'{path} not found')
    return path


BOT_LIST = {
    'github-actions[bot]',
    'pre-commit-ci[bot]',
    'dependabot[bot]',
    'github-advanced-security[bot]',
    'napari-bot',
    None,
}


def get_correction_dict(file_path: Path | None) -> dict[str, str]:
    """
    Read file with correction of name between
    """
    if not file_path or not file_path.exists():
        return {}

    correction_dict = {}
    with open(file_path, encoding='utf-8') as f:
        corrections = safe_load(f)
        for correction in corrections['login_to_name']:
            correction_dict[correction['login']] = correction['corrected_name']

    return correction_dict


def get_corrections_from_citation_cff(
    cff_data: str | Path | dict,
) -> dict[str, str]:
    if isinstance(cff_data, str | Path):
        cff_data = Path(cff_data)
        if not cff_data.exists():
            return {}
        with cff_data.open(encoding='utf8') as f:
            cff_data = safe_load(f)
    res = {}
    for author in cff_data['authors']:
        if 'alias' in author:
            res[author['alias']] = f'{author["given-names"]} {author["family-names"]}'
    return res


def get_corrections_from_citation_cff2(
    cff_data: str | Path | dict,
) -> dict[str, str]:
    if isinstance(cff_data, str | Path):
        cff_data = Path(cff_data)
        if not cff_data.exists():
            return {}
        with cff_data.open(encoding='utf8') as f:
            cff_data = safe_load(f)
    res = {}
    for author in cff_data['authors']:
        if 'alias' in author:
            res[author['alias']] = unidecode(
                f'{author["given-names"]} {author["family-names"]}'.lower()
            )
    return res


LOCAL_DIR = Path(__file__).parent

PR_REGEXP = re.compile(r'(?P<user>[\w-]+)/(?P<repo>[\w-]+)#(?P<pr>\d+)')


class PRInfo(NamedTuple):
    user: str
    repo: str
    pr: int


def parse_pr_num(pr_num):
    if match := PR_REGEXP.match(pr_num):
        return PRInfo(match.group('user'), match.group('repo'), int(match.group('pr')))
    try:
        return int(pr_num)
    except ValueError as err:
        raise argparse.ArgumentTypeError(f'{pr_num} is not a valid PR number.') from err


parser = argparse.ArgumentParser(usage=__doc__)
parser.add_argument('tag', help='The tag that will be released, e.g. 0.6.2')
parser.add_argument('--target-directory', type=Path, default=None)
parser.add_argument(
    '--correction-file',
    help='The file with the corrections',
    default=LOCAL_DIR / 'name_corrections.yaml',
)
parser.add_argument(
    '--with-pr',
    help='Include PR numbers for not merged PRs',
    type=parse_pr_num,
    default=None,
    nargs='+',
)
parser.add_argument(
    '--only-merged',
    help='Only include merged PRs, excluding open ones.',
    action='store_const',
    const='is:merged',
    default='',
    dest='merged',
)
parser.add_argument(
    '--no-cache',
    help='Disable caching of GitHub API requests. This may lead to slower execution and more requests to the GitHub API, but ensures that you are getting the most up-to-date information.',
    action='store_true',
)

args = parser.parse_args()

version = parse_version(args.tag)

args.milestone = version.base_version

if not args.no_cache:
    setup_cache()
repo = get_repo()
correction_dict = get_correction_dict(
    args.correction_file
) | get_corrections_from_citation_cff(LOCAL_DIR / REPO_DIR_NAME / 'CITATION.cff')


def add_to_users(users_dkt, new_user):
    if new_user.login in users_dkt:
        # reduce obsolete requests to GitHub API
        return
    if new_user.login in correction_dict:
        users_dkt[new_user.login] = correction_dict[new_user.login]
    elif new_user.name is None:
        users_dkt[new_user.login] = new_user.login
    else:
        users_dkt[new_user.login] = new_user.name


authors = set()
committers = set()
docs_authors = set()
docs_committers = set()
reviewers = set()
docs_reviewers = set()
users = {}

non_merged_pr = []

highlights = {
    'Highlights': {},
    'New Features': {},
    'Breaking Changes': {},
    'Improvements': {},
    'Performance': {},
    'Bug Fixes': {},
    'API Changes': {},
    'Deprecations': {},
    'Build Tools': {},
    'Documentation': {},
}

other_pull_requests = {}

label_to_section = {
    'bug': 'Bug Fixes',
    'bugfix': 'Bug Fixes',
    'feature': 'New Features',
    'api': 'API Changes',
    'highlight': 'Highlights',
    'performance': 'Performance',
    'enhancement': 'Improvements',
    'deprecation': 'Deprecations',
    'dependencies': 'Build Tools',
    'documentation': 'Documentation',
    'example': 'Documentation',
    'release:breaking change': 'Breaking Changes',
}


def parse_pull(pull_number: int, repo_full_name: str):
    repo_ = get_repo(*repo_full_name.split('/'))
    pull = repo_.get_pull(pull_number)

    is_merged = pull.raw_data.get('merged')
    if is_merged is None:
        is_merged = pull.merged

    if is_merged:
        if pull.merged_by is not None:
            add_to_users(users, pull.merged_by)
            committers.add(pull.merged_by.login)
        if pull.user is not None:
            add_to_users(users, pull.user)
            authors.add(pull.user.login)

    summary = pull.title

    for review in pull.get_reviews():
        if review.user is not None:
            add_to_users(users, review.user)
            reviewers.add(review.user.login)
    assigned_to_section = False
    pr_labels = {label.name.lower() for label in pull.labels}
    for label_name, section in label_to_section.items():
        if label_name in pr_labels:
            highlights[section][pull_number] = {
                'summary': summary,
                'repo': repo_full_name.split('/')[1],
            }
            assigned_to_section = True

    if not assigned_to_section:
        other_pull_requests[pull_number] = {
            'summary': summary,
            'repo': repo_full_name.split('/')[1],
        }


pulls_to_parse = []
for pull_ in iter_pull_request(f'milestone:{args.milestone} {args.merged}'):
    is_merged = pull_.raw_data.get('merged')
    if is_merged is None:
        is_merged = pull_.merged
    if not is_merged:
        non_merged_pr.append(pull_)
    pulls_to_parse.append((pull_.number, repo.full_name))

if args.with_pr is not None:
    for pr_num in args.with_pr:
        if isinstance(pr_num, int):
            pulls_to_parse.append((pr_num, repo.full_name))
        else:
            r = get_repo(pr_num.user, pr_num.repo)
            pulls_to_parse.append((pr_num.pr, r.full_name))

doc_pulls = list(
    iter_pull_request(f'milestone:{args.milestone} {args.merged}', repo=GH_DOCS_REPO)
)

for pull in doc_pulls:
    is_merged = pull.raw_data.get('merged')
    if is_merged is None:
        is_merged = pull.merged
    if not is_merged:
        non_merged_pr.append(pull)

# cache is not threadsafe
max_workers = 10 if args.no_cache else 1

with ThreadPoolExecutor(max_workers=max_workers) as executor:
    list(executor.map(lambda x: parse_pull(*x), pulls_to_parse))

for pull in doc_pulls:
    issue = pull.as_issue()
    add_to_users(users, issue.user)
    docs_authors.add(issue.user.login)

    summary = pull.title

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # We need reviews for docs PRs too
        reviews = list(pull.get_reviews())
        for review in reviews:
            if review.user is not None:
                add_to_users(users, review.user)
                docs_reviewers.add(review.user.login)

    assigned_to_section = False
    pr_labels = {label.name.lower() for label in pull.labels}
    if 'highlight' in pr_labels:
        highlights['Highlights'][pull.number] = {
            'summary': summary,
            'repo': GH_DOCS_REPO,
        }
    if 'maintenance' in pr_labels:
        other_pull_requests[pull.number] = {
            'summary': summary,
            'repo': GH_DOCS_REPO,
        }
    else:
        highlights['Documentation'][pull.number] = {
            'summary': summary,
            'repo': GH_DOCS_REPO,
        }


# add Other PRs to the ordered dict to make doc generation easier.
highlights['Other Pull Requests'] = other_pull_requests


# remove these bots.
committers -= BOT_LIST
authors -= BOT_LIST
docs_committers -= BOT_LIST
docs_authors -= BOT_LIST
reviewers -= BOT_LIST
docs_reviewers -= BOT_LIST

USER_NAME_PATTERN = re.compile(r'@([\w-]+)')  # pattern for GitHub usernames
GITHUB_PR_LINK_PATTERN = re.compile(
    GH + r'/(?P<owner>[\w-]+)/(?P<repo>[\w-]+)/pull/(?P<number>\d+)'
)  # pattern for GitHub PR link


old_contributors = set()

if args.target_directory is None:
    file_handle = sys.stdout
else:
    res_file_name = f'release_{args.milestone.replace(".", "_")}.md'
    file_handle = open(args.target_directory / res_file_name, 'w', encoding='utf-8')  # noqa
    for file_path in args.target_directory.glob('release_*.md'):
        if file_path.name == res_file_name:
            continue
        with open(file_path, encoding='utf-8') as f:
            old_contributors.update(USER_NAME_PATTERN.findall(f.read()))


# Now generate the release notes
title = f'# napari {args.milestone}'
print(title, file=file_handle)

notes_dir = LOCAL_DIR / 'additional_notes' / args.milestone
if not notes_dir.glob('*.md'):
    print(
        'There is no prepared sections in the additional_notes directory.',
        file=sys.stderr,
    )

milestone_obj = get_milestone(args.milestone)

# prerelease includes alpha and rc versions
if version.is_prerelease:
    print(
        f'⚠️ *Note: these release notes are still in draft while {version} is in prerelease testing.* ⚠️',
        file=file_handle,
    )
print('', file=file_handle)
print(f'*{milestone_obj.due_on.strftime("%a, %b %d, %Y")}*', file=file_handle)
print('', file=file_handle)

if (fn := notes_dir / 'header.md').exists():
    intro = fn.open(encoding='utf-8').read()
else:
    intro = f"""We're happy to announce the release of napari {args.milestone}!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website,
https://napari.org.
"""

print(intro, file=file_handle)


def detect_effver_type(milestone):
    """Detect if this is a MACRO, MESO, or MICRO release based on version number."""
    # Remove any pre-release suffixes (like 0.6.0rc1 -> 0.6.0)
    clean_version = milestone.split('rc')[0].split('a')[0].split('b')[0]
    parts = clean_version.split('.')
    vinfo = int(parts[0]), int(parts[1]), int(parts[2])
    match vinfo:
        case 0, _, 0:
            return 'MACRO'
        case 0, _, _:
            return 'MESO'
        case _, 0, 0:
            return 'MACRO'
        case _, _, 0:
            return 'MESO'
        case _:
            return 'MICRO'


effver_type = detect_effver_type(args.milestone)

effver_info = {
    'MACRO': 'this is a **Macro** release containing awesome new features, but may require dedication of some significant time when upgrading projects to use this version.',
    'MESO': 'this is a **Meso** release containing awesome new features, but some effort may be needed when updating previous projects to use this version.',
    'MICRO': 'this is a **Micro** release containing awesome new features that are expected to be adoptable with no additional effort.',
}
effver_info = f"""napari follows [EffVer (Intended Effort Versioning)](https://effver.org/); {effver_info.get(effver_type)}
"""

print(effver_info, file=file_handle)

for section, pull_request_dicts in highlights.items():
    section_path = (
        LOCAL_DIR / 'additional_notes' / args.milestone / f'{section.lower()}.md'
    )

    if not section_path.exists() and not pull_request_dicts:
        continue

    print(f'## {section}\n', file=file_handle)

    mentioned_pr = set()
    if section_path.exists():
        with section_path.open(encoding='utf-8') as f:
            text = f.read()
        for owner, repo, pr_number in GITHUB_PR_LINK_PATTERN.findall(text):
            mentioned_pr.add(PRInfo(user=owner, repo=repo, pr=int(pr_number)))
        print(text, file=file_handle)
        print('', file=file_handle)

    for number, pull_request_info in sorted(
        pull_request_dicts.items(), key=lambda x: x[0]
    ):
        if (
            PRInfo(user=GH_USER, repo=pull_request_info['repo'], pr=number)
            in mentioned_pr
        ):
            continue
        repo_str = pull_request_info['repo']
        repo_prefix = repo_str if repo_str != 'napari' else ''
        print(
            f'- {pull_request_info["summary"]} ([{repo_prefix}#{number}]'
            f'(https://{GH}/{GH_USER}/{repo_str}/pull/{number}))',
            file=file_handle,
        )
    print('', file=file_handle)


contributors = {
    'authors': authors | docs_authors,
    'reviewers': reviewers | docs_reviewers,
}

# ignore committers
# contributors['committers'] = committers
new_contributors = (authors | docs_authors) - old_contributors

for section_name, contributor_set in contributors.items():
    print('', file=file_handle)
    if None in contributor_set:
        contributor_set.remove(None)
    committer_str = (
        f'## {len(contributor_set)} {section_name} added to this release (alphabetical)'
    )
    print(committer_str, file=file_handle)
    print('', file=file_handle)
    print('(+) denotes first-time contributors 🥳', file=file_handle)
    print('', file=file_handle)

    for c in sorted(contributor_set, key=lambda x: users[x].lower()):
        if c in authors and c in docs_authors:
            first_repo_name = GH_REPO
            second_repo_str = (
                f' ([docs](https://{GH}/{GH_USER}/{GH_DOCS_REPO}/commits?author={c})) '
            )
        elif c in authors:
            first_repo_name = GH_REPO
            second_repo_str = ''
        else:  # docs only
            first_repo_name = GH_DOCS_REPO
            second_repo_str = ''

        first = ' +' if c in new_contributors else ''
        commit_link = f'https://{GH}/{GH_USER}/{first_repo_name}/commits?author={c}'
        print(
            f'- [{users[c]}]({commit_link}){second_repo_str} - @{c}{first}',
            file=file_handle,
        )

if args.target_directory:
    toc_path = args.target_directory.parent / '_toc.yml'
    with open(toc_path) as f:
        toc = f.read()
    # add new notes to release
    new_version = args.milestone.replace('.', '_')
    if not re.search(rf'release_{new_version}', toc):
        toc = re.sub(
            r'(\s+- file: release/release)(.*)',
            rf'\1_{new_version}\1\2',
            toc,
            count=1,
        )
        with open(toc_path, 'w') as f:
            toc = f.write(toc)

if non_merged_pr:
    if len(non_merged_pr) == 1:
        pr = non_merged_pr[0]
        print(
            f"There is on unmerged PR ({pr.number} {pr.title} - {pr.html_url}). If it is release notes PR it's fine.",
            file=sys.stderr,
        )

    else:
        pr_info = [
            f'{pr.base.repo.full_name}#{pr.number} - {pr.title} {pr.html_url}'
            for pr in non_merged_pr
        ]
        print('#' * 50, file=sys.stderr)
        print(f'There are {len(non_merged_pr)} unmerged PRs:', file=sys.stderr)
        print('\n'.join(pr_info), file=sys.stderr)
