# napari 0.4.14

We're happy to announce the release of napari 0.4.14!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).

This is a small release containing some new features and fixing a few issues that have come up since 0.4.13 was released.

This release adds the ability to convert a shapes layer to a labels layer from a context menu available on right clicking the layer list entry ({pr}`3978`). Our vectors layer has gained the 
ability to render vectors in 2D across multiple slices ({pr}`2902`) and points in the points
layer can now be hidden individually ({pr}`3625`).

For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

Complete list of changes below:

## Highlights
- Enable shapes layer (right click) > convert to labels ({pr}`3978`)
- Out-of-slice rendering for Vectors ({pr}`2902`)
- Hide points individually ({pr}`3625`)

## New Features

## Improvements
- Update tests to remove warnings ({pr}`3974`)
- Add test to check that things are removed properly ({pr}`3996`)
- Change base point slice thickness to half a unit ({pr}`3997`)
- Change base vector slice thickness to half a unit ({pr}`4001`)
- Use scikit-image[data] in the bundle ({pr}`4024`)
- Rename n_dimensional to out_of_slice_display in Points and Vectors ({pr}`4007`)
- Raise reader plugin errors sooner, (avoid cryptic error messages) ({pr}`4026`)
- Unlink close button from plugins ({pr}`4027`)
- Update QtProgressBar total when progress total is changed ({pr}`4034`)
- Update on merge to stack action ordering ({pr}`4033`)

## Bug Fixes
- Fix about on python 3.10 ({pr}`3972`)
- Revert changes to scikit-image test API ({pr}`3979`)
- Fix missing builtins in bundle ({pr}`3982`)
- Don't use texture_format auto if float textures not available on machine ({pr}`3990`)
- Fix error when setting ndisplay=3 with empty shapes layer in viewer ({pr}`4003`)
- Fix bug preventing close button on dock widgets ({pr}`4006`)
- Fix point symbol on instantiation ({pr}`4043`)
- Only set dims kwargs on viewer after adding layer ({pr}`4021`)
- Imsave deprecation ({pr}`4057`)

## API Changes

## Deprecations


## Build Tools and Docs
- DOC: Misc doc syntax. ({pr}`3985`)
- Fix include_package_data inclusion in the "your first plugin" docs page ({pr}`4022`)
- 0.4.14 translation strings ({pr}`4029`)
- Use python -m pytest with xvfb-action ({pr}`4046`)
- Update packaging files, remove setup.py and requirements.txt ({pr}`4014`)

## 11 authors added to this release (alphabetical)
- [Alister Burt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [Andy Sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Gregory Lee](https://github.com/napari/napari/commits?author=grlee77) - @grlee77
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Jaime Rodríguez-Guerra](https://github.com/napari/napari/commits?author=jaimergp) - @jaimergp
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Pam](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03


## 11 reviewers added to this release (alphabetical)
- [Alister Burt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [Andy Sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Chi-li Chiu](https://github.com/napari/napari/commits?author=chili-chiu) - @chili-chiu
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Gregory Lee](https://github.com/napari/napari/commits?author=grlee77) - @grlee77
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nathan Clack](https://github.com/napari/napari/commits?author=nclack) - @nclack
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
  

