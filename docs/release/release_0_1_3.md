# napari 0.1.3

We're happy to announce the release of napari 0.1.3! napari is a fast,
interactive, multi-dimensional image viewer for Python. It's designed for
browsing, annotating, and analyzing large multi-dimensional images. It's built
on top of Qt (for the GUI), vispy (for performant GPU-based rendering), and the
scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## New Features

- Support for volumetric rendering of images

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

## 6 authors added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Alexandre de Siqueira](https://github.com/napari/napari/commits?author=alexdesiqueira) - @alexdesiqueira
- [Mars Huang](https://github.com/napari/napari/commits?author=marshuang80) - @marshuang80
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pranathi Vemuri](https://github.com/napari/napari/commits?author=pranathivemuri) - @pranathivemuri

## 4 reviewers added to this release (alphabetical)

- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pranathi Vemuri](https://github.com/napari/napari/commits?author=pranathivemuri) - @pranathivemuri
