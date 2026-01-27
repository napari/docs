(hub-customization)=

# Customizing your plugin's listing on napari hub

Once your plugin is published to [PyPI](https://pypi.org/) with the `Framework :: napari` classifier, it will automatically appear on the [napari hub](https://napari-hub.org/). This guide explains how to customize your plugin's listing to provide the best experience for potential users.

## Overview

The napari hub displays information about your plugin from two main sources:

1. **PyPI** - Core package metadata from your `pyproject.toml`
2. **npe2 manifest** - Plugin-specific metadata from your `napari.yaml` file

By understanding how these sources work together, you can ensure your plugin appears with accurate, appealing information on the hub.

## Setting package metadata in pyproject.toml

Most of the information displayed on the napari hub comes from your [Python package metadata](https://packaging.python.org/en/latest/specifications/core-metadata/). The napari hub reads this information from [PyPI's JSON API](https://docs.pypi.org/api/json/) after you publish your package.

### Essential fields

These fields appear prominently on your plugin's listing and in search results:

#### Name

The package name as it appears on PyPI. This is what users will use to install your plugin.

```toml
[project]
name = "napari-example-plugin"
```

#### Summary

A one-line description of your plugin. Keep it concise and descriptive - it appears in plugin listings and search results.

```toml
[project]
description = "A plugin for advanced image segmentation using deep learning"
```

#### Version

The current version of your plugin. We strongly recommend using [Semantic Versioning (SemVer)](https://semver.org/) or [Intended Effort Versioning (EffVer)](https://jacobtomlinson.dev/effver/) with Python conventions for pre-releases ([PEP 440](https://www.python.org/dev/peps/pep-0440/)).

```toml
[project]
version = "0.1.0"
```

````{tip}
If you're using dynamic versioning tools like `setuptools-scm` or `hatch-vcs`, you can specify:

```toml
[project]
dynamic = ["version"]
```
````

#### Authors

Plugin authors displayed on your listing. The hub will display this information on the search page and on your plugin's page.

```toml
[project]
authors = [
    {name = "Jane Doe", email = "jane@example.com"},
    {name = "John Smith"},
]
```

#### License

The license under which your plugin is distributed. Use a valid [SPDX identifier](https://spdx.org/licenses/) or the string `"Other"`. Modern Python packaging uses the [`license-expression` format](https://packaging.python.org/en/latest/specifications/core-metadata/#license-expression) for specifying licenses.

```toml
[project]
license = "BSD-3-Clause"
license-files = ["LICENSE"]
```

````{note}
Previously, the valid way to specify license information used the `license` table with `file` or `text` keys and a license trove classifier. This still works for listings on the napari-hub, but is deprecated in favor of `license-expression`.

```toml
[project]
license = {text = "BSD-3-Clause"}
```

````

#### Description

A detailed description of your plugin. This appears on the plugin's detail page and is indexed for search. Use your `README.md` file:

```toml
[project]
readme = "README.md"
```

The hub will render your README with proper Markdown formatting. If you begin with a Level 1 heading, it will be treated as a title and removed from the description.

**What to include:**

- **Clear summary**: Start with who the plugin is for, what data it works with, and what problems it solves
- **Quick start example**: Include images, GIFs, or videos showing the plugin in action
- **Relevant keywords**: Mention key terms users might search for (e.g., "segmentation", "3D", "time series")
- **Section headings**: Use Level 2 headings (`##`) to organize content - these create navigation links in the sidebar

#### Classifiers

Trove classifiers provide structured metadata about your plugin. The `Framework :: napari` classifier is required for hub visibility.

```toml
[project]
classifiers = [
    "Development Status :: 4 - Beta",
    "Framework :: napari",
    "Intended Audience :: Science/Research",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Scientific/Engineering :: Image Processing",
]
```

**Operating System classifiers** let users filter by platform:

```toml
classifiers = [
    "Operating System :: MacOS",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    # OR for cross-platform plugins:
    "Operating System :: OS Independent",
]
```

See the full list of [PyPI classifiers](https://pypi.org/classifiers/).

#### Python version requirements

Specify the Python versions your plugin supports:

```toml
[project]
requires-python = ">=3.10"
```

If you specify `">=3.10"`, the hub will tag your plugin as supporting Python 3.10, 3.11, 3.12, etc.

#### Dependencies

List your plugin's dependencies. The hub displays these on the detail page.

```toml
[project]
dependencies = [
    "numpy>=1.21",
    "scikit-image>=0.19",
    "torch>=2.0",
    "qtpy",
]
```

```{warning}
**Never include Qt backends** (`PyQt5`, `PyQt6`, `PySide2`, `PySide6`) or `napari[all]` in your base dependencies! See [](best-practices-no-qt-backend) for details.
```

### Project URLs

Project URLs appear as links on your plugin's detail page. The hub recognizes several special URL names:

```toml
[project.urls]
Homepage = "https://github.com/username/napari-example-plugin"
Documentation = "https://napari-example-plugin.readthedocs.io"
"Source Code" = "https://github.com/username/napari-example-plugin"
"Bug Tracker" = "https://github.com/username/napari-example-plugin/issues"
"User Support" = "https://forum.image.sc/tag/napari"
```

### Complete example

Here's a complete example of a well-configured `pyproject.toml`:

```toml
[project]
name = "napari-example-plugin"
version = "0.1.0"
description = "Advanced image segmentation using deep learning"
readme = "README.md"
license = "BSD-3-Clause"
license-files = ["LICENSE"]
requires-python = ">=3.10"
authors = [
    {name = "Jane Doe", email = "jane@example.com"},
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Framework :: napari",
    "Intended Audience :: Science/Research",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Scientific/Engineering :: Image Processing",
]
dependencies = [
    "numpy>=1.21",
    "scikit-image>=0.19",
    "magicgui>=0.8.0",
]

[project.urls]
Homepage = "https://github.com/username/napari-example-plugin"
Documentation = "https://napari-example-plugin.readthedocs.io"
"Bug Tracker" = "https://github.com/username/napari-example-plugin/issues"
"User Support" = "https://forum.image.sc/tag/napari"

[project.entry-points."napari.manifest"]
napari-example-plugin = "napari_example_plugin:napari.yaml"
```

## npe2 manifest metadata

Your plugin's [npe2 manifest](plugin-manifest) (`napari.yaml`) provides napari-specific metadata that appears on the hub.

### Display name

The display name appears in plugin listings and the napari plugin manager:

```yaml
name: napari-example-plugin
display_name: Example Segmentation Plugin
```

### Plugin type indicators

The hub automatically detects your plugin's capabilities from your manifest contributions:

- **Reader plugins**: Detected from `contributions.readers`
- **Writer plugins**: Detected from `contributions.writers`
- **Widget plugins**: Detected from `contributions.widgets`
- **Sample data**: Detected from `contributions.sample_data`

The hub displays supported file extensions for readers and writers:

```yaml
contributions:
  readers:
    - command: napari-example-plugin.read_tiff
      filename_patterns: ["*.tif", "*.tiff"]
    - command: napari-example-plugin.read_custom
      filename_patterns: ["*.custom"]
  
  writers:
    - command: napari-example-plugin.write_tiff
      filename_patterns: ["*.tif"]
      layer_types: ["image", "labels"]
```

### Visibility control

Control whether your plugin appears in hub search and listings, and in the napari plugin manager:

```yaml
name: napari-example-plugin
visibility: public  # or "hidden"
```

- `public` (default): Plugin appears in search and listings
- `hidden`: Detail page is accessible via direct link, but plugin doesn't appear in search. Remains installable via napari plugin manager.

### Removing your plugin from napari and the hub

To completely hide your plugin from both the napari plugin manager and the napari hub, remove the `Framework :: napari` classifier from your `pyproject.toml`:

```toml
[project]
classifiers = [
    # "Framework :: napari",  # Remove or comment out this line
    "Programming Language :: Python :: 3",
    # ... other classifiers
]
```

```{important}
You must release a new version for this change to take effect.
```

After removing the classifier:

- Your plugin will still work when manually installed (`pip install your-plugin`)
- It won't appear in the napari plugin manager
- It won't appear on the napari hub
- It won't be automatically discovered by napari metadata tools

## Troubleshooting

### My changes aren't showing up on the hub

The napari hub updates plugin information periodically. After publishing a new version to PyPI:

1. Wait up to 4 hours for the hub to refresh
2. Clear your browser cache
3. Check that your new version appears on [PyPI](https://pypi.org/)
4. Verify your GitHub "Source Code" URL is correct and publicly accessible

### My plugin doesn't appear on the hub at all

Check that:

- Your package is published to PyPI
- You included the `Framework :: napari` classifier
- Your plugin's `visibility` is not set to `hidden` (or is set to `public`)
- Your package has a valid npe2 manifest (`napari.yaml`) with a `napari.manifest` entry point

### My description isn't formatting correctly

- Ensure your README is valid Markdown
- Check that `readme = "README.md"` is in your `pyproject.toml`
- Remember that Level 1 headings (`#`) are treated as titles and removed
- Use Level 2 headings (`##`) to create navigable sections

## Best practices

### Write a compelling summary

Your summary appears in search results and plugin listings. Make it count:

**Good**: "GPU-accelerated 3D cell segmentation for confocal microscopy"  
**Poor**: "A napari plugin for segmentation"

### Provide comprehensive documentation

Link to thorough documentation that includes:

- Installation instructions
- Usage examples with screenshots
- API reference
- Troubleshooting guide

### Keep dependencies minimal

Only include necessary dependencies in your base requirements. Use optional dependencies for features like:

- Specific backends or accelerators

```toml
[project.optional-dependencies]
gpu = ["cupy", "torch"]
```

Use dependency groups for requirements that are not necessary to include in project metadata like:

- Development tools
- Documentation building

```toml
[dependency-groups]
dev = ["pytest", "pytest-cov", "ruff"]
docs = ["sphinx", "sphinx-rtd-theme"]
```
