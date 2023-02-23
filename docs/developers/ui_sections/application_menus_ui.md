## Application menus
### Dependencies diagram (related `napari` modules)
```{mermaid}
graph LR
	napari._qt(napari._qt)
	napari._qt --> napari._qt.qt_main_window
	click napari._qt "https://github.com/napari/napari/tree/main/napari/_qt/__init__.py" _blank
	napari._qt.dialogs.preferences_dialog(napari._qt.dialogs.preferences_dialog)
	click napari._qt.dialogs.preferences_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/preferences_dialog.py" _blank
	napari._qt.dialogs.qt_about(napari._qt.dialogs.qt_about)
	click napari._qt.dialogs.qt_about "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_about.py" _blank
	napari._qt.dialogs.qt_plugin_dialog(napari._qt.dialogs.qt_plugin_dialog)
	napari._qt.dialogs.qt_plugin_dialog --> napari._qt.qt_resources
	napari._qt.dialogs.qt_plugin_dialog --> napari._qt.widgets
	click napari._qt.dialogs.qt_plugin_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_plugin_dialog.py" _blank
	napari._qt.dialogs.qt_plugin_report(napari._qt.dialogs.qt_plugin_report)
	click napari._qt.dialogs.qt_plugin_report "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_plugin_report.py" _blank
	napari._qt.dialogs.qt_reader_dialog(napari._qt.dialogs.qt_reader_dialog)
	click napari._qt.dialogs.qt_reader_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_reader_dialog.py" _blank
	napari._qt.dialogs.screenshot_dialog(napari._qt.dialogs.screenshot_dialog)
	click napari._qt.dialogs.screenshot_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/screenshot_dialog.py" _blank
	napari._qt.menus(napari._qt.menus)
	napari._qt.menus --> napari._qt.menus.debug_menu
	napari._qt.menus --> napari._qt.menus.file_menu
	napari._qt.menus --> napari._qt.menus.help_menu
	napari._qt.menus --> napari._qt.menus.plugins_menu
	napari._qt.menus --> napari._qt.menus.view_menu
	napari._qt.menus --> napari._qt.menus.window_menu
	click napari._qt.menus "https://github.com/napari/napari/tree/main/napari/_qt/menus/__init__.py" _blank
	napari._qt.menus._util(napari._qt.menus._util)
	click napari._qt.menus._util "https://github.com/napari/napari/tree/main/napari/_qt/menus/_util.py" _blank
	napari._qt.menus.debug_menu(napari._qt.menus.debug_menu)
	napari._qt.menus.debug_menu --> napari._qt.menus._util
	napari._qt.menus.debug_menu --> napari._qt.qt_main_window
	click napari._qt.menus.debug_menu "https://github.com/napari/napari/tree/main/napari/_qt/menus/debug_menu.py" _blank
	napari._qt.menus.file_menu(napari._qt.menus.file_menu)
	napari._qt.menus.file_menu --> napari._qt.dialogs.preferences_dialog
	napari._qt.menus.file_menu --> napari._qt.dialogs.qt_reader_dialog
	napari._qt.menus.file_menu --> napari._qt.dialogs.screenshot_dialog
	napari._qt.menus.file_menu --> napari._qt.menus._util
	napari._qt.menus.file_menu --> napari._qt.qt_main_window
	click napari._qt.menus.file_menu "https://github.com/napari/napari/tree/main/napari/_qt/menus/file_menu.py" _blank
	napari._qt.menus.help_menu(napari._qt.menus.help_menu)
	napari._qt.menus.help_menu --> napari._qt.dialogs.qt_about
	napari._qt.menus.help_menu --> napari._qt.menus._util
	napari._qt.menus.help_menu --> napari._qt.qt_main_window
	click napari._qt.menus.help_menu "https://github.com/napari/napari/tree/main/napari/_qt/menus/help_menu.py" _blank
	napari._qt.menus.plugins_menu(napari._qt.menus.plugins_menu)
	napari._qt.menus.plugins_menu --> napari._qt.dialogs.qt_plugin_dialog
	napari._qt.menus.plugins_menu --> napari._qt.dialogs.qt_plugin_report
	napari._qt.menus.plugins_menu --> napari._qt.menus._util
	napari._qt.menus.plugins_menu --> napari._qt.qt_main_window
	click napari._qt.menus.plugins_menu "https://github.com/napari/napari/tree/main/napari/_qt/menus/plugins_menu.py" _blank
	napari._qt.menus.view_menu(napari._qt.menus.view_menu)
	napari._qt.menus.view_menu --> napari._qt.menus._util
	napari._qt.menus.view_menu --> napari._qt.qt_main_window
	click napari._qt.menus.view_menu "https://github.com/napari/napari/tree/main/napari/_qt/menus/view_menu.py" _blank
	napari._qt.menus.window_menu(napari._qt.menus.window_menu)
	napari._qt.menus.window_menu --> napari._qt.menus._util
	napari._qt.menus.window_menu --> napari._qt.qt_main_window
	click napari._qt.menus.window_menu "https://github.com/napari/napari/tree/main/napari/_qt/menus/window_menu.py" _blank
	napari._qt.qt_main_window(napari._qt.qt_main_window)
	napari._qt.qt_main_window --> napari._qt.menus
	napari._qt.qt_main_window --> napari._qt.qt_resources
	napari._qt.qt_main_window --> napari._qt.widgets
	click napari._qt.qt_main_window "https://github.com/napari/napari/tree/main/napari/_qt/qt_main_window.py" _blank
	napari._qt.qt_resources(napari._qt.qt_resources)
	click napari._qt.qt_resources "https://github.com/napari/napari/tree/main/napari/_qt/qt_resources/__init__.py" _blank
	napari._qt.widgets(napari._qt.widgets)
	click napari._qt.widgets "https://github.com/napari/napari/tree/main/napari/_qt/widgets/__init__.py" _blank
	classDef default fill:#00c3ff,color:black;
	linkStyle default stroke:#00c3ff
	classDef external fill:#ffa600,color:black;
```
### Source code directory layout (related to modules inside `napari`)
```
napari/
└─_qt/
  ├─dialogs/
  │ ├─preferences_dialog.py
  │ ├─qt_about.py
  │ ├─qt_plugin_dialog.py
  │ ├─qt_plugin_report.py
  │ ├─qt_reader_dialog.py
  │ └─screenshot_dialog.py
  ├─menus/
  │ ├─debug_menu.py
  │ ├─file_menu.py
  │ ├─help_menu.py
  │ ├─plugins_menu.py
  │ ├─view_menu.py
  │ ├─window_menu.py
  │ ├─_util.py
  │ └─__init__.py
  ├─qt_main_window.py
  ├─qt_resources/
  │ └─__init__.py
  ├─widgets/
  │ └─__init__.py
  └─__init__.py
```
