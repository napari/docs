# napari 0.2.0

We're happy to announce the release of napari 0.2.0! napari is a fast,
interactive, multi-dimensional image viewer for Python. It's designed for
browsing, annotating, and analyzing large multi-dimensional images. It's built
on top of Qt (for the GUI), vispy (for performant GPU-based rendering), and the
scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## New Features

- **Improved UI**, unifying buttons from controls, icons for layers,
  and more understandable dimensions sliders
- Add support for **3D rendering** for all our layer types
- Add a `Surface` layer to render already generated meshes. Support nD meshes
  rendered in 2D or 3D.
- Add `viewer.add_multichannel` method to rapidly add expand a multichannel
  array along one particular axis with different colormaps ({pr}`528`).
- Add basic **undo / redo** functionality to the labels layer

## Deprecations

- Drop `napari.view` method. Replaced with `napari.view_*` methods in for all
  our layer types.
- Drop `Pyramid` layer. Pyramid functionality now integrated into both the
  labels and image layer.

## Pull Requests

- Tutorials ({pr}`395`)
- fix import in cli ({pr}`403`)
- 3D volume viewer - volume layer ({pr}`405`)
- remove vispy backport ({pr}`406`)
- Fix axis shape one ({pr}`409`)
- Xarray example ({pr}`410`)
- fix clim setter ({pr}`411`)
- switch to pyside2 ({pr}`412`)
- fix delete markers ({pr}`413`)
- [FIX] paint color inidicator update when shuffle color ({pr}`416`)
- QT returns a warning instead of an error ({pr}`418`)
- Fix Crash with stacked binary tiffs. ({pr}`422`)
- cleanup shape classes ({pr}`423`)
- move tutorials to napari-tutorials repo ({pr}`425`)
- fix vispy 0.6.0 colormap bug ({pr}`426`)
- fix points keypress ({pr}`427`)
- minimal vispy 0.6 colormap fix ({pr}`430`)
- Fix dims sliders ({pr}`431`)
- add `_vispy` init ({pr}`433`)
- Expose args for blending, visible, opacity ({pr}`434`)
- more dims fixes ({pr}`435`)
- fix screenshot ({pr}`437`)
- fix dims mixing ({pr}`438`)
- test add_* signatures and improve docstring testing ({pr}`439`)
- add qt console ({pr}`443`)
- adapt existing keybindings to use new system ({pr}`444`)
- fix aspect ratio ({pr}`446`)
- Swappable dimensions ({pr}`451`)
- use __init_subclass__ in keymap mixin to create empty class keymap ({pr}`452`)
- use pytest-qt ({pr}`453`)
- use codecov ({pr}`455`)
- expose scaling factor for volume ({pr}`463`)
- fix size policy on layers list ({pr}`466`)
- Allow out of range float images ({pr}`468`)
- add viewer keybindings ({pr}`472`)
- fix windows ci build ({pr}`479`)
- fix OSX CI ({pr}`482`)
- remove vispy backport ({pr}`483`)
- clean up black pre-commit hook & exclusion pattern ({pr}`484`)
- remove vispy code from layer models ({pr}`485`)
- host docs ({pr}`486`)
- Fix keybindings ({pr}`487`)
- layer views ({pr}`488`)
- Include requirements/default.txt in sdist ({pr}`491`)
- Integrate 3D rendering with layers ({pr}`493`)
- revert "layer views (#488)" ({pr}`494`)
- support more image dtypes ({pr}`498`)
- rename clim ({pr}`499`)
- fix cursor position ({pr}`501`)
- add surface layer ({pr}`503`)
- don't ignore errors in events ({pr}`505`)
- fix contributing guidelines ({pr}`506`)
- create release guide ({pr}`508`)
- fix node ordering ({pr}`509`)
- fix call signature to work with keyword-only arguments ({pr}`510`)
- prevent selected label from being reduced below 0 ({pr}`512`)
- fix typos in release guidelines ({pr}`522`)
- clip rgba images ({pr}`524`)
- DOC: specify that IPython needs to be started with `gui=qt` ({pr}`525`)
- add multichannel ({pr}`528`)
- enable `python -m napari` ({pr}`529`)
- support 3D rendering shapes layer ({pr}`532`)
- add undo/redo to labels layer ({pr}`533`)
- unified layer ui ({pr}`536`)
- add `view_*` methods at napari level ({pr}`542`)
- Merge pyramid layer into image ({pr}`545`)
- Add release notes ({pr}`546`)
- Labels pyramid ({pr}`548`)
- fix 3d point rendering ({pr}`549`)
- make dims sliders bars ({pr}`550`)
- fix menubar focus mac ({pr}`553`)
- move zarr, xarray, dask from examples to tests ({pr}`555`)
- fix pyramid guessing ({pr}`556`)
- Update NumPy pad call for 1.16.4 ({pr}`559`)
- WIP Unify IO between different modalities ({pr}`560`)

## 11 authors added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Alexandre de Siqueira](https://github.com/napari/napari/commits?author=alexdesiqueira) - @alexdesiqueira
- [Ariel Rokem](https://github.com/napari/napari/commits?author=arokem) - @arokem
- [Christoph Gohlke](https://github.com/napari/napari/commits?author=cgohlke) - @cgohlke
- [Jan Eglinger](https://github.com/napari/napari/commits?author=imagejan) - @imagejan
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Mars Huang](https://github.com/napari/napari/commits?author=marshuang80) - @marshuang80
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pranathi Vemuri](https://github.com/napari/napari/commits?author=pranathivemuri) - @pranathivemuri

## 6 reviewers added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Loic Royer](https://github.com/napari/napari/commits?author=royerloic) - @royerloic
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pranathi Vemuri](https://github.com/napari/napari/commits?author=pranathivemuri) - @pranathivemuri
