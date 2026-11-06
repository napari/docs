Generate the release notes automatically from GitHub pull requests
------------------------------------------------------------------

We recommend using `uv run --locked` to run this script. This will run the
script in an isolated environment using the adjacent `uv.lock` file.

# GitHub token

You need a GitHub API token to run this script. You can do this in two ways:

1. using the `gh` command line utility
2. generating a token on the GitHub website and making it available to your
   shell.

## Method 1: using the `gh` command line interface to fetch a token.

### bash/zsh

```
GH_TOKEN=`gh auth token` python generate_release_notes.py 0.9.1
```

### fish

```
GH_TOKEN=(gh auth token) python generate_release_notes.py 0.9.1
```

### Windows cmd

```
for /f %%i in ('gh auth token') do set GH_TOKEN=%%i
python generate_release_notes.py 0.9.1
```

### Windows PowerShell

```
$env:GH_TOKEN = gh auth token
python generate_release_notes.py 0.9.1
```

## Method 2: manually generating a token and copying it locally

You can create a new GitHub API token by navigating to:

    https://github.com/settings/personal-access-tokens/new

Set an expiry date longer than 30 days if desired (but it is restricted to
being shorter than 365 days). The remaining default settings (read-only access
to public repositories) are sufficient for our purposes.

Copy the text to a safe place: you can only see it at creation time. You can
add them to your startup files as follows; in each case, you will need to start
a new shell for the setting to take effect.

### bash

```
echo export GH_TOKEN='<your-gh-api-token>' >> ~/.bashrc
```

### zsh

```
echo export GH_TOKEN='<your-gh-api-token>' >> ~/.zshrc
```

### fish

```
echo set GH_TOKEN <your-gh-api-token> >> ~/.config/fish/config.fish
```

### Windows cmd

```
setx GH_TOKEN <your-gh-api-token>
```

### Windows PowerShell

```
[Environment]::SetEnvironmentVariable("GH_TOKEN", "<your-gh-api-token>",
"User")
```

# Run the script:

```
uv run generate_release_notes.py <milestone>
```

For example:

```
uv run generate_release_notes.py 0.9.1
```

By default, the output will overwrite `../docs/release/release_M_N_P.md` for
milestone M.N.P, but you can override it with the `--target-directory` option:

```
# output to current directory for testing
uv run generate_release_notes.py <milestone> --target-directory=.
```

# Notes

## Contributor names

To substitute GitHub handles for author names, the `name_corrections.yaml` file
is used in cases when the GitHub User API does not return suitable values. You
can a custom file with the `--correction-file` option:

```
uv run generate_release_notes.py <milestone> \
    --correction-file /path/to/name_corrections.yaml
```

## Caching

To help with milestones with a large number of commits, the script
caches GitHub API requests to speed up execution and reduce the number of
requests to the GitHub API. Consequently, if you edit some PR titles or labels,
you may not see the changes in the generated release notes until the cache
expires (after 1h by default).

Use the `--no-cache` option to ignore the cache.

The cache is a simple `github_cache` folder in the current directory, so it can
be cleared by deleting that folder.

## Threading

Use of the cache is not thread-safe, so multithreading is disabled when caching
is enabled.
