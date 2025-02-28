# Advanced Topics

Some plugin developers may find more **in-depth, technical information** helpful. This section describes topics, such as:
- specifications for napari's plugin ecosystem using the standard plugin engine `npe2`.
- migration to the present standard plugin engine `npe2` from the deprecated plugin engine, napari plugin engine v1.
- reference documentation about the deprecated napari plugin engine v1.

## npe2 advanced topics and reference

::::{grid}
:::{grid-item-card} Migration guide to `npe2`
:link: npe2-migration-guide
:link-type: ref
Have a plugin written for the first generation plugin system? This guide will help you migrate to the `npe2` plugin system.

:::

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

## Deprecated v1 napari plugin engine reference

::::{grid}
:::{grid-item-card} First generation napari plugin engine v1
:link: napari-plugin-engine
:link-type: ref

These documents provide background on the first generation plugin system which is now deprecated.

New plugins should use the `npe2` standard.
We encourage first generation plugin authors to migrate their plugin to the `npe2` standard.

:::
::::