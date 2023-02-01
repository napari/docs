---
theme:
  metaDescription: Napari is a fast multi-dimensional image viewer for Python. It can help you **explore** any image-like data, be it 2D, 3D, or even higher-dimensional. It can also help you **overlay** downstream or **associated data**, such as point coordinates or segmentations, which you can use to **annotate** and **proofread** your image data.
  quickLinks:
    - title: Community
      content: Meet the team, our mission, and our values
      url: /community/index.html

    - title: Tutorials
      content: Step by step guides for common napari workflows
      url: /tutorials/index.html

    - title: Plugins
      content: Learn how to create a plugin that works with the napari ecosystem
      url: /plugins/index.html

    - title: Release notes
      content: See what’s been updated in the latest releases
      url: /release/index.html

    - title: API reference
      content: Information on specific functions, classes, and methods
      url: /api/index.html

    - title: Roadmaps
      content: Find out what we plan to build next and into the near future
      url: /roadmaps/index.html

    - title: Developer guides
      content: Explanations about how napari works behind the screen
      url: /guides/index.html

    - title: Developer resources
      content: All you need to know to contribute to the napari codebase
      url: /developers/index.html

    - title: Source code
      content: Jump out to GitHub to take a look at the code that runs napari
      url: https://github.com/napari/napari

    - title: napari hub
      content: Discover, install, and share napari plugins
      url: https://www.napari-hub.org
---

# napari

```python
from skimage.data import cells3d
import napari

viewer, layers = napari.imshow(cells3d(), channel_axis=1)
```

![napari viewer showing 3D cells image](images/multichannel_cells.png)

## A multi-dimensional image viewer for Python

Napari is a fast multi-dimensional image viewer for Python. It can help you
**explore** any image-like data, be it 2D, 3D, or even higher-dimensional. It
can also help you **overlay** downstream or **associated data**, such as point
coordinates or segmentations, which you can use to **annotate** and
**proofread** your image data.

::::{grid}
:::{grid-item-card} Examples gallery
:link: gallery
:link-type: ref

See some of the things napari can do.
:::

:::{grid-item-card} Installation
:link: installation
:link-type: ref

How to install napari.
:::

::::

::::{grid}
:::{grid-item-card} Getting started
:link: getting_started
:link-type: ref

Get started with napari.
:::

:::{grid-item-card} Community
:link: community
:link-type: ref

Forums, web chat, video chat, and more! Join us!
:::

::::

