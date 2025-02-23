(plugins-index)=

# Plugins

Plugins extend napari's functionality, allowing for customization and sharing with the community.
While you can use scripts and widgets to extend napari, plugins provide great flexibility.
Existing plugins extend napari to add:

- support for import and export of image and related data types.
- support for working with specialized data formats.
- domain specific features, including microscopy, climate, geoscience, and more.

Share and discover napari plugins on [napari hub](https://napari-hub.org),
[PyPI](https://pypi.org/search/?q=napari), or [conda-forge](https://conda-forge.org/packages/).
Interested in creating a plugin? A [napari-plugin-template](https://github.com/napari/napari-plugin-template),
a [copier](https://copier.readthedocs.io/en/stable/) template, bootstraps authoring
[npe](https://github.com/napari/npe2)-based napari plugins.

## Plugin users

Check out the user focused guides for installing and using napari plugins.

::::{grid} Plugin Users
:::{grid-item-card} Start using plugins
:link: plugins-getting-started
:link-type: ref

Introduction to napari plugins, what they can provide, and where to get support.
:::

:::{grid-item-card} Finding and installing plugins
:link: find-and-install-plugins
:link-type: ref

How to find and install plugins using the napari plugin installer or napari hub.
:::
::::

## Plugin Developers

Check out our plugin developer guides to start creating your own napari plugins.

::::{grid}
:::{grid-item-card} Building a plugin
:link: how-to-build-a-plugin
:link-type: ref
In depth guides to build a plugin for napari.

:::

:::{grid-item-card} Virtual environments and useful tools
:link: virtual-environments-and-useful-tools
:link-type: ref

Workshop on virtual environments and useful tools for plugin development.

::::

::::{grid}
:::{grid-item-card} Testing and publishing
:link: plugin-test-deploy
:link-type: ref

How to test your plugin works and how to publish it,
along with some tips for making your plugin easy to find.
:::

:::{grid-item-card} Technical references
:link: plugin-technical-references
:link-type: ref

Technical references for the plugin system and the plugin API
and guides to convert from first generation plugins to npe2.
:::
::::
:::::
