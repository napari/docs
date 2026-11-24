[#6542](https://github.com/napari/napari/pull/6542) made a number of
deprecations to the Labels API to simplify it. Rather than having color-related
properties strewn all over the layer, color control is moved strictly to the
layer's `colormap`. Here is the full list of deprecated attributes and their
replacements:

- num_colors: `layer.num_colors` becomes `len(layer.colormap)`.
  `layer.num_colors = n` becomes `layer.colormap = label_colormap(n)`.
- `napari.utils.colormaps.LabelColormap` is deprecated and has been renamed to
  `napari.utils.colormaps.CyclicLabelColormap`.
- color: `layer.color` becomes `layer.colormap.color_dict`.
  `layer.color = color_dict` becomes
  `layer.colormap = DirectLabelColormap(color_dict)`.
- _background_label: `layer._background_label` is now at
  `layer.colormap.background_value`.
- color_mode: `layer.color_mode` is set by setting the colormap using the
  corresponding colormap type (`CyclicLabelColormap` or `DirectLabelColormap`;
  these classes can be imported from `napari.utils.colormaps`.).
- `seed`: was only used for shifting labels around in [0, 1]. It is
  superseded by `layer.new_colormap()` which was implemented in
  [#6460](https://github.com/napari/napari/pull/6460).
