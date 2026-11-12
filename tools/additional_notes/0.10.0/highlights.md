This release contains several new features and many enhancements and bugfixes. We also welcomed a ton of new contributors to the community!

### Coordinate Grid with axes and ticks
This features has been requested for years, and we finally managed to get a version that we're happy with! With [#7827](https://github.com/napari/napari/pull/7827), you can now use `viewer.scene.overlays.coordinate_grid` to display a grid on your data, including unit-aware tick marks and axis labels! Try it out:

```py
import napari

viewer = napari.Viewer(ndisplay=3)
layers = viewer.open_sample('napari', 'cells3d')

for layer in layers:
    layer.units = 'nm'
    layer.axis_labels = ['z', 'y', 'x']

viewer.scene.overlays.coordinate_grid.visible = True
```

![screenshot of the viewer with the coordinate_grid overlay enabled, showing the grid with axis labels and units, and axis ticks](https://github.com/user-attachments/assets/54993979-4774-4e66-87fb-d1bfcb27fb98)

### Colorful names

Another long-requested feature: displaying [layer names](https://napari.org/stable/getting_started/layers.html#layer-overlays) on the canvas now has colormap-aware colors ([#9598](https://github.com/napari/napari/pull/9598))! This comes with some fancy machinery to ensure that colors are shifted enough to be always readable.

```py
import napari

viewer = napari.Viewer()
layers = viewer.open_sample('napari', 'lily')

for layer in layers:
    layer.name_overlay.visible = True

viewer.canvas.grid.enabled = True
viewer.canvas.grid.stride = 2
```

![screenshot of the viewer with layer names overlays enabled, colored based on each layer's colormap](https://github.com/user-attachments/assets/629e63f5-381a-4a92-ba17-de02fa408edf)

### Cursor crosshair

Ever use the [grid mode](https://napari.org/stable/gallery/grid_mode.html#grid-mode) for your multichannel data but then struggle to know where you're clicking? Struggle no more! You can now enable the new crosshair overlay ([#8017](https://github.com/napari/napari/pull/8017)) to always locate your exact position in every viewbox.

![screenshot of the viewer with grid-mode and the crosshair enabled](https://github.com/user-attachments/assets/cff866f3-fa28-42a8-a8df-94062b118573)

### Default dock area and tabify for plugin dock widgets

Some plugin dock widgets are wider than they are tall, fitting poorly on the right-side dock and forcing users to manually move the widget to a different area every time on first launch. With [#9526](https://github.com/napari/napari/pull/9526)) and ([#9707](https://github.com/napari/napari/pull/9707), you can now specify a default dock area and tabify behaviour for a dock widget contribution, which will prevent the need for this manual rearranging step:

```yaml
  widgets:
    - command: example-plugin.my_widget
      display_name: My wide widget
      default_dock_area: bottom
      tabify: True
```
