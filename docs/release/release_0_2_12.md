# napari 0.2.12

We're happy to announce the release of napari 0.2.12! napari is a fast,
interactive, multi-dimensional image viewer for Python. It's designed for
browsing, annotating, and analyzing large multi-dimensional images. It's built
on top of Qt (for the GUI), vispy (for performant GPU-based rendering), and the
scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## New Features

- Add clickable color swatch with QColorDialog ({pr}`832`)
- Implement pluggy as plugin manager ({pr}`908`)
- Allow toggle theme from GUI ({pr}`943`)
- Add "Screenshot" option to File menu ({pr}`944`)

## Improvements

- Allow 3D point selection via API ({pr}`907`)
- Add show param to Viewer ({pr}`961`)
- Make mouse drag attributes private in qt_layerlist ({pr}`974`)
- Rename `viewer` attribute on QtViewerDockWidget to `qt_viewer`({pr}`975`)
- Allow LayerList to be initialized by passing in a list of layers ({pr}`979`)
- Rename `object` to `item` in list input arguments ({pr}`980`)
- Add layers.events.changed event ({pr}`982`)

## Bug Fixes

- Fix add points to empty layer ({pr}`933`)
- Fix points thumbnail ({pr}`934`)
- Fix 4D ellipses ({pr}`950`)
- Fix Points highlight bug index (Points-data6-3 test) ({pr}`972`)
- Fix labels colormap by updating computation of low discrepancy images ({pr}`985`)
- Pin jupyter-client<6.0.0 ({pr}`997`)

## Support

- Sphinx docs restructuring (create space for dev-focused prose) ({pr}`942`)
- Fixes broken tutorials links ({pr}`946`)
- Remove 'in-depth' descriptor for tutorials ({pr}`949`)
- Flatten auto-generated docs repo ({pr}`954`)
- Fix bash codeblock in README.md ({pr}`956`)
- Abstract the construction of view/viewermodel ({pr}`957`)
- Add docstrings to qt_layerlist.py ({pr}`958`)
- Fix docs url ({pr}`960`)
- Fix docs script ({pr}`963`)
- Fix docs version tag ({pr}`964`)
- Disallow sphinx 2.4.0; bug fixed in 2.4.1 ({pr}`965`)
- Remove duplicated imports in setup.py ({pr}`969`)
- Fix viewer view_* func signature parity ({pr}`976`)
- Fix ability to test released distributions ({pr}`1002`)
- Fix recursive-include in manifest.in ({pr}`1003`)

## 11 authors added to this release (alphabetical)

- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Hagai Har-Gil](https://github.com/napari/napari/commits?author=HagaiHargil) - @HagaiHargil
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Justin Kiggins](https://github.com/napari/napari/commits?author=neuromusic) - @neuromusic
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Peter Boone](https://github.com/napari/napari/commits?author=boonepeter) - @boonepeter
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Tony Tung](https://github.com/napari/napari/commits?author=ttung) - @ttung
- [Trevor Manz](https://github.com/napari/napari/commits?author=manzt) - @manzt

## 10 reviewers added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Clinton Roy](https://github.com/napari/napari/commits?author=clintonroy) - @clintonroy
- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Peter Boone](https://github.com/napari/napari/commits?author=boonepeter) - @boonepeter
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Tony Tung](https://github.com/napari/napari/commits?author=ttung) - @ttung
