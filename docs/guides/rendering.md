(rendering)=

# Rendering

This document explains how napari produces a 2- or 3-dimensional render in
the canvas from layers' n-dimensional array-like data.
The intended audience is someone who wants to understand napari's rendering
pipeline to help optimize its performance for their usage.
Or someone that wants to help improve the clarity or performance of napari's
rendering pipeline itself.

## Overview

At a high level, rendering in napari is simple.

1. View: `Viewer.dims` determines which 2D or 3D region is currently in view.
2. Slice: the 2D or 3D region of the layer's ND data is loaded into RAM.
3. Render: the 2D or 3D sliced data is pushed from RAM to VRAM.

But as the details of this document reveal, rendering in napari is, in fact,
very complicated.
Consider some of the more important reasons for this.

- Multiple layers can have different extents with different sampling properties.
- Different layer types (e.g. Images vs. Points) handle slicing differently.
- Layer data can be large or slow to load into RAM.
- Sliced data in VRAM may exceed the maximum texture size.

As a result, rendering in napari is the source of many bugs and performance
problems that we are actively trying to fix and improve.

## View region

The region visible in napari's canvas is almost entirely determined by the state
in the `Viewer.dims`.

Specifically, `Dims.point` describes the coordinates of the slicing (hyper)plane
in the world coordinate shared across all layers.

TODO: briefly mention thick slicing, but simplify here.

Only the dimensions in `Dims.not_displayed` have meaningful values in `Dims.point`
because it is assumed that all data in displayed dimensions should be sliced
(though may not be visible in the canvas due to the current camera parameter values).


## Slicing

### Map from ND world coordinates to N'D layer data coordinates

First, we need to map from ND world coordinates to N'D layer data coordinates.


## Array-like images

napari renders data out of an array-like interface. The data can be owned
by any object that supports `NumPy`'s slicing syntax. One common such
object is a [Dask](https://www.dask.org/) array. The fact that napari can
render out of any array-like data is flexible and powerful, but it means
that simple array accesses can result in the execution of arbitrary code.
For example, an array access might result disk IO or network IO, or even a
complex machine learning computation. This means array accesses can take an
arbitrary long time to complete.


## Multi-scale images




## Asynchronous slicing

### Past

Before napari v0.4, all slicing was performed on the main thread.
From v0.4.3, two experimental implementations were introduced to perform slicing asynchronously.
These implementations could be enabled using the `NAPARI_ASYNC` and `NAPARI_OCTREE` settings.
To understand how to use these in napari v0.4, see the [associated documentation](https://napari.org/0.4.19/guides/rendering.html).
In napari v0.5, these implementations were removed in favor of the approach described in [NAP-4 — Asynchronous slicing](https://napari.org/dev/naps/4-async-slicing.html).


### Present


### Future

Since we don't know how long an array access will take, and we never want
the GUI thread to block, we cannot access array-like objects in the GUI
thread. Instead, napari's rendering has to be done _asynchronously_. This
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


Running napari with `NAPARI_ASYNC=1` enables asynchronous rendering using
the existing {class}`~napari.layers.Image` class. The
{class}`~napari.layers.Image` class will no longer call
`np.asarray()` in the GUI thread. We do this so that if `np.asarray()`
blocks on IO or a computation, the GUI thread will not block and the
framerate will not suffer.


Asynchronous rendering allows the user to interrupt the loading of a slice
at any time. The user can freely move the slice slider. This is especially
nice for remote or slow-loading data.

To avoid blocking the GUI thread the
{class}`~napari.layers.Image` class will load chunks using the
new {class}`~napari.components.experimental.chunk._loader.ChunkLoader`
class. The
{class}`~napari.components.experimental.chunk._loader.ChunkLoader` will
call `np.asarray()` in a worker thread. When the worker thread finishes
it will call {meth}`~napari.layers.Image.on_chunk_loaded` with
the loaded data. The next frame {class}`~napari.layers.Image`
can display the new data.

Without `NAPARI_ASYNC` napari will block when switching slices. Napari
will hang until the new slice has loaded. If the slice loads slowly enough
you might see the "spinning wheel of death" on a Mac indicating the process
is hung.

### Multi-scale images

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
