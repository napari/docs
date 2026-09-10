napari 0.5.0 is the beginning of an architectural overhaul of napari. The
architecture improvements, which are still ongoing, enable more responsive
asynchronous loading when slicing layers or panning and zooming in multiscale
2D layers ([#5816](https://github.com/napari/napari/pull/5816)). There's
several performance improvements, too, including faster points layer creation
and updates ([#6727](https://github.com/napari/napari/pull/6727)).

Other architectural changes, refactoring napari on top of
[app-model](https://app-model.readthedocs.io/en/latest/), have enabled us to
(finally 😅) implement [NAP-6](nap-6-contributable-menus), which allows
plugins to organize their commands in defined menus in the napari menubar
and application. Please read [NAP-6](nap-6-contributable-menus) for all the
juicy details, including how to request more menus if the existing ones don't
meet your needs. 📋 ([#7011](https://github.com/napari/napari/pull/7011))

Another important development for plugins is that we have added fields for
axis names and physical units in layers
([#6979](https://github.com/napari/napari/pull/6979)). If you implement a
reader plugin, you can now specify the names of the axes in the data that you
are reading in, and the physical units of the scale and other transformations.
Currently, napari is *not* using this information, but we will in upcoming
versions, so plugins should start providing this information if they have it.

There's plenty of new features, too, including a polygon drawing tool when
painting labels ([#5806](https://github.com/napari/napari/pull/5806)),
pinch-to-zoom ([#5859](https://github.com/napari/napari/pull/5859)), better
ways to show/hide individual layers when exploring your data
([#5574](https://github.com/napari/napari/pull/5574))
([#5618](https://github.com/napari/napari/pull/5618)), creating a layer from
an image or URL in your clipboard
([#6532](https://github.com/napari/napari/pull/6532)),
a new way to export figure-quality renderings from the canvas
([#6730](https://github.com/napari/napari/pull/6730)) (2D-only for now),
and the ability to copy and paste spatial metadata (scale, translate, etc)
between layers ([#6864](https://github.com/napari/napari/pull/6864)).

You'll also note a new little button on layer controls, including images:

```{image} ../images/transform-icon.svg
:alt: transform layer icon
:width: 100px
:align: center
```

This little button allows you to resize and rotate layers, enabling manual
alignment ([#6794](https://github.com/napari/napari/pull/6794))!

All in all, this release has over 20 new features and over 100 bug fixes and
improvements. Please see below for the full list of changes since 0.4.19.
