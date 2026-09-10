### A Zoom with a View 🔍

Pardon the play on words, but you can now zoom directly to a region of interest in the viewer by holding `Alt` and dragging with the mouse [(#8004)](https://github.com/napari/napari/pull/8004). The camera will pan and zoom to fit the selected region, making it much easier to focus on specific areas of your data. This feature works in both 2D and 3D views.

![GIF Displaying Alt-Drag Zoom Box Behavior](https://github.com/user-attachments/assets/f32ea020-28e2-4059-90b9-491bdd4a962b)

### Fine Tuning Thick Slicing from the GUI 📏

Thick slicing controls are now available in the GUI [(#6146)](https://github.com/napari/napari/pull/6146)! This allows you to project multiple slices together using different modes (sum, mean, max, and min) for better visualization of your multidimensional data. You can access the thickness controls by right-clicking on the dimension sliders to open a popup to change the margins either symmetrically or asymmetrical and projection mode settings are now available per layer in the layer controls widget.

![GIF Displaying Thick Slicing GUI Controls](https://github.com/user-attachments/assets/f61636d6-8540-4c33-9abc-1e065c5f9d38)

### Run Scripts by Dragging and Dropping into the Viewer 🖱️

Scripts can now be run by dragging and dropping them into the viewer [(#8135)](https://github.com/napari/napari/pull/8135)! This is particularly useful for running [napari examples](https://napari.org/stable/gallery.html#gallery) without having to use the command line; you can even run these scripts from the bundled install! This works by adding a `.py` reader to napari's builtins.

![Image Depicting a User dragging a script into the viewer](https://github.com/user-attachments/assets/af4edaa3-fd77-4697-85ea-4f2eb662f5ec)

### Windows: Access ~~Denied~~ Fixed 🪟

A critical Windows-specific bug that caused Access Violation errors has been resolved [(#8122)](https://github.com/napari/napari/pull/8122)! This longstanding issue would cause napari to stop displaying layers due to various events and often occurred at seemingly non-reproducible times, and required a full restart of napari. The fix ensures proper cleanup and syncing of GPU resources, also reducing memory usage on all platforms. If you were an effected user, you may recall it as `Access Violation`, `0x000000000000001C` if triggered without a plugin, or `0x000000000000034C` if triggered with a plugin.

### Improved PySide6 Support 🛠️

Napari now has improved support for PySide6 [(#7887)](https://github.com/napari/napari/pull/7887). We encourage plugin developers to test against PySide6, as a fully supported backend going forward. Additionally, this change will enable us to drop PySide2 along side Python 3.10, in the near future. If you are a plugin developer or otherwise depend on napari and PySide2, please reach out on Zulip or Github.
