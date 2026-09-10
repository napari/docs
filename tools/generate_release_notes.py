"""Generate the release notes automatically from GitHub pull requests.

We recoment using uv for runing this script.
1. clone the napari/docs repository to read previous contributors and to write the release notes to the correct location.

2. Install the requirements into a virtual environment (PyGitHub and tqdm) with
   ```
   uv sync
   ```
3. Start by creating a GitHub API token. You can do this by going to
GitHub settings -> Developer settings -> Personal access tokens -> Fine-grained tokens.
Create a new token with read-only access to Public repositories;
the token must expire in 365 days or less.

4. Set the token as an environment variable:
On Linux or MacOS:
```
export GH_TOKEN='<your-gh-api-token>'
```
or in Windows cmd:
```
set GH_TOKEN=<your-gh-api-token>
```
or set permanently with Windows PowerShell:
```
[Environment]::SetEnvironmentVariable("GH_TOKEN", "<your-gh-api-token>", "User")
```

5. Run the script:
Then, to include everything set for the a chosen milestone:
```
uv run generate_release_notes.py <milestone> --target-directory=/path/to/docs/release/
```
For example:
```
uv run generate_release_notes.py 0.7.1 --target-directory=../napari-docs/docs/release/
```

To substitute GitHub handles for author names, use the `--correction-file` option:
```
uv run generate_release_notes.py <milestone> --target-directory=/path/to/docs/release/ --correction-file /path/to/name_corrections.yaml
```

The default correction file is `name_corrections.yaml` in the same directory as this script, so the argument is not needed.

By default the script is caching GitHub API requests to speed
up execution and reduce the number of requests to the GitHub API.
It means that if you edit some PR titles or labels, you may not see
the changes in the generated release notes until the cache expires (after 1h by default).

Cache is used to avoid hitting GitHub API rate limits, which can be a
problem when generating release notes for a large number of pull requests.

Script can be run with the `--no-cache` option to disable caching of GitHub API requests.

To clean the cache, you can delete the `github_cache` directory in the current working directory.

There is a known problem with using cache on conda environments, because
we use threads to speed up the execution, and
access to sqlite database used by cache is not thread-safe.
Even if we use `filesystem` backend for cache, it still uses sqlite database under the hood.

Hoever, when using `uv` it works and speeds up the execution significantly, so we recommend using `uv` for running this script.



References:
- https://github.com/scikit-image/scikit-image/blob/main/tools/generate_release_notes.py
- https://github.com/scikit-image/scikit-image/issues/3404
- https://github.com/scikit-image/scikit-image/issues/3405
"""

import argparse
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import NamedTuple

from packaging.version import parse as parse_version

from release_utils import (
    BOT_LIST,
    GH,
    GH_DOCS_REPO,
    GH_REPO,
    GH_USER,
    REPO_DIR_NAME,
    get_correction_dict,
    get_corrections_from_citation_cff,
    get_milestone,
    get_repo,
    iter_pull_request,
    setup_cache,
)

LOCAL_DIR = Path(__file__).parent

PR_REGEXP = re.compile(r'(?P<user>[\w-]+)/(?P<repo>[\w-]+)#(?P<pr>\d+)')


class PRInfo(NamedTuple):
    user: str
    repo: str
    pr: int


def parse_pr_num(pr_num):
    if match := PR_REGEXP.match(pr_num):
        return PRInfo(
            match.group('user'), match.group('repo'), int(match.group('pr'))
        )
    try:
        return int(pr_num)
    except ValueError:
        raise argparse.ArgumentTypeError(f'{pr_num} is not a valid PR number.')


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
) | get_corrections_from_citation_cff(
    LOCAL_DIR / REPO_DIR_NAME / 'CITATION.cff'
)


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
    iter_pull_request(
        f'milestone:{args.milestone} {args.merged}', repo=GH_DOCS_REPO
    )
)

for pull in doc_pulls:
    is_merged = pull.raw_data.get('merged')
    if is_merged is None:
        is_merged = pull.merged
    if not is_merged:
        non_merged_pr.append(pull)

with ThreadPoolExecutor(max_workers=10) as executor:
    list(executor.map(lambda x: parse_pull(*x), pulls_to_parse))

for pull in doc_pulls:
    issue = pull.as_issue()
    add_to_users(users, issue.user)
    docs_authors.add(issue.user.login)

    summary = pull.title

    with ThreadPoolExecutor(max_workers=10) as executor:
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
    file_handle = open(
        args.target_directory / res_file_name, 'w', encoding='utf-8'
    )
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
        LOCAL_DIR
        / 'additional_notes'
        / args.milestone
        / f'{section.lower()}.md'
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
        f'## {len(contributor_set)} {section_name} added to this '
        'release (alphabetical)'
    )
    print(committer_str, file=file_handle)
    print('', file=file_handle)
    print('(+) denotes first-time contributors 🥳', file=file_handle)
    print('', file=file_handle)

    for c in sorted(contributor_set, key=lambda x: users[x].lower()):
        if c in authors and c in docs_authors:
            first_repo_name = GH_REPO
            second_repo_str = (
                f' ([docs](https://{GH}/{GH_USER}/'
                f'{GH_DOCS_REPO}/commits?author={c})) '
            )
        elif c in authors:
            first_repo_name = GH_REPO
            second_repo_str = ''
        else:  # docs only
            first_repo_name = GH_DOCS_REPO
            second_repo_str = ''

        first = ' +' if c in new_contributors else ''
        commit_link = (
            f'https://{GH}/{GH_USER}/{first_repo_name}/commits?author={c}'
        )
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
