from __future__ import annotations

import contextlib
import os
import re
import sys
import threading
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

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
    return datetime.strptime(
        remote_commit.last_modified, '%a, %d %b %Y %H:%M:%S %Z'
    )


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
            res[author['alias']] = (
                f'{author["given-names"]} {author["family-names"]}'
            )
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
