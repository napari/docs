## Dialogs
### Dependencies diagram (related `napari` modules)
```{mermaid}
graph LR
	napari._qt(napari._qt)
	napari._qt --> napari._qt.qt_main_window
	click napari._qt "https://github.com/napari/napari/tree/main/napari/_qt/__init__.py" _blank
	napari._qt.code_syntax_highlight(napari._qt.code_syntax_highlight)
	click napari._qt.code_syntax_highlight "https://github.com/napari/napari/tree/main/napari/_qt/code_syntax_highlight.py" _blank
	napari._qt.dialogs.confirm_close_dialog(napari._qt.dialogs.confirm_close_dialog)
	click napari._qt.dialogs.confirm_close_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/confirm_close_dialog.py" _blank
	napari._qt.dialogs.preferences_dialog(napari._qt.dialogs.preferences_dialog)
	click napari._qt.dialogs.preferences_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/preferences_dialog.py" _blank
	napari._qt.dialogs.qt_about(napari._qt.dialogs.qt_about)
	click napari._qt.dialogs.qt_about "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_about.py" _blank
	napari._qt.dialogs.qt_activity_dialog(napari._qt.dialogs.qt_activity_dialog)
	napari._qt.dialogs.qt_activity_dialog --> napari._qt.widgets.qt_progress_bar
	click napari._qt.dialogs.qt_activity_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_activity_dialog.py" _blank
	napari._qt.dialogs.qt_modal(napari._qt.dialogs.qt_modal)
	click napari._qt.dialogs.qt_modal "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_modal.py" _blank
	napari._qt.dialogs.qt_notification(napari._qt.dialogs.qt_notification)
	napari._qt.dialogs.qt_notification --> napari._qt.code_syntax_highlight
	napari._qt.dialogs.qt_notification --> napari._qt.qt_main_window
	napari._qt.dialogs.qt_notification --> napari._qt.qt_resources
	click napari._qt.dialogs.qt_notification "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_notification.py" _blank
	napari._qt.dialogs.qt_plugin_dialog(napari._qt.dialogs.qt_plugin_dialog)
	napari._qt.dialogs.qt_plugin_dialog --> napari._qt.qt_resources
	napari._qt.dialogs.qt_plugin_dialog --> napari._qt.qthreading
	napari._qt.dialogs.qt_plugin_dialog --> napari._qt.widgets.qt_tooltip
	click napari._qt.dialogs.qt_plugin_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_plugin_dialog.py" _blank
	napari._qt.dialogs.qt_plugin_report(napari._qt.dialogs.qt_plugin_report)
	napari._qt.dialogs.qt_plugin_report --> napari._qt.code_syntax_highlight
	click napari._qt.dialogs.qt_plugin_report "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_plugin_report.py" _blank
	napari._qt.dialogs.qt_reader_dialog(napari._qt.dialogs.qt_reader_dialog)
	click napari._qt.dialogs.qt_reader_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/qt_reader_dialog.py" _blank
	napari._qt.dialogs.screenshot_dialog(napari._qt.dialogs.screenshot_dialog)
	click napari._qt.dialogs.screenshot_dialog "https://github.com/napari/napari/tree/main/napari/_qt/dialogs/screenshot_dialog.py" _blank
	napari._qt.menus(napari._qt.menus)
	napari._qt.menus --> napari._qt.menus.file_menu
	napari._qt.menus --> napari._qt.menus.help_menu
	napari._qt.menus --> napari._qt.menus.plugins_menu
	napari._qt.menus --> napari._qt.menus.view_menu
	click napari._qt.menus "https://github.com/napari/napari/tree/main/napari/_qt/menus/__init__.py" _blank
	napari._qt.menus.file_menu(napari._qt.menus.file_menu)
	napari._qt.menus.file_menu --> napari._qt.dialogs.preferences_dialog
	napari._qt.menus.file_menu --> napari._qt.dialogs.qt_reader_dialog
	napari._qt.menus.file_menu --> napari._qt.dialogs.screenshot_dialog
	napari._qt.menus.file_menu --> napari._qt.qt_main_window
	click napari._qt.menus.file_menu "https://github.com/napari/napari/tree/main/napari/_qt/menus/file_menu.py" _blank
	napari._qt.menus.help_menu(napari._qt.menus.help_menu)
	napari._qt.menus.help_menu --> napari._qt.dialogs.qt_about
	napari._qt.menus.help_menu --> napari._qt.qt_main_window
	click napari._qt.menus.help_menu "https://github.com/napari/napari/tree/main/napari/_qt/menus/help_menu.py" _blank
	napari._qt.menus.plugins_menu(napari._qt.menus.plugins_menu)
	napari._qt.menus.plugins_menu --> napari._qt.dialogs.qt_plugin_dialog
	napari._qt.menus.plugins_menu --> napari._qt.dialogs.qt_plugin_report
	napari._qt.menus.plugins_menu --> napari._qt.qt_main_window
	click napari._qt.menus.plugins_menu "https://github.com/napari/napari/tree/main/napari/_qt/menus/plugins_menu.py" _blank
	napari._qt.menus.view_menu(napari._qt.menus.view_menu)
	napari._qt.menus.view_menu --> napari._qt.qt_main_window
	click napari._qt.menus.view_menu "https://github.com/napari/napari/tree/main/napari/_qt/menus/view_menu.py" _blank
	napari._qt.qt_main_window(napari._qt.qt_main_window)
	napari._qt.qt_main_window --> napari._qt.dialogs.confirm_close_dialog
	napari._qt.qt_main_window --> napari._qt.dialogs.qt_activity_dialog
	napari._qt.qt_main_window --> napari._qt.dialogs.qt_notification
	napari._qt.qt_main_window --> napari._qt.menus
	napari._qt.qt_main_window --> napari._qt.qt_resources
	napari._qt.qt_main_window --> napari._qt.qt_viewer
	napari._qt.qt_main_window --> napari._qt.widgets.qt_viewer_status_bar
	click napari._qt.qt_main_window "https://github.com/napari/napari/tree/main/napari/_qt/qt_main_window.py" _blank
	napari._qt.qt_resources(napari._qt.qt_resources)
	napari._qt.qt_resources --> napari._qt.qt_resources._svg
	click napari._qt.qt_resources "https://github.com/napari/napari/tree/main/napari/_qt/qt_resources/__init__.py" _blank
	napari._qt.qt_resources._svg(napari._qt.qt_resources._svg)
	click napari._qt.qt_resources._svg "https://github.com/napari/napari/tree/main/napari/_qt/qt_resources/_svg.py" _blank
	napari._qt.qt_viewer(napari._qt.qt_viewer)
	napari._qt.qt_viewer --> napari._qt.dialogs.qt_reader_dialog
	napari._qt.qt_viewer --> napari._qt.dialogs.screenshot_dialog
	click napari._qt.qt_viewer "https://github.com/napari/napari/tree/main/napari/_qt/qt_viewer.py" _blank
	napari._qt.qthreading(napari._qt.qthreading)
	click napari._qt.qthreading "https://github.com/napari/napari/tree/main/napari/_qt/qthreading.py" _blank
	napari._qt.widgets.qt_dims_slider(napari._qt.widgets.qt_dims_slider)
	napari._qt.widgets.qt_dims_slider --> napari._qt.dialogs.qt_modal
	napari._qt.widgets.qt_dims_slider --> napari._qt.qthreading
	click napari._qt.widgets.qt_dims_slider "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_dims_slider.py" _blank
	napari._qt.widgets.qt_progress_bar(napari._qt.widgets.qt_progress_bar)
	click napari._qt.widgets.qt_progress_bar "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_progress_bar.py" _blank
	napari._qt.widgets.qt_tooltip(napari._qt.widgets.qt_tooltip)
	click napari._qt.widgets.qt_tooltip "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_tooltip.py" _blank
	napari._qt.widgets.qt_viewer_status_bar(napari._qt.widgets.qt_viewer_status_bar)
	napari._qt.widgets.qt_viewer_status_bar --> napari._qt.dialogs.qt_activity_dialog
	napari._qt.widgets.qt_viewer_status_bar --> napari._qt.qt_main_window
	click napari._qt.widgets.qt_viewer_status_bar "https://github.com/napari/napari/tree/main/napari/_qt/widgets/qt_viewer_status_bar.py" _blank
	classDef default fill:#00c3ff,color:black;
	linkStyle default stroke:#00c3ff
	classDef external fill:#ffa600,color:black;
```
### Source code directory layout (related to modules inside `napari`)
```
napari/
└─_qt/
  ├─code_syntax_highlight.py
  ├─dialogs/
  │ ├─confirm_close_dialog.py
  │ ├─preferences_dialog.py
  │ ├─qt_about.py
  │ ├─qt_activity_dialog.py
  │ ├─qt_modal.py
  │ ├─qt_notification.py
  │ ├─qt_plugin_dialog.py
  │ ├─qt_plugin_report.py
  │ ├─qt_reader_dialog.py
  │ └─screenshot_dialog.py
  ├─menus/
  │ ├─file_menu.py
  │ ├─help_menu.py
  │ ├─plugins_menu.py
  │ ├─view_menu.py
  │ └─__init__.py
  ├─qthreading.py
  ├─qt_main_window.py
  ├─qt_resources/
  │ ├─_svg.py
  │ └─__init__.py
  ├─qt_viewer.py
  ├─widgets/
  │ ├─qt_dims_slider.py
  │ ├─qt_progress_bar.py
  │ ├─qt_tooltip.py
  │ └─qt_viewer_status_bar.py
  └─__init__.py
```
