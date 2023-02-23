## Viewer
### Dependencies diagram (related `napari` modules)
```{mermaid}
graph LR
	napari._qt(napari._qt)
	napari._qt --> napari._qt.qt_main_window
	click napari._qt "https://github.com/napari/napari/tree/main/napari/_qt/__init__.py" _blank
	napari._qt.containers(napari._qt.containers)
	click napari._qt.containers "https://github.com/napari/napari/tree/main/napari/_qt/containers/__init__.py" _blank
	napari._qt.dialogs.confirm_close_dialog(napari._qt.dialogs.confirm_close_dialog)
	click napari._qt.dialogs.confirm_close_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/confirm_close_dialog.py" _blank
	napari._qt.dialogs.qt_activity_dialog(napari._qt.dialogs.qt_activity_dialog)
	click napari._qt.dialogs.qt_activity_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_activity_dialog.py" _blank
	napari._qt.dialogs.qt_modal(napari._qt.dialogs.qt_modal)
	click napari._qt.dialogs.qt_modal "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_modal.py" _blank
	napari._qt.dialogs.qt_notification(napari._qt.dialogs.qt_notification)
	napari._qt.dialogs.qt_notification --> napari._qt.qt_main_window
	napari._qt.dialogs.qt_notification --> napari._qt.utils
	click napari._qt.dialogs.qt_notification "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_notification.py" _blank
	napari._qt.dialogs.qt_reader_dialog(napari._qt.dialogs.qt_reader_dialog)
	click napari._qt.dialogs.qt_reader_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_reader_dialog.py" _blank
	napari._qt.dialogs.screenshot_dialog(napari._qt.dialogs.screenshot_dialog)
	click napari._qt.dialogs.screenshot_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/screenshot_dialog.py" _blank
	napari._qt.layer_controls(napari._qt.layer_controls)
	click napari._qt.layer_controls "https://github.com/napari/napari/tree/main/napari/_qt/layer_controls/__init__.py" _blank
	napari._qt.qt_main_window(napari._qt.qt_main_window)
	napari._qt.qt_main_window --> napari._qt.dialogs.confirm_close_dialog
	napari._qt.qt_main_window --> napari._qt.dialogs.qt_activity_dialog
	napari._qt.qt_main_window --> napari._qt.dialogs.qt_notification
	napari._qt.qt_main_window --> napari._qt.qt_viewer
	napari._qt.qt_main_window --> napari._qt.utils
	napari._qt.qt_main_window --> napari._qt.widgets.qt_viewer_dock_widget
	click napari._qt.qt_main_window "https://github.com/napari/napari/tree/main/napari/_qt/qt_main_window.py" _blank
	napari._qt.qt_viewer(napari._qt.qt_viewer)
	napari._qt.qt_viewer --> napari._qt.containers
	napari._qt.qt_viewer --> napari._qt.dialogs.qt_reader_dialog
	napari._qt.qt_viewer --> napari._qt.dialogs.screenshot_dialog
	napari._qt.qt_viewer --> napari._qt.layer_controls
	napari._qt.qt_viewer --> napari._qt.utils
	napari._qt.qt_viewer --> napari._qt.widgets.qt_dims
	napari._qt.qt_viewer --> napari._qt.widgets.qt_viewer_buttons
	napari._qt.qt_viewer --> napari._qt.widgets.qt_viewer_dock_widget
	napari._qt.qt_viewer --> napari._qt.widgets.qt_welcome
	napari._qt.qt_viewer --> napari.components._interaction_box_mouse_bindings
	napari._qt.qt_viewer --> napari.components.camera
	napari._qt.qt_viewer --> napari.components.layerlist
	napari._qt.qt_viewer --> napari.layers
	click napari._qt.qt_viewer "https://github.com/napari/napari/tree/main/napari/_qt/qt_viewer.py" _blank
	napari._qt.qthreading(napari._qt.qthreading)
	napari._qt.qthreading --> napari.layers
	click napari._qt.qthreading "https://github.com/napari/napari/tree/main/napari/_qt/qthreading.py" _blank
	napari._qt.utils(napari._qt.utils)
	click napari._qt.utils "https://github.com/napari/napari/tree/main/napari/_qt/utils.py" _blank
	napari._qt.widgets.qt_dims(napari._qt.widgets.qt_dims)
	napari._qt.widgets.qt_dims --> napari._qt.widgets.qt_dims_slider
	napari._qt.widgets.qt_dims --> napari.components.dims
	click napari._qt.widgets.qt_dims "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_dims.py" _blank
	napari._qt.widgets.qt_dims_slider(napari._qt.widgets.qt_dims_slider)
	napari._qt.widgets.qt_dims_slider --> napari._qt.dialogs.qt_modal
	napari._qt.widgets.qt_dims_slider --> napari._qt.qthreading
	click napari._qt.widgets.qt_dims_slider "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_dims_slider.py" _blank
	napari._qt.widgets.qt_dims_sorter(napari._qt.widgets.qt_dims_sorter)
	napari._qt.widgets.qt_dims_sorter --> napari._qt.containers
	napari._qt.widgets.qt_dims_sorter --> napari._qt.widgets.qt_tooltip
	click napari._qt.widgets.qt_dims_sorter "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_dims_sorter.py" _blank
	napari._qt.widgets.qt_spinbox(napari._qt.widgets.qt_spinbox)
	click napari._qt.widgets.qt_spinbox "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_spinbox.py" _blank
	napari._qt.widgets.qt_tooltip(napari._qt.widgets.qt_tooltip)
	click napari._qt.widgets.qt_tooltip "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_tooltip.py" _blank
	napari._qt.widgets.qt_viewer_buttons(napari._qt.widgets.qt_viewer_buttons)
	napari._qt.widgets.qt_viewer_buttons --> napari._qt.dialogs.qt_modal
	napari._qt.widgets.qt_viewer_buttons --> napari._qt.widgets.qt_dims_sorter
	napari._qt.widgets.qt_viewer_buttons --> napari._qt.widgets.qt_spinbox
	napari._qt.widgets.qt_viewer_buttons --> napari._qt.widgets.qt_tooltip
	click napari._qt.widgets.qt_viewer_buttons "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_viewer_buttons.py" _blank
	napari._qt.widgets.qt_viewer_dock_widget(napari._qt.widgets.qt_viewer_dock_widget)
	napari._qt.widgets.qt_viewer_dock_widget --> napari._qt.qt_viewer
	napari._qt.widgets.qt_viewer_dock_widget --> napari._qt.utils
	click napari._qt.widgets.qt_viewer_dock_widget "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_viewer_dock_widget.py" _blank
	napari._qt.widgets.qt_welcome(napari._qt.widgets.qt_welcome)
	click napari._qt.widgets.qt_welcome "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_welcome.py" _blank
	napari.components._interaction_box_constants(napari.components._interaction_box_constants)
	click napari.components._interaction_box_constants "https://github.com/napari/napari/tree/main/napari/components/_interaction_box_constants.py" _blank
	napari.components._interaction_box_mouse_bindings(napari.components._interaction_box_mouse_bindings)
	napari.components._interaction_box_mouse_bindings --> napari.components._interaction_box_constants
	napari.components._interaction_box_mouse_bindings --> napari.layers
	click napari.components._interaction_box_mouse_bindings "https://github.com/napari/napari/tree/main/napari/components/_interaction_box_mouse_bindings.py" _blank
	napari.components._viewer_key_bindings(napari.components._viewer_key_bindings)
	napari.components._viewer_key_bindings --> napari.components.viewer_model
	click napari.components._viewer_key_bindings "https://github.com/napari/napari/tree/main/napari/components/_viewer_key_bindings.py" _blank
	napari.components.camera(napari.components.camera)
	click napari.components.camera "https://github.com/napari/napari/tree/main/napari/components/camera.py" _blank
	napari.components.dims(napari.components.dims)
	click napari.components.dims "https://github.com/napari/napari/tree/main/napari/components/dims.py" _blank
	napari.components.layerlist(napari.components.layerlist)
	napari.components.layerlist --> napari.layers
	click napari.components.layerlist "https://github.com/napari/napari/tree/main/napari/components/layerlist.py" _blank
	napari.components.viewer_model(napari.components.viewer_model)
	napari.components.viewer_model --> napari.components.camera
	napari.components.viewer_model --> napari.components.dims
	napari.components.viewer_model --> napari.components.layerlist
	napari.components.viewer_model --> napari.layers
	click napari.components.viewer_model "https://github.com/napari/napari/tree/main/napari/components/viewer_model.py" _blank
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
│ ├─camera.py
│ ├─dims.py
│ ├─layerlist.py
│ ├─viewer_model.py
│ ├─_interaction_box_constants.py
│ ├─_interaction_box_mouse_bindings.py
│ └─_viewer_key_bindings.py
├─layers/
│ └─__init__.py
└─_qt/
  ├─containers/
  │ └─__init__.py
  ├─dialogs/
  │ ├─confirm_close_dialog.py
  │ ├─qt_activity_dialog.py
  │ ├─qt_modal.py
  │ ├─qt_notification.py
  │ ├─qt_reader_dialog.py
  │ └─screenshot_dialog.py
  ├─layer_controls/
  │ └─__init__.py
  ├─qthreading.py
  ├─qt_main_window.py
  ├─qt_viewer.py
  ├─utils.py
  ├─widgets/
  │ ├─qt_dims.py
  │ ├─qt_dims_slider.py
  │ ├─qt_dims_sorter.py
  │ ├─qt_spinbox.py
  │ ├─qt_tooltip.py
  │ ├─qt_viewer_buttons.py
  │ ├─qt_viewer_dock_widget.py
  │ └─qt_welcome.py
  └─__init__.py
```
