## Console (napari-console)
### Dependencies diagram (related `napari` modules)
```{mermaid}
graph LR
	napari._qt(napari._qt)
	napari._qt --> napari._qt.qt_main_window
	click napari._qt "https://github.com/napari/napari/tree/main/napari/_qt/__init__.py" _blank
	napari._qt.qt_main_window(napari._qt.qt_main_window)
	napari._qt.qt_main_window --> napari._qt.qt_viewer
	napari._qt.qt_main_window --> napari.settings
	click napari._qt.qt_main_window "https://github.com/napari/napari/tree/main/napari/_qt/qt_main_window.py" _blank
	napari._qt.qt_viewer(napari._qt.qt_viewer)
	napari._qt.qt_viewer --> napari._qt.widgets.qt_viewer_buttons
	napari._qt.qt_viewer --> napari.settings
	napari._qt.qt_viewer --> napari_console
	click napari._qt.qt_viewer "https://github.com/napari/napari/tree/main/napari/_qt/qt_viewer.py" _blank
	napari._qt.widgets.qt_tooltip(napari._qt.widgets.qt_tooltip)
	click napari._qt.widgets.qt_tooltip "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_tooltip.py" _blank
	napari._qt.widgets.qt_viewer_buttons(napari._qt.widgets.qt_viewer_buttons)
	napari._qt.widgets.qt_viewer_buttons --> napari._qt.widgets.qt_tooltip
	click napari._qt.widgets.qt_viewer_buttons "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_viewer_buttons.py" _blank
	napari.qt(napari.qt)
	napari.qt --> napari._qt
	napari.qt --> napari._qt.qt_main_window
	napari.qt --> napari._qt.qt_viewer
	napari.qt --> napari._qt.widgets.qt_tooltip
	napari.qt --> napari._qt.widgets.qt_viewer_buttons
	click napari.qt "https://github.com/napari/napari/tree/main/napari/qt/__init__.py" _blank
	napari.settings(napari.settings)
	click napari.settings "https://github.com/napari/napari/tree/main/napari/settings/__init__.py" _blank
	napari_console(napari_console)
	napari_console --> napari_console.qt_console
	napari_console.qt_console(napari_console.qt_console)
	napari_console.qt_console --> napari.qt
	classDef default fill:#00c3ff,color:black;
	linkStyle default stroke:#00c3ff
	classDef external fill:#ffa600,color:black;
	class napari_console external
	class napari_console.qt_console external
```
### Source code directory layout (related to modules inside `napari`)
```
napari/
├─qt/
│ └─__init__.py
├─settings/
│ └─__init__.py
└─_qt/
  ├─qt_main_window.py
  ├─qt_viewer.py
  ├─widgets/
  │ ├─qt_tooltip.py
  │ └─qt_viewer_buttons.py
  └─__init__.py
```
