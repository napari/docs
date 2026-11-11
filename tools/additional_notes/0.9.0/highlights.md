### Auto-labelling of viewer axes

napari 0.5.0 laid the ground work for more accurate metadata handling by
allowing users and plugins to set the `axis_labels` on layers. napari 0.9.0
*finally* capitalises on that work by automatically labelling viewer axes based
on the axis labels of layers present in the viewer.
([#9282](https://github.com/napari/napari/pull/9282))

Now, opening a dataset with labelled axes will result in correctly labelled
axes in the viewer:

![napari screenshot showing inherited labeled viewer axes](../_static/images/axis-labels.png)

Additionally, when you create a new layer from an existing one using the
buttons in the GUI, the new layer now inherits the axis labels of the layer(s)
it was derived from. ([#9293](https://github.com/napari/napari/pull/9293))

There is still work to be done here. For example, if layers have labels that
are inconsistent with each other, napari will simply ignore layers with fewer
dimensions, or layers added later. But, for most use cases, layer and viewer
metadata will now be much more informative!

### Xarray metadata is now inherited

In the same vein, if you work with [Xarray](https://docs.xarray.dev/) — common in climate,
geoscience, and many places where data ships with labelled coordinates — napari
now reads metadata straight from your `DataArray`s. When you add an xarray
object to the viewer, napari will use its dimension names as axis labels, infer
`scale` and `translate` from the coordinate values, and pick up `units` from
CF-convention `units` attributes on coordinates ([#9316](https://github.com/napari/napari/pull/9316)).
This closed an 8-year old, double-digit, nearly-as-old-as-napari-itself issue!
([#14](https://github.com/napari/napari/issues/14))

### Status bar coordinates as floats

Continuing on the theme of improved metadata, when scale and/or unit metadata
is set on the layer, the status bar coordinates now have increased precision,
where before they were limited to just integers. This means you can have more
accurate physical estimates of your data coordinates when exploring data.
([#9287](https://github.com/napari/napari/pull/9287))

### Layer controls for multiple selected layers

Until now, layer controls only appeared when a single layer was selected. Now,
napari dynamically builds the layer controls from your selection, so
when you select several layers at once you can see and use the controls that
are shared between them. Pan-zoom is always available, while the layer-specific
buttons still appear only when a single layer is selected.
([#9318](https://github.com/napari/napari/pull/9318))

```{raw} html
<figure>
  <video width="100%" controls autoplay loop muted playsinline>
    <source src="../_static/images/joint-controls.webm" type="video/webm" />
    <source src="../_static/images/joint-controls.mp4" type="video/mp4" />
    <img src="../_static/images/joint-controls.png"
      title="Your browser does not support the video tag"
      alt="Video showing the editing of multiple selected layers at once."
    >
  </video>
</figure>
```

There's also an experimental setting, *Generate GUI layer controls dynamically
instead of using premade panels*, that makes napari use the new dynamic
controls even for single layers.

### Take a guided tour of the viewer

New to napari, or just want a quick refresher on where everything lives? There's
now a guided tour, available from **Help → Take a tour**. The tour highlights
the main areas of the viewer — the canvas, the layer list, layer controls, the
viewer buttons, the dimension sliders, and the status bar — so you can get your
bearings in seconds. If the viewer is empty, napari opens the built-in *Balls
(3D)* sample data so the walkthrough has something to show ([#9290](https://github.com/napari/napari/pull/9290)).

![Screenshot of the napari viewer guided tour][../_static/images/guided-tour.png)

### Contributable plugin preferences

Plugins can now ship their own preferences ([#9308](https://github.com/napari/napari/pull/9308))!
By declaring `configurations` in
their `napari.yaml` manifest, plugins get their own settings — stored
separately from napari's own settings, automatically added to and editable from
the napari **Preferences** dialog, and accessible programmatically from Python:

```python
from napari.settings import get_plugin_settings

settings = get_plugin_settings("my-plugin")
settings.reader.lazy = True
```

Read more in the [Configurations Guide](https://napari.org/dev/plugins/building_a_plugin/guides.html#configurations)
to learn more about how to add this new contribution to your own plugins.

### Adjust grid rendering with hidden layers

Grid mode with hidden layers is much improved: empty
grid spaces are never shown and stride operates on the *full* layer list, so
layer grouping doesn't change when you show or hide layers ([#9244](https://github.com/napari/napari/pull/9244)).

### Fuzzy find in command palette

Have you used our [command palette](command-palette) yet? It's a great way to
quickly access and even discover napari functionality. Now, thanks to
[#8661](https://github.com/napari/napari/pull/8661), it's easier to find
functions when you don't know the exact name, or you mistyped something. You'll
need to have [rapidfuzz](https://rapidfuzz.github.io/RapidFuzz/) installed to
make use of it. It's automatically installed with `napari[all]` or
`napari[optional]`. And if the search feels a bit off, you can set just how
fuzzy you want it to be in Preferences > Experimental > Fuzzy Search Threshold.

![Example of fuzzy find using "scle" to find "scale"](https://github.com/user-attachments/assets/88d4d2e1-36e1-4921-8df6-6f8ded4df12e)

### 2D slicing of surfaces

Ever since we added surfaces, they have been invisible in 2D slices. Now,
thanks to all the work done on [thick slicing](thick-slicing), surface
slices appear in 2D view ([#8783](https://github.com/napari/napari/pull/8783)).
This enhancement is accompanied by support for async slicing, which should
improve viewer responsiveness when slicing large, time varying surfaces, for
example.

```{raw} html
<figure>
  <video width="100%" controls autoplay loop muted playsinline>
    <source src="../_static/images/slicing_surface.webm" type="video/webm" />
    <source src="../_static/images/slicing_surface.mp4" type="video/mp4" />
    <img src="../_static/images/slicing_surface.png"
      title="Your browser does not support the video tag"
      alt="Video showing a slicing of surface layers, with showing how to change thickness of slize and controlling slice mmode."
    >
  </video>
</figure>
```

... And you can try this out yourself with common .obj surface files thanks to
a new built-in reader plugin!
([#9228](https://github.com/napari/napari/pull/9228))

You should now be able to drag and drop .obj files into napari and see them
instantly.

### Public API for auto contrast limits

For a very long time, it's been possible to set automatic contrast limits
updating on a layer *only* through the graphical user interface. This means an
extra click for many workflows and poorer reproducibility. Thanks to
[#9271](https://github.com/napari/napari/pull/9271), you can now set the
`auto_contrast` attribute on Image layers:

```python
image_layer = viewer.add_image(..., auto_contrast=True)
# or
image_layer.auto_contrast = True
```

### The life-changing magic of tidying up the Viewer model

The napari Viewer model, for historical reasons, is a grab-bag of *many*
attributes, which makes usage, discoverability, and code modularity and
composability a major issue. We've taken some *big* steps towards cleaning up
one of our most important namespaces by creating Canvas
([#8633](https://github.com/napari/napari/pull/8633)) and Scene
([#9323](https://github.com/napari/napari/pull/9323)) models, which cleans up
([#9363](https://github.com/napari/napari/pull/9363)) and clarifies
([napari/docs#1083](https://github.com/napari/docs/pull/1083)) many parts of
the API.

The old API is in extremely widespread use, so although it is silently
deprecated, it will continue to work for the foreseeable future. In the
meantime, the new API should be much friendlier to work with by carefully
grouping related concepts and APIs. Some examples:

- `viewer.axes` and `viewer.floating_axes` become `viewer.scene.overlays.axes`
  and `viewer.canvas.overlays.axes`.
- From that API, you may also guess that the scale bar is on
  `viewer.canvas.overlays.scale_bar`.
- You can even get a list of the current overlays (both visible and invisible)
  with `list(viewer.canvas.overlays)` and `list(viewer.scene.overlays)`. (But
  do note that overlays with a `_` prefix are private and may change!)
- `viewer.camera` is now `viewer.scene.camera`.
- Grid mode is now accessed at `viewer.canvas.grid` (e.g.
  `viewer.canvas.grid.enabled = True`).

This has also enabled a new public API: you can now query the canvas size (in
pixels) without accessing private napari APIs! Check `viewer.canvas.size`!

The TL;DR:

```python
# Canvas Model
viewer.scale_bar -> viewer.canvas.overlays.scale_bar
viewer.text_overlay -> viewer.canvas.overlays.text
viewer.floating_axes -> viewer.canvas.overlays.axes
viewer.grid -> viewer.canvas.grid
NOW EXPOSED -> viewer.canvas.overlays.current_slice
NEW -> viewer.canvas.overlay_tiling
NEW -> viewer.canvas.background_color & viewer.canvas.background_color_override
NEW -> viewer.canvas.size

# Scene Model
viewer.camera -> viewer.scene.camera
viewer.axes -> viewer.scene.overlays.axes
```

### Removal of translation code

Several years ago, we started working on implementing localization machinery
into napari. Unfortunately, this work has been sitting unfinished and unused,
while making maintaining napari harder. Given the extra maintenance burden
without benefit, we made the difficult decision to remove it from our codebase
([#8935](https://github.com/napari/napari/pull/8935)), with the hope that in
the future we might restart this effort with a better plan.

We do aim to revisit when napari's foundations are more solid, but for now,
`napari.utils.translations` is deprecated. If you have this code in your
codebase:

```
from napari.utils import translations as trans
```

please remove it. (For now, `trans._()` is a no-op.)
