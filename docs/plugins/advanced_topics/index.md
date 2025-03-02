# Advanced Topics

Some plugin developers may find more **in-depth, technical information** helpful. This section describes topics, such as:
- specifications for napari's plugin ecosystem using the plugin engine `npe2`.
- migration to `npe2` from the deprecated napari plugin engine v1.

## npe2: napari plugin engine v2

::::{grid}
:::{grid-item-card} npe2 manifest reference
:link: plugin-manifest
:link-type: ref

A reference for the `npe2` manifest file, which is used to define the plugin and its contributions.

:::

:::{grid-item-card} `npe2` contributions reference
:link: contributions-ref
:link-type: ref

A technical specification for how plugins can contribute additional functionality and features to napari.

:::
::::

## Deprecated: napari plugin engine v1

:::{important} Use npe2.
New plugins should use the `npe2` standard.
We encourage first generation plugin authors to migrate their plugin to the `npe2` standard.
:::

::::{grid}
:::{grid-item-card} Napari plugin engine v1 reference
:link: napari-plugin-engine
:link-type: ref

These documents provide background on the first generation plugin system which is now deprecated.

:::

:::{grid-item-card} Migration guide to `npe2`
:link: npe2-migration-guide
:link-type: ref
Have a plugin written for the first generation plugin system? This guide will help you migrate to the `npe2` plugin system.

:::

::::