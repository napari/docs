## Layers controls
### Dependencies diagram (related `napari` modules)
```{mermaid}
graph LR
	napari._qt(napari._qt)
	napari._qt --> napari._qt.qt_main_window
	click napari._qt "https://github.com/napari/napari/tree/main/napari/_qt/__init__.py" _blank
	napari._qt.layer_controls(napari._qt.layer_controls)
	napari._qt.layer_controls --> napari._qt.layer_controls.qt_layer_controls_container
	click napari._qt.layer_controls "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/__init__.py" _blank
	napari._qt.layer_controls.qt_colormap_combobox(napari._qt.layer_controls.qt_colormap_combobox)
	click napari._qt.layer_controls.qt_colormap_combobox "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_colormap_combobox.py" _blank
	napari._qt.layer_controls.qt_image_controls(napari._qt.layer_controls.qt_image_controls)
	napari._qt.layer_controls.qt_image_controls --> napari._qt.layer_controls.qt_image_controls_base
	napari._qt.layer_controls.qt_image_controls --> napari._qt.utils
	napari._qt.layer_controls.qt_image_controls --> napari.layers
	click napari._qt.layer_controls.qt_image_controls "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_image_controls.py" _blank
	napari._qt.layer_controls.qt_image_controls_base(napari._qt.layer_controls.qt_image_controls_base)
	napari._qt.layer_controls.qt_image_controls_base --> napari._qt.layer_controls.qt_colormap_combobox
	napari._qt.layer_controls.qt_image_controls_base --> napari._qt.layer_controls.qt_layer_controls_base
	napari._qt.layer_controls.qt_image_controls_base --> napari._qt.utils
	napari._qt.layer_controls.qt_image_controls_base --> napari._qt.widgets._slider_compat
	napari._qt.layer_controls.qt_image_controls_base --> napari._qt.widgets.qt_range_slider_popup
	napari._qt.layer_controls.qt_image_controls_base --> napari.layers
	click napari._qt.layer_controls.qt_image_controls_base "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_image_controls_base.py" _blank
	napari._qt.layer_controls.qt_labels_controls(napari._qt.layer_controls.qt_labels_controls)
	napari._qt.layer_controls.qt_labels_controls --> napari._qt.layer_controls.qt_layer_controls_base
	napari._qt.layer_controls.qt_labels_controls --> napari._qt.utils
	napari._qt.layer_controls.qt_labels_controls --> napari._qt.widgets._slider_compat
	napari._qt.layer_controls.qt_labels_controls --> napari._qt.widgets.qt_mode_buttons
	napari._qt.layer_controls.qt_labels_controls --> napari.layers
	click napari._qt.layer_controls.qt_labels_controls "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_labels_controls.py" _blank
	napari._qt.layer_controls.qt_layer_controls_base(napari._qt.layer_controls.qt_layer_controls_base)
	napari._qt.layer_controls.qt_layer_controls_base --> napari._qt.widgets._slider_compat
	napari._qt.layer_controls.qt_layer_controls_base --> napari.layers
	click napari._qt.layer_controls.qt_layer_controls_base "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_layer_controls_base.py" _blank
	napari._qt.layer_controls.qt_layer_controls_container(napari._qt.layer_controls.qt_layer_controls_container)
	napari._qt.layer_controls.qt_layer_controls_container --> napari._qt.layer_controls.qt_image_controls
	napari._qt.layer_controls.qt_layer_controls_container --> napari._qt.layer_controls.qt_labels_controls
	napari._qt.layer_controls.qt_layer_controls_container --> napari._qt.layer_controls.qt_points_controls
	napari._qt.layer_controls.qt_layer_controls_container --> napari._qt.layer_controls.qt_shapes_controls
	napari._qt.layer_controls.qt_layer_controls_container --> napari._qt.layer_controls.qt_surface_controls
	napari._qt.layer_controls.qt_layer_controls_container --> napari._qt.layer_controls.qt_tracks_controls
	napari._qt.layer_controls.qt_layer_controls_container --> napari._qt.layer_controls.qt_vectors_controls
	napari._qt.layer_controls.qt_layer_controls_container --> napari.layers
	click napari._qt.layer_controls.qt_layer_controls_container "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_layer_controls_container.py" _blank
	napari._qt.layer_controls.qt_points_controls(napari._qt.layer_controls.qt_points_controls)
	napari._qt.layer_controls.qt_points_controls --> napari._qt.layer_controls.qt_layer_controls_base
	napari._qt.layer_controls.qt_points_controls --> napari._qt.utils
	napari._qt.layer_controls.qt_points_controls --> napari._qt.widgets._slider_compat
	napari._qt.layer_controls.qt_points_controls --> napari._qt.widgets.qt_color_swatch
	napari._qt.layer_controls.qt_points_controls --> napari._qt.widgets.qt_mode_buttons
	napari._qt.layer_controls.qt_points_controls --> napari.layers
	click napari._qt.layer_controls.qt_points_controls "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_points_controls.py" _blank
	napari._qt.layer_controls.qt_shapes_controls(napari._qt.layer_controls.qt_shapes_controls)
	napari._qt.layer_controls.qt_shapes_controls --> napari._qt.layer_controls.qt_layer_controls_base
	napari._qt.layer_controls.qt_shapes_controls --> napari._qt.utils
	napari._qt.layer_controls.qt_shapes_controls --> napari._qt.widgets._slider_compat
	napari._qt.layer_controls.qt_shapes_controls --> napari._qt.widgets.qt_color_swatch
	napari._qt.layer_controls.qt_shapes_controls --> napari._qt.widgets.qt_mode_buttons
	napari._qt.layer_controls.qt_shapes_controls --> napari.layers
	click napari._qt.layer_controls.qt_shapes_controls "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_shapes_controls.py" _blank
	napari._qt.layer_controls.qt_surface_controls(napari._qt.layer_controls.qt_surface_controls)
	napari._qt.layer_controls.qt_surface_controls --> napari._qt.layer_controls.qt_image_controls_base
	napari._qt.layer_controls.qt_surface_controls --> napari.layers
	click napari._qt.layer_controls.qt_surface_controls "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_surface_controls.py" _blank
	napari._qt.layer_controls.qt_tracks_controls(napari._qt.layer_controls.qt_tracks_controls)
	napari._qt.layer_controls.qt_tracks_controls --> napari._qt.layer_controls.qt_layer_controls_base
	napari._qt.layer_controls.qt_tracks_controls --> napari._qt.utils
	napari._qt.layer_controls.qt_tracks_controls --> napari.layers
	click napari._qt.layer_controls.qt_tracks_controls "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_tracks_controls.py" _blank
	napari._qt.layer_controls.qt_vectors_controls(napari._qt.layer_controls.qt_vectors_controls)
	napari._qt.layer_controls.qt_vectors_controls --> napari._qt.layer_controls.qt_layer_controls_base
	napari._qt.layer_controls.qt_vectors_controls --> napari._qt.utils
	napari._qt.layer_controls.qt_vectors_controls --> napari._qt.widgets.qt_color_swatch
	napari._qt.layer_controls.qt_vectors_controls --> napari.layers
	click napari._qt.layer_controls.qt_vectors_controls "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/qt_vectors_controls.py" _blank
	napari._qt.qt_main_window(napari._qt.qt_main_window)
	napari._qt.qt_main_window --> napari._qt.qt_viewer
	napari._qt.qt_main_window --> napari._qt.utils
	napari._qt.qt_main_window --> napari._qt.widgets.qt_viewer_dock_widget
	click napari._qt.qt_main_window "https://github.com/napari/napari/tree/main/napari/_qt/qt_main_window.py" _blank
	napari._qt.qt_viewer(napari._qt.qt_viewer)
	napari._qt.qt_viewer --> napari._qt.layer_controls
	napari._qt.qt_viewer --> napari._qt.utils
	napari._qt.qt_viewer --> napari._qt.widgets.qt_viewer_dock_widget
	napari._qt.qt_viewer --> napari.components
	napari._qt.qt_viewer --> napari.components._interaction_box_mouse_bindings
	napari._qt.qt_viewer --> napari.components.layerlist
	napari._qt.qt_viewer --> napari.layers
	click napari._qt.qt_viewer "https://github.com/napari/napari/tree/main/napari/_qt/qt_viewer.py" _blank
	napari._qt.utils(napari._qt.utils)
	click napari._qt.utils "https://github.com/napari/napari/tree/main/napari/_qt/utils.py" _blank
	napari._qt.widgets._slider_compat(napari._qt.widgets._slider_compat)
	click napari._qt.widgets._slider_compat "https://github.com/napari/napari/tree/main/napari/_qt/widgets/_slider_compat.py" _blank
	napari._qt.widgets.qt_color_swatch(napari._qt.widgets.qt_color_swatch)
	click napari._qt.widgets.qt_color_swatch "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_color_swatch.py" _blank
	napari._qt.widgets.qt_mode_buttons(napari._qt.widgets.qt_mode_buttons)
	click napari._qt.widgets.qt_mode_buttons "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_mode_buttons.py" _blank
	napari._qt.widgets.qt_range_slider_popup(napari._qt.widgets.qt_range_slider_popup)
	click napari._qt.widgets.qt_range_slider_popup "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_range_slider_popup.py" _blank
	napari._qt.widgets.qt_viewer_dock_widget(napari._qt.widgets.qt_viewer_dock_widget)
	napari._qt.widgets.qt_viewer_dock_widget --> napari._qt.qt_viewer
	napari._qt.widgets.qt_viewer_dock_widget --> napari._qt.utils
	click napari._qt.widgets.qt_viewer_dock_widget "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_viewer_dock_widget.py" _blank
	napari.components(napari.components)
	napari.components --> napari.components.layerlist
	click napari.components "https://github.com/napari/napari/tree/main/napari/components/__init__.py" _blank
	napari.components._interaction_box_mouse_bindings(napari.components._interaction_box_mouse_bindings)
	napari.components._interaction_box_mouse_bindings --> napari.layers
	click napari.components._interaction_box_mouse_bindings "https://github.com/napari/napari/tree/main/napari/components/_interaction_box_mouse_bindings.py" _blank
	napari.components.layerlist(napari.components.layerlist)
	napari.components.layerlist --> napari.layers
	click napari.components.layerlist "https://github.com/napari/napari/tree/main/napari/components/layerlist.py" _blank
	napari.layers(napari.layers)
	click napari.layers "https://github.com/napari/napari/tree/main/napari/layers/__init__.py" _blank
	classDef default fill:#00c3ff,color:black;
	linkStyle default stroke:#00c3ff
	classDef external fill:#ffa600,color:black;
```
### Source code directory layout (related to modules inside `napari`)
```
napari/
├─components/
│ ├─layerlist.py
│ ├─_interaction_box_mouse_bindings.py
│ └─__init__.py
├─layers/
│ └─__init__.py
└─_qt/
  ├─layer_controls/
  │ ├─qt_colormap_combobox.py
  │ ├─qt_image_controls.py
  │ ├─qt_image_controls_base.py
  │ ├─qt_labels_controls.py
  │ ├─qt_layer_controls_base.py
  │ ├─qt_layer_controls_container.py
  │ ├─qt_points_controls.py
  │ ├─qt_shapes_controls.py
  │ ├─qt_surface_controls.py
  │ ├─qt_tracks_controls.py
  │ ├─qt_vectors_controls.py
  │ └─__init__.py
  ├─qt_main_window.py
  ├─qt_viewer.py
  ├─utils.py
  ├─widgets/
  │ ├─qt_color_swatch.py
  │ ├─qt_mode_buttons.py
  │ ├─qt_range_slider_popup.py
  │ ├─qt_viewer_dock_widget.py
  │ └─_slider_compat.py
  └─__init__.py
```
