# napari 0.3.6

We're happy to announce the release of napari 0.3.6!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).


For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## Highlights
This release contains the long awaited addition of text to both the points and
shapes layers ({pr}`1374`). Checkout our `examples/*_with_text.py` for simple usage
and this [segmentation annotation tutorial](https://napari.org/tutorials/segmentation/annotate_segmentation)
for a more real-world use case.

We've added support for a circular paintbrush for easier labels painting,
and moved more of our contrast limits and gamma setting to the GPU for faster
rendering and interactivity with 3D rendered datasets. As always this release
contains various bug fixes and other improvements, including some automated
reformatting and fixes to our docstrings.

This release also contains a number of contributions from new authors thanks
to the SciPy conference sprints. We’re delighted to welcome new contributors to
the codebase. If you want help contributing to napari, reach out to us on our chat
room at https://napari.zulipchat.com!


## New Features
- Functions to split/combine multiple layers along an axis ({pr}`1322`)
- Add text to shapes and points via TextManager ({pr}`1374`)
- Add circle/spherical brush to Labels paint brush ({pr}`1429`)


## Improvements
- Add ability to run napari script with/without gui_qt from CLI ({pr}`1373`)
- Event handler refactor for image layer  "reverted by (#1416)" ({pr}`1376`)
- Add ndim as a keyword argument to shapes to support creating empty layers ({pr}`1379`)
- Add helpful error on multichannel IndexError ({pr}`1381`)
- Use qlistwidget for QtLayerList "reverted by (#1416)" ({pr}`1391`)
- Event handler surface layer  "reverted by (#1416)" ({pr}`1396`)
- Revert "event handler refactors (#1376), (#1391), (#1396)" ({pr}`1416`)
- Move contrast limits and gamma to the shader by vendoring vispy code ({pr}`1456`)
- Reduce attenuation default and range ({pr}`1460`)


## Bug Fixes
- Revert "remove scipy.stats import (#1250)" ({pr}`1371`)
- Fix vispy volume colormap changing ({pr}`1402`)
- Fix vertical alignment of QLabel in QtDimSliderWidget ({pr}`1415`)
- Fix adding single shape duplicating properties ({pr}`1427`)
- Fix viewing properties for multiscale labels layers ({pr}`1433`)
- Fix trim of layer number ({pr}`1439`)
- Hide status bar line on windows ({pr}`1440`)
- Handle nested zarr path ({pr}`1441`)
- Toggle image/ volume nodes on ndisplay change ({pr}`1445`)
- Fix attenuation setting ({pr}`1454`)
- Fix toggle ndisplay z-order points ({pr}`1463`)
- Fix edge color select bug ({pr}`1464`)
- Proper recognition tiff files with ".TIF" extension ({pr}`1472`)


## Build Tools
- Updates plugin dev docs to encourage github topic ({pr}`1366`)
- Refactor all tests to hide GUI ({pr}`1372`)
- Fix two remaining tests that try to show the viewer. ({pr}`1375`)
- Fix windows tests ({pr}`1377`)
- Dedicated testing doc ({pr}`1378`)
- Rename mark to avoid warning on pytest ordering package ({pr}`1383`)
- Rename viewer_factory -> make_test_viewer, don't return view ({pr}`1386`)
- Fix inconsistency in docs ({pr}`1420`)
- Docreformat ({pr}`1428`)
- DOC: autoreformat of more docstrings. ({pr}`1437`)
- Fix typos using codespell ({pr}`1438`)
- Preserve tests from EVH revert ({pr}`1452`)
- Fix typos ({pr}`1468`)
- DOC: minor doc reformatting. ({pr}`1469`)
- DOC: update param names to match function signature. ({pr}`1479`)
- Fix events docstring type ({pr}`1481`)
- Don't look for release notes in pre-releases ({pr}`1483`)


## 14 authors added to this release (alphabetical)

- [Cameron Lloyd](https://github.com/napari/napari/commits?author=camlloyd) - @camlloyd
- [Chris Wood](https://github.com/napari/napari/commits?author=cwood1967) - @cwood1967
- [Draga Doncila](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Forrest Li](https://github.com/napari/napari/commits?author=floryst) - @floryst
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Hector Munoz](https://github.com/napari/napari/commits?author=hectormz) - @hectormz
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Justin Kiggins](https://github.com/napari/napari/commits?author=neuromusic) - @neuromusic
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Trevor Manz](https://github.com/napari/napari/commits?author=manzt) - @manzt
- [Ziyang Liu](https://github.com/napari/napari/commits?author=ziyangczi) - @ziyangczi


## 12 reviewers added to this release (alphabetical)

- [Chris Wood](https://github.com/napari/napari/commits?author=cwood1967) - @cwood1967
- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Hector Munoz](https://github.com/napari/napari/commits?author=hectormz) - @hectormz
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Justin Kiggins](https://github.com/napari/napari/commits?author=neuromusic) - @neuromusic
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Trevor Manz](https://github.com/napari/napari/commits?author=manzt) - @manzt
- [Ziyang Liu](https://github.com/napari/napari/commits?author=ziyangczi) - @ziyangczi
