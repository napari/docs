# napari 0.2.7

We're happy to announce the release of napari 0.2.7! napari is a fast,
interactive, multi-dimensional image viewer for Python. It's designed for
browsing, annotating, and analyzing large multi-dimensional images. It's built
on top of Qt (for the GUI), vispy (for performant GPU-based rendering), and the
scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## Highlights

- Play button for animating axes now in the GUI
- Threshold slider for much improved isosurface rendering
- Dockable widgets (!)
- Slice information on sliders
- Dramatically improved performance with many invisible layers
- Adopted a Governance model with a mission and values statement
- Added a new Core Dev guide

## New Features

- Add governance model, mission and values, core dev guide ({pr}`655`)

## Improvements

- Iso-surface threshold slider ({pr}`712`)
- Add play button to GUI ({pr}`726`)
- Make layers list dockable ({pr}`727`)
- Add Zenodo badge to documentation ({pr}`743`)
- Add a dock icon ({pr}`744`)
- Show splash screen for cli launch ({pr}`745`)
- Add benchmarks for setting `.data` in Image layers ({pr}`747`)
- Refactor layer tests to be more parametrized ({pr}`723`)
- Support opening labels layers via directly from path ({pr}`748`)
- Simplify keybindings info display ({pr}`749`)
- Clean up info box ({pr}`750`)
- Display slice info on right of slider ({pr}`759`)
- Block refresh for invisible layers ({pr}`776`)
- About copy button to info display box ({pr}`798`)
- Add blocked_signals context manager ({pr}`797`)
- Better selected menu header background color ({pr}`813`)

## Bug Fixes

- Fix StringEnum setting and errors ({pr}`757`)
- scale argument now accepts array-like input ({pr}`765`)
- fix `set_fps` type to float ({pr}`767`)
- Add shutdown method to QtViewer that closes all resources ({pr}`769`)
- Change language around windows support in readme ({pr}`779`)
- Revert #784 console shutdown conditionals ({pr}`796`)
- Fix window raise & inactive menubar conflict ({pr}`795`)
- Change documentation on qt.py folder location ({pr}`783`)
- Updating qt_console with better resource management ({pr}`784`)
- Respect vispy max texture limits ({pr}`788`)
- Fix (minor) deprecation warnings ({pr}`800`)
- Fix FPS spin box on Qt < 5.12 ({pr}`803`)
- Bumpy vispy dependency to 0.6.4 ({pr}`807`)
- Set threshold for codecov failure ({pr}`806`)
- Rename util to utils in MANIFEST.in ({pr}`811`)
- Add `requirements/release.txt` with release dependencies ({pr}`809`)

## API Changes

- Rename util to utils across repo ({pr}`808`)
- Move Labels utility functions to labels_util.py ({pr}`770`)
- Move Image layer utility functions to image_utils.py ({pr}`775`)
- Move Layer utility functions to /napari/layers/layer_utils.py ({pr}`778`)
- Refactor util.misc ({pr}`781`)
- Drop ndim keyword from labels layer ({pr}`773`)

## 7 authors added to this release (alphabetical)

- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Peter Boone](https://github.com/napari/napari/commits?author=boonepeter) - @boonepeter
- [Shannon Axelrod](https://github.com/napari/napari/commits?author=shanaxel42) - @shanaxel42
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03

## 7 reviewers added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Shannon Axelrod](https://github.com/napari/napari/commits?author=shanaxel42) - @shanaxel42
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
