(rendering)=

# Rendering

This document explains how napari produces a 2- or 3-dimensional render in
the canvas from layers' n-dimensional array-like data.
The intended audience is someone who wants to understand napari's rendering
pipeline to help optimize its performance for their usage.
Or someone that wants to contribute to and help improve the clarity or
performance of napari's rendering pipeline itself.

## Overview

At a high level, rendering in napari is simple.

1. View: `ViewerModel.dims` defines which 2D or 3D region is currently being viewed.
2. Slice: `Layer._slice_dims` loads the corresponding 2D or 3D region of the layer's ND data into RAM.
3. Render: `VispyBaseLayer._on_data_change` pushes the 2D or 3D sliced data from RAM to VRAM.

But as the details of this document reveal, rendering in napari is, in fact,
very complicated.

Consider some of the more important reasons for this.

- Multiple layers can have different extents with different transforms.
- Different layer types (e.g. Images vs. Points) handle slicing differently.
- Layer data can be large or slow to load into RAM.
- Sliced data in VRAM may exceed the maximum texture size.
- There are experimental settings that enable asynchronous slicing.

As a result, rendering in napari is the source of many bugs and performance
problems that we are actively trying to fix and improve.

## View

The region visible in napari's canvas is almost entirely determined by the state
in the `Viewer.dims`.

Specifically, `Dims.point` describes the coordinates of the slicing plane
in the world coordinate system shared across all layers.

TODO: briefly mention thick slicing, but simplify here.

Only the dimensions in `Dims.not_displayed` have meaningful values in `Dims.point`
because it is assumed that all data in displayed dimensions should be retained in
slice, even though those data may not be visible in the canvas due to the current
camera parameter values.

TODO: briefly mention multi-scale image slicing, and point to section.

## Slice

### Mapping from world coordinates to layer data coordinates

First, we need to map from the n-dimensional world coordinates shared across all
layers to a layer's specific m-dimensional data coordinates.

This involves a two-step process.

#### World to layer dimensions

The first maps the shared world dimensions to the layer dimensions.
In the case that all layers have the same number of dimensions, this mapping is
just the identity function.

In the case that layers have different numbers of dimensions, napari uses the
same approach as the numpy broadcasting rules to right-align the dimensions
to determine the mapping.

For example, let's consider the case of one 2D and one 3D layer.

| World   | 0 | 1 | 2 |
| ------- | - | - | - |
| 2DLayer |   | 0 | 1 |
| 3DLayer | 0 | 1 | 2 |

As before, the mapping from the world dimensions to the 3D layer's dimensions
is the identity function.
But the mapping from the world dimensions to the 2D layer's dimensions is a
little trickier.
In this case, the world's dimensions 1 and 2 map to the 2D layer's dimension
0 and 1 respectively.

TODO: mention and link to `Layer._world_to_layer_dims`.

For simple cases like the above, this right-alignment approach tends to work well.

But for more complex cases, it quickly runs into problems.
For example, changing the dimensions that are displayed in the canvas
(effectively defined by `ViewerModel.dims.order`) causes the mapping to change
(see [issue #3882](https://github.com/napari/napari/issues/3882)).

We would love to fix these problems.
There are few related issues and conversations, but maybe the best way to
track our progress is to follow [issue #5949](https://github.com/napari/napari/issues/5949)
which aims enrich napari's handling of dimensions in general and is on
[napari's global roadmap](https://github.com/orgs/napari/projects/24/views/1).

#### World to data coordinates

After identifying the layer's dimensions that are in view, we need to define
how we are going to slice its data across its dimensions that are *not* in view.
In order to do this, we need to map from the layer's world coordinates to
the layer's data coordinates.

This is achieved with `Layer.world_to_data` which transforms the world coordinates,
which take into account the layer's transform properties like `Layer.scale`,
`Layer.translate`, and `Layer.affine`, and convert them to data coordinates.

These data coordinates are still continuous values that may not perfectly align
with data array indices and may even fall outside of the valid range of the
layer's data array.
But after clamping and rounding the coordinates, the resulting indices can be
used to look up the sub-set of the layer's data that are in view.
The exact form of this look depends on if the layer is an image-like layer

TODO: mention that layer's with non-trivial rotations are not handled yet.

### Loading array-like image data

napari renders data out of an array-like interface. The data can be owned
by any object that supports `NumPy`'s slicing syntax. One common such
object is a [Dask](https://www.dask.org/) array. The fact that napari can
render out of any array-like data is flexible and powerful, but it means
that simple array accesses can result in the execution of arbitrary code.
For example, an array access might result disk IO or network IO, or even a
complex machine learning computation. This means array accesses can take an
arbitrary long time to complete.

### Loading multi-scale image data

With today's {class}`~napari.layers.Image` class there are no
tiles or chunks. Instead, whenever the camera is panned or zoomed napari
fetches all the data needed to draw the entire current canvas. This
actually works amazingly well with local data. Fetching the whole canvas of
data each time can be quite fast.

With remote or other high latency data, however, this method can be very
slow. Even if you pan only a tiny amount, napari has to fetch the whole
canvas worth of data, and you cannot interrupt the load to further adjust
the camera.

With `NAPARI_ASYNC` overall performance is the same, but the advantage is
you can interrupt the load by moving the camera at any time. This is a nice
improvement, but working with slow-loading data is still slow. Most large
image viewers improve on this experience with chunks or tiles. With chunks
or tiles when the image is panned the existing tiles are translated and
re-used. Then the viewer only needs to fetch tiles which newly slid onto
the screen. This style of rendering is what the `NAPARI_OCTREE` flag
enables.

## Asynchronous slicing

Since we don't know how long an array access will take, and we never want
the GUI thread to block, we should not access array-like objects in the GUI
thread. Instead, napari's rendering can be done _asynchronously_. This
means rendering proceeds at full speed drawing only the data which is in
memory ready to be drawn, while in the background worker threads load more
data into memory to be drawn in the future.

This necessarily means that napari will sometimes have to draw data that's
only partially loaded. For example, napari might have to show a lower
resolution version of the data, such that the data appears blurry until the
rest of the data has loaded in. There might even be totally blank portions
of the screen.

Although showing the user partial data is not ideal, it's vastly better
than letting the GUI thread block and napari hang. If napari stays
responsive the user stays in control. The user can sit still and watch the
data load in, or they can navigate somewhere else entirely, they are free
to choose.

Asynchronous rendering allows the user to interrupt the loading of a slice
at any time. The user can freely move the slice slider. This is especially
nice for remote or slow-loading data.

### Past

Before napari v0.4, all slicing was performed on the main thread.

From v0.4.3, two experimental implementations were introduced to perform slicing asynchronously.
These implementations could be enabled using the `NAPARI_ASYNC` and `NAPARI_OCTREE` settings.
To understand how to use these in napari v0.4, see the [associated documentation](https://napari.org/0.4.19/guides/rendering.html).

TODO: add warning that these are not well maintained and may not work at all on some later v0.4.* versions.

### Present

In napari v0.5, these implementations were removed in favor of the approach described in
[NAP-4 — Asynchronous slicing](https://napari.org/dev/naps/4-async-slicing.html), which
describes the approach in detail.

This effort is tracked by [issue #4795](https://github.com/napari/napari/issues/4795)
on [napari's global roadmap](https://github.com/orgs/napari/projects/24/views/1).
It is partially complete as an experimental setting that should at least work for
image-like layers.
To enable the experimental setting, change it in napari's settings or preference,
or set `NAPARI_ASYNC=1` as an environment variable before running napari.

The key code changes introduced so far are to push all slicing (including synchronous slicing)
through a dedicated controller `_LayerSlicer`.
And to define all the layer-specific slicing logic in dedicated callable
classes (e.g. `_ImageSliceRequest`) that capture all the state needed to perform
slicing and can be executed asynchronously on another thread without needing to
guard access with locks.

These new additions make following the old synchronous slicing code paths more complicated.
But eventually we hope to mostly remove those complications and make synchronous
and asynchronous slicing easy enough to follow.

### Future

TODO: link to progressive rendering issue.