This a sizeable release containing a few new exciting features and a lot of bugfixes.

### EffVer and no more _alpha_
It is our first release officially following the [EffVer versioning scheme](https://effver.org/). We also took this occasion to (finally!) remove the `Alpha` qualifier from the project ([#8288](https://github.com/napari/napari/pull/8288)), to better reflect the reality of the extensive use of napari in production. Note that these changes are just formally bringing up to date the state of the project: our development continues as before!

### Define a startup script for custom launch behaviour
Do you have a code snippet that you always find yourself running after you launch napari? No more! You can now put this code in a script and set its path in the new `startup script` setting ([#8188](https://github.com/napari/napari/pull/8188)), and it will be executed every time napari opens. It's just a python script, so sky's the limit :) We found it particularly useful for adding custom colormaps, setting up the scale bar *just right*, or automatically launching our favourite plugin on startup.

![Screenshot of the application settings menu highlighting the field for the startup script path](https://github.com/user-attachments/assets/7b0e5e5c-252b-45a0-ae76-aac88e488cbc)
### Automatically tiled overlays and ColorBar overlay
Canvas overlays such as `scale_bar`, `text_overlay`, and `colorbar` overlay are now automatically tiling ([#7836](https://github.com/napari/napari/pull/7836)), preventing annoying overlap and making them easier to use without having to manage positioning. Wait, `colorbar` overlay you said? You heard it right! This is a new overlay ([#7832](https://github.com/napari/napari/pull/7832)) that shows a color bar legend, and it works with any layer which uses a colormap. All of this works seamlessly with multiple overlays and even grid mode:

```py
import napari

viewer = napari.Viewer()

# enable grid with stride 2 to get layers split two-by-two
viewer.grid.enabled = True
viewer.grid.stride = 2

# set the scale bar to gridded mode so it appears in each grid box
viewer.scale_bar.visible = True
viewer.scale_bar.gridded = True

layers = viewer.open_sample('napari', 'lily')

# enable color bars
for layer in layers:
    layer.colorbar.visible = True
```

![Image depicting the napari viewer in grid mode with scale bars and color bars enabled](https://github.com/user-attachments/assets/622b2d36-11a7-4c55-9550-c82ddebc2fda)

Alternatively, you may also activate the `colorbar` (and other layer-related overlays such as `bounding_box`) from the graphical interface by right clicking on selected layers in the layerlist and toggling the relative entries in the **Visualization** submenu ([#8319](https://github.com/napari/napari/pull/8319)).

### Task manager will now try to prevent losing unfinished work
We added a new task manager ([#8211](https://github.com/napari/napari/pull/8211)) which automatically registers any running `thread_worker`, showing a confirmation dialog if you attempt to close napari while a task is running.

### New *remove* and *pop* methods for Points and Shapes
Points and Shapes can now be easily removed, not just added :P ([#8031](https://github.com/napari/napari/pull/8031) and [#8072](https://github.com/napari/napari/pull/8072)).

### A few shiny new updates to our website and documentation
[napari.org](https://napari.org/) can now be visited in *dark mode* ([docs#840](https://github.com/napari/docs/pull/840))! You could try out this new relaxing colorscheme while exploring the new overhauled [Preferences documentation](https://napari.org/stable/guides/preferences.html#preferences) section 😉 ([docs#834](https://github.com/napari/docs/pull/834)).
There's also new sections on [viewer overlays](https://napari.org/stable/tutorials/fundamentals/viewer.html#viewer-overlays) and [layer overlays](https://napari.org/stable/guides/layers.html#layer-overlays), to better explain how to use these old and new tools.
Our [release notes page](https://napari.org/dev/release/index.html) also received a glow-up ([docs#838](https://github.com/napari/docs/pull/838)), displaying past release highlights in collapsible boxes in the timeline. This should make it easier to quickly catch up when updating across multiple releases!

### Extra dependencies for development moved to dependency groups
A note for our contributors and plugin developers: we transferred our dev-related extra dependencies to the new python dependency groups ([#8227](https://github.com/napari/napari/pull/8227)). The installation is therefore slightly different, for example: `pip install napari --group testing` instead of `pip install napari[testing]`. The previous method will continue to work, but we will likely remove the old `optional-dependences` approach in a future release.
