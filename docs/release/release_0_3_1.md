# napari 0.3.1

We're happy to announce the release of napari 0.3.1!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).

This is a bug fix release to address issues that snuck through into 0.3.0.

For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari


## Improvements
- CLI accepts --plugin or any add_* kwargs ({pr}`1220`)
- Specify viewer.open(plugins='builtins') for all tests ({pr}`1222`)
- Unify user/plugin kwargs.  Use filename for layer name ({pr}`1232`)

## Bug Fixes
- rework dask cache ({pr}`1206`)
- Use grayscale when n_channels=1 ({pr}`1217`)
- Better error on magic_imread with no files ({pr}`1218`)
- Improve plugin error messages, bump napari-plugin-engine ({pr}`1219`)
- make skimage data fixtures compatible with 0.17.0 ({pr}`1223`)
- Better icon-building strategy ({pr}`1229`)
- Unpin Jupyter client, issue seems to have resolved ({pr}`1240`)
- Don't try to get an event.key name if there is no event.key ({pr}`1241`)
- Update guess_multiscale to deal with strange inputs ({pr}`1244`)


## Support
- Don't build wheels with releases ({pr}`1215`)
- Update github issues templates with links to image.sc and zulip  ({pr}`1234`)
- add new performance doc in new "explanations" directory ({pr}`1239`)


## 3 authors added to this release (alphabetical)

- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Philip Winston](https://github.com/napari/napari/commits?author=pwinston) - @pwinston
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03


## 5 reviewers added to this release (alphabetical)

- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Philip Winston](https://github.com/napari/napari/commits?author=pwinston) - @pwinston
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
