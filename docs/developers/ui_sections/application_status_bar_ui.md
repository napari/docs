## Application status bar
### Dependencies diagram (related `napari` modules)
```{mermaid}
graph LR
	napari._qt(napari._qt)
	napari._qt --> napari._qt.qt_main_window
	click napari._qt "https://github.com/napari/napari/tree/main/napari/_qt/__init__.py" _blank
	napari._qt.dialogs.qt_activity_dialog(napari._qt.dialogs.qt_activity_dialog)
	napari._qt.dialogs.qt_activity_dialog --> napari._qt.widgets.qt_progress_bar
	napari._qt.dialogs.qt_activity_dialog --> napari.utils.progress
	click napari._qt.dialogs.qt_activity_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_activity_dialog.py" _blank
	napari._qt.qt_main_window(napari._qt.qt_main_window)
	napari._qt.qt_main_window --> napari._qt.dialogs.qt_activity_dialog
	napari._qt.qt_main_window --> napari._qt.widgets.qt_viewer_status_bar
	click napari._qt.qt_main_window "https://github.com/napari/napari/tree/main/napari/_qt/qt_main_window.py" _blank
	napari._qt.widgets.qt_progress_bar(napari._qt.widgets.qt_progress_bar)
	napari._qt.widgets.qt_progress_bar --> napari.utils.progress
	click napari._qt.widgets.qt_progress_bar "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_progress_bar.py" _blank
	napari._qt.widgets.qt_viewer_status_bar(napari._qt.widgets.qt_viewer_status_bar)
	napari._qt.widgets.qt_viewer_status_bar --> napari._qt.dialogs.qt_activity_dialog
	napari._qt.widgets.qt_viewer_status_bar --> napari._qt.qt_main_window
	click napari._qt.widgets.qt_viewer_status_bar "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_viewer_status_bar.py" _blank
	napari.utils.progress(napari.utils.progress)
	click napari.utils.progress "https://github.com/napari/napari/tree/main/napari/utils/progress.py" _blank
	classDef default fill:#00c3ff,color:black;
	linkStyle default stroke:#00c3ff
	classDef external fill:#ffa600,color:black;
```
### Source code directory layout (related to modules inside `napari`)
```
napari/
├─utils/
│ └─progress.py
└─_qt/
  ├─dialogs/
  │ └─qt_activity_dialog.py
  ├─qt_main_window.py
  ├─widgets/
  │ ├─qt_progress_bar.py
  │ └─qt_viewer_status_bar.py
  └─__init__.py
```
