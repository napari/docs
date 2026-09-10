### Run scripts with napari from the command line

As a follow-up to the ability to drag-n-drop scripts into the napari window from 0.6.3, you can now run scripts directly from the command line using the `napari` command and the path to the script ([#8185](https://github.com/napari/napari/pull/8185) and [#8187](https://github.com/napari/napari/pull/8187)).
`napari examples/magic_immage_arithmetic.py` will open a local napari and run the local script.
You can also run scripts from a remote location ([#8208](https://github.com/napari/napari/pull/8208)), including Github, Gist, Gitlab, and the napari gallery.
For example, you can run `napari https://github.com/napari/napari/blob/main/examples/grid_mode.py`.
If you have `uv` you can even run a script without installing napari by using `uvx --with "napari[gallery,all]" napari https://napari.org/stable/_downloads/55f878f7d41dc4c7c2e28483653273cb/affine_coffee_cup.py`, serving as a clever way to trial napari or share your script. As always with remote connections, only use this feature with scripts you trust.

### Toggling the napari console now places focus on the console

Toggling the napari console (with the keyboard (`Cmd/Ctrl+Shift+C`), GUI, or command pallete) will now transfer focus on the console, allowing you to immediately start typing commands without needing to click into the console first ([#8182](https://github.com/napari/napari/pull/8182)). We have found this to be a very useful feature for a keyboard-centric workflow combining the power of the command palette and console together.
