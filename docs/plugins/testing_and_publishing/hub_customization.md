(hub-customization)=

# Customizing your plugin's listing on napari hub

Once your plugin is published to [PyPI](https://pypi.org/) with the `Framework :: napari` classifier, it will automatically appear on the [napari hub](https://napari-hub.org/). This guide explains how to customize your plugin's listing to provide the best experience for potential users.

## Overview

The napari hub displays information about your plugin from three sources:

1. **PyPI** - Core package metadata from your `pyproject.toml`
2. **npe2 manifest** - Plugin-specific metadata from your `napari.yaml` file
3. **GitHub** - Optional `.napari-hub/` customization files in your repository

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

Plugin authors displayed on your listing. The hub will use this information unless you provide a `CITATION.cff` file (see [Citation information](#citation-information)).

```toml
[project]
authors = [
    {name = "Jane Doe", email = "jane@example.com"},
    {name = "John Smith"},
]
```

#### License

The license under which your plugin is distributed. Use a valid [SPDX identifier](https://spdx.org/licenses/) or the string `"Other"`. The hub supports filtering by [OSI-approved](https://opensource.org/licenses) open source licenses. Modern Python packaging uses the [`license-expression` format](https://packaging.python.org/en/latest/specifications/core-metadata/#license-expression) for specifying licenses.

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

```{note}
If you specify a license that is not a valid SPDX identifier, the hub will display "Other". The hub will also attempt to detect your license from your GitHub repository if available.
```

#### Description

A detailed description of your plugin. This appears on the plugin's detail page and is indexed for search. Use your `README.md` file:

```toml
[project]
readme = "README.md"
```

The hub will render your README with proper Markdown formatting. If you begin with a Level 1 heading, it will be treated as a title and removed from the description. Use Level 2 headings to create sections - the hub will automatically generate sidebar navigation from them.

```{tip}
You can provide a hub-specific description using the `.napari-hub/DESCRIPTION.md` file in your repository (see [Hub-specific description](#hub-specific-description)).
```

#### Classifiers

Classifiers provide structured metadata about your plugin. The `Framework :: napari` classifier is required for hub visibility.

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

Specify the Python versions your plugin supports. The hub uses this for filtering:

```toml
[project]
requires-python = ">=3.10"
```

If you specify `">=3.10"`, the hub will tag your plugin as supporting Python 3.10, 3.11, 3.12, etc.

#### Dependencies

List your plugin's dependencies. The hub displays these on the detail page (excluding `napari` and `napari-plugin-engine`).

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

```{note}
If your `Homepage` URL points to a GitHub repository, it will be used as the "Source Code" link. Having a "Source Code" link is required for the hub to access your repository for additional metadata.
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

### Categories

Categories help users discover your plugin through filtering and search. The hub maps certain npe2 categories to "Workflow Steps":

```yaml
name: napari-example-plugin
# Optional: Define categories
categories: ["Segmentation", "Image Processing"]
contributions:
  commands:
    - id: napari-example-plugin.segment
      title: Segment Image
  widgets:
    - command: napari-example-plugin.segment
      display_name: Segment

```

These category values map to the hub's "Workflow Step" filter:

- `Annotation` → Workflow Step: Annotation
- `Segmentation` → Workflow Step: Segmentation
- `Image Processing` → Workflow Step: Image Processing
- `Transformations` → Workflow Step: Transformations
- `Visualization` → Workflow Step: Visualization

```{admonition} Request new categories
If you need additional categories, please [open an issue on the npe2 repository](https://github.com/napari/npe2/issues).
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

Control whether your plugin appears in hub search and listings:

```yaml
name: napari-example-plugin
visibility: public  # or "hidden"
```

- `public` (default): Plugin appears in search and listings
- `hidden`: Detail page is accessible via direct link, but plugin doesn't appear in search

```{note}
Even `hidden` plugins are installable via the napari plugin manager. To completely remove your plugin from napari and the hub, see [Removing your plugin](#removing-your-plugin-from-napari-and-the-hub).
```

## Hub-specific configuration (.napari-hub/)

For fine-grained control over your hub listing, create a `.napari-hub/` folder in your repository root. The hub will only access this folder if you've specified a "Source Code" URL pointing to your GitHub repository.

```{note}
The hub previously supported `.napari/` for configuration files, but `.napari-hub/` is now the preferred location to avoid confusion with the plugin manifest.
```

### Hub-specific description

Provide a different description for the hub by creating `.napari-hub/DESCRIPTION.md`:

```markdown
<!-- .napari-hub/DESCRIPTION.md -->

# Example Segmentation Plugin for napari

This plugin provides state-of-the-art deep learning segmentation specifically designed for microscopy images.

## Features

- Pre-trained models for common cell types
- GPU acceleration support
- Interactive parameter tuning
- Batch processing capabilities

## Getting Started

After installation, find the plugin in the `Plugins` menu...
```

This overrides your `README.md` for the hub listing only. Level 2 headings (`##`) create automatic sidebar navigation.

### Additional metadata (config.yml)

Create `.napari-hub/config.yml` for additional metadata:

```yaml
# .napari-hub/config.yml

# Image modalities your plugin supports
image_modalities:
  - Fluorescence
  - Brightfield
  - Electron Microscopy

# Data types your plugin works with
supported_data:
  - 2D
  - 3D
  - Time Series

# Override authors (if not using CITATION.cff)
authors:
  - Jane Doe
  - John Smith
  - Research Lab Team
```

```{warning}
Some fields in `config.yml` are being migrated to the npe2 manifest. Image modality and supported data may eventually move to manifest-defined categories. Check the [napari hub wiki](https://github.com/chanzuckerberg/napari-hub/wiki) for the latest information.
```

## Citation information

If your plugin has a `CITATION.cff` file in your repository root, the hub will:

1. Display citation information on your plugin's detail page
2. Allow users to download citations in various formats (BibTeX, APA, etc.)
3. Use author information from the file, overriding PyPI metadata

Example `CITATION.cff`:

```yaml
cff-version: 1.2.0
message: "If you use this plugin, please cite it as below."
title: "napari Example Segmentation Plugin"
version: 0.1.0
date-released: 2024-01-15
authors:
  - family-names: Doe
    given-names: Jane
    orcid: https://orcid.org/0000-0000-0000-0000
  - family-names: Smith
    given-names: John
repository-code: "https://github.com/username/napari-example-plugin"
license: BSD-3-Clause
```

Learn more at [Citation File Format documentation](https://citation-file-format.github.io/).

## Field reference

This table summarizes where each field is displayed and how it's sourced:

| Field | Detail Page | Listings | Search | Filter | Source | Fallback |
|-------|-------------|----------|--------|--------|--------|----------|
| Display Name | ✅ | ✅ | ✅ | - | npe2 manifest | - |
| Package Name | ✅ | ✅ | ✅ | - | PyPI | - |
| Version | ✅ | ✅ | - | - | PyPI | - |
| Summary | ✅ | ✅ | ✅ | - | PyPI | - |
| Description | ✅ | - | ✅ | - | PyPI `readme` | `.napari-hub/DESCRIPTION.md` |
| Authors | ✅ | ✅ | ✅ | - | `CITATION.cff` | PyPI, `.napari-hub/config.yml` |
| License | ✅ | - | - | ✅ (OSI) | GitHub API | PyPI |
| Python Version | ✅ | - | - | ✅ | PyPI `requires-python` | - |
| Operating System | ✅ | - | - | ✅ | PyPI classifiers | - |
| Dependencies | ✅ | - | - | - | PyPI `dependencies` | - |
| Workflow Step | ✅ | ✅ | - | ✅ | npe2 categories | `.napari-hub/config.yml` |
| Image Modality | ✅ | ✅ | - | ✅ | `.napari-hub/config.yml` | - |
| Supported Data | ✅ | - | - | ✅ | `.napari-hub/config.yml` | - |
| Plugin Type | ✅ | ✅ | - | ✅ | npe2 contributions | - |
| File Extensions (read) | ✅ | - | - | ✅ | npe2 readers | - |
| File Extensions (write) | ✅ | - | - | ✅ | npe2 writers | - |
| Layer Types (write) | ✅ | - | - | - | npe2 writers | - |
| Documentation | ✅ | - | - | - | PyPI `urls.Documentation` | - |
| Source Code | ✅ | - | - | - | PyPI `urls."Source Code"` | PyPI `urls.Homepage` |
| Bug Tracker | ✅ | - | - | - | PyPI `urls."Bug Tracker"` | - |
| User Support | ✅ | - | - | - | PyPI `urls."User Support"` | - |
| Twitter | ✅ | - | - | - | PyPI `urls.Twitter` | - |
| Release Date | ✅ | ✅ | - | ✅ | PyPI | - |
| Citation | ✅ | - | - | - | `CITATION.cff` | - |
| Visibility | - | - | - | - | npe2 manifest | `public` |

## Removing your plugin from napari and the hub

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

- ✅ Your plugin will still work when manually installed (`pip install your-plugin`)
- ❌ It won't appear in the napari plugin manager
- ❌ It won't appear on the napari hub
- ❌ It won't be automatically discovered by napari

If you want your plugin to remain installable with the napari plugin manager but not appear in search, use the `visibility: hidden` setting in your `napari.yaml` manifest instead.

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

### My custom .napari-hub files aren't being used

Ensure that:

- Your package is published to PyPI
- You included the `Framework :: napari` classifier
- Your plugin's `visibility` is not set to `hidden` (or is set to `public`)
- Your package has a valid npe2 manifest (`napari.yaml`) with a `napari.manifest` entry point

### Author information is incorrect

The hub prioritizes author information in this order:

1. `.napari-hub/config.yml` `authors` field
2. `CITATION.cff` file
3. `pyproject.toml` `authors` field

Make sure you're updating the highest priority source that exists in your project.

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

### Use meaningful categories

Choose categories that accurately reflect your plugin's functionality to help users discover it through filters.

### Keep dependencies minimal

Only include necessary dependencies in your base requirements. Use optional dpendencies for features like:

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
