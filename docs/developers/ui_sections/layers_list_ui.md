## Layers list
### Dependencies diagram (related `napari` modules)
```{mermaid}
graph LR
	napari._qt(napari._qt)
	napari._qt --> napari._qt.qt_main_window
	click napari._qt "https://github.com/napari/napari/tree/main/napari/_qt/__init__.py" _blank
	napari._qt._qapp_model(napari._qt._qapp_model)
	napari._qt._qapp_model --> napari._qt._qapp_model._menus
	click napari._qt._qapp_model "https://github.com/napari/napari/tree/main/napari/_qt/_qapp_model/__init__.py" _blank
	napari._qt._qapp_model._menus(napari._qt._qapp_model._menus)
	click napari._qt._qapp_model._menus "https://github.com/napari/napari/tree/main/napari/_qt/_qapp_model/_menus.py" _blank
	napari._qt.containers(napari._qt.containers)
	napari._qt.containers --> napari._qt.containers._factory
	napari._qt.containers --> napari._qt.containers.qt_layer_list
	napari._qt.containers --> napari._qt.containers.qt_layer_model
	napari._qt.containers --> napari._qt.containers.qt_list_model
	napari._qt.containers --> napari._qt.containers.qt_list_view
	click napari._qt.containers "https://github.com/napari/napari/tree/main/napari/_qt/containers/__init__.py" _blank
	napari._qt.containers._base_item_model(napari._qt.containers._base_item_model)
	click napari._qt.containers._base_item_model "https://github.com/napari/napari/tree/main/napari/_qt/containers/_base_item_model.py" _blank
	napari._qt.containers._base_item_view(napari._qt.containers._base_item_view)
	napari._qt.containers._base_item_view --> napari._qt.containers._base_item_model
	napari._qt.containers._base_item_view --> napari._qt.containers._factory
	click napari._qt.containers._base_item_view "https://github.com/napari/napari/tree/main/napari/_qt/containers/_base_item_view.py" _blank
	napari._qt.containers._factory(napari._qt.containers._factory)
	napari._qt.containers._factory --> napari.components
	napari._qt.containers._factory --> napari.components.layerlist
	click napari._qt.containers._factory "https://github.com/napari/napari/tree/main/napari/_qt/containers/_factory.py" _blank
	napari._qt.containers._layer_delegate(napari._qt.containers._layer_delegate)
	napari._qt.containers._layer_delegate --> napari._qt._qapp_model
	napari._qt.containers._layer_delegate --> napari._qt.containers._base_item_model
	napari._qt.containers._layer_delegate --> napari._qt.containers.qt_layer_model
	napari._qt.containers._layer_delegate --> napari._qt.qt_resources
	napari._qt.containers._layer_delegate --> napari.components
	napari._qt.containers._layer_delegate --> napari.components.layerlist
	click napari._qt.containers._layer_delegate "https://github.com/napari/napari/tree/main/napari/_qt/containers/_layer_delegate.py" _blank
	napari._qt.containers.qt_layer_list(napari._qt.containers.qt_layer_list)
	napari._qt.containers.qt_layer_list --> napari._qt.containers._base_item_model
	napari._qt.containers.qt_layer_list --> napari._qt.containers._layer_delegate
	napari._qt.containers.qt_layer_list --> napari._qt.containers.qt_list_view
	napari._qt.containers.qt_layer_list --> napari.components
	napari._qt.containers.qt_layer_list --> napari.components.layerlist
	napari._qt.containers.qt_layer_list --> napari.layers
	click napari._qt.containers.qt_layer_list "https://github.com/napari/napari/tree/main/napari/_qt/containers/qt_layer_list.py" _blank
	napari._qt.containers.qt_layer_model(napari._qt.containers.qt_layer_model)
	napari._qt.containers.qt_layer_model --> napari._qt.containers.qt_list_model
	napari._qt.containers.qt_layer_model --> napari.layers
	click napari._qt.containers.qt_layer_model "https://github.com/napari/napari/tree/main/napari/_qt/containers/qt_layer_model.py" _blank
	napari._qt.containers.qt_list_model(napari._qt.containers.qt_list_model)
	napari._qt.containers.qt_list_model --> napari._qt.containers._base_item_model
	click napari._qt.containers.qt_list_model "https://github.com/napari/napari/tree/main/napari/_qt/containers/qt_list_model.py" _blank
	napari._qt.containers.qt_list_view(napari._qt.containers.qt_list_view)
	napari._qt.containers.qt_list_view --> napari._qt.containers._base_item_view
	napari._qt.containers.qt_list_view --> napari._qt.containers.qt_list_model
	click napari._qt.containers.qt_list_view "https://github.com/napari/napari/tree/main/napari/_qt/containers/qt_list_view.py" _blank
	napari._qt.qt_main_window(napari._qt.qt_main_window)
	napari._qt.qt_main_window --> napari._qt.qt_resources
	napari._qt.qt_main_window --> napari._qt.qt_viewer
	napari._qt.qt_main_window --> napari._qt.utils
	napari._qt.qt_main_window --> napari._qt.widgets.qt_viewer_dock_widget
	click napari._qt.qt_main_window "https://github.com/napari/napari/tree/main/napari/_qt/qt_main_window.py" _blank
	napari._qt.qt_resources(napari._qt.qt_resources)
	napari._qt.qt_resources --> napari._qt.qt_resources._svg
	click napari._qt.qt_resources "https://github.com/napari/napari/tree/main/napari/_qt/qt_resources/__init__.py" _blank
	napari._qt.qt_resources._svg(napari._qt.qt_resources._svg)
	click napari._qt.qt_resources._svg "https://github.com/napari/napari/tree/main/napari/_qt/qt_resources/_svg.py" _blank
	napari._qt.qt_viewer(napari._qt.qt_viewer)
	napari._qt.qt_viewer --> napari._qt.containers
	napari._qt.qt_viewer --> napari._qt.utils
	napari._qt.qt_viewer --> napari._qt.widgets.qt_viewer_buttons
	napari._qt.qt_viewer --> napari._qt.widgets.qt_viewer_dock_widget
	napari._qt.qt_viewer --> napari.components
	napari._qt.qt_viewer --> napari.components._interaction_box_mouse_bindings
	napari._qt.qt_viewer --> napari.components.layerlist
	napari._qt.qt_viewer --> napari.layers
	click napari._qt.qt_viewer "https://github.com/napari/napari/tree/main/napari/_qt/qt_viewer.py" _blank
	napari._qt.utils(napari._qt.utils)
	click napari._qt.utils "https://github.com/napari/napari/tree/main/napari/_qt/utils.py" _blank
	napari._qt.widgets.qt_viewer_buttons(napari._qt.widgets.qt_viewer_buttons)
	click napari._qt.widgets.qt_viewer_buttons "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_viewer_buttons.py" _blank
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
	napari.components.axes(napari.components.axes)
	click napari.components.axes "https://github.com/napari/napari/tree/main/napari/components/axes.py" _blank
	napari.components.layerlist(napari.components.layerlist)
	napari.components.layerlist --> napari.layers
	click napari.components.layerlist "https://github.com/napari/napari/tree/main/napari/components/layerlist.py" _blank
	napari.components.scale_bar(napari.components.scale_bar)
	click napari.components.scale_bar "https://github.com/napari/napari/tree/main/napari/components/scale_bar.py" _blank
	napari.components.text_overlay(napari.components.text_overlay)
	click napari.components.text_overlay "https://github.com/napari/napari/tree/main/napari/components/text_overlay.py" _blank
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
│ ├─axes.py
│ ├─layerlist.py
│ ├─scale_bar.py
│ ├─text_overlay.py
│ ├─_interaction_box_mouse_bindings.py
│ └─__init__.py
├─layers/
│ └─__init__.py
└─_qt/
  ├─containers/
  │ ├─qt_layer_list.py
  │ ├─qt_layer_model.py
  │ ├─qt_list_model.py
  │ ├─qt_list_view.py
  │ ├─_base_item_model.py
  │ ├─_base_item_view.py
  │ ├─_factory.py
  │ ├─_layer_delegate.py
  │ └─__init__.py
  ├─qt_main_window.py
  ├─qt_resources/
  │ ├─_svg.py
  │ └─__init__.py
  ├─qt_viewer.py
  ├─utils.py
  ├─widgets/
  │ ├─qt_viewer_buttons.py
  │ └─qt_viewer_dock_widget.py
  ├─_qapp_model/
  │ ├─_menus.py
  │ └─__init__.py
  └─__init__.py
```
