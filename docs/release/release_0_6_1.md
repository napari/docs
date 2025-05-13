# napari 0.6.1
⚠️ *Note: these release notes are still in draft while 0.6.1 is in release candidate testing.* ⚠️
*Wed, May 14, 2025*
We’re happy to announce the release of napari 0.6.0! The right-handed release! This release features major changes so read on to see how they might affect you!

napari is a fast, interactive, multi-dimensional image viewer for Python. It’s designed for exploring, annotating, and analyzing multi-dimensional images. It’s built on Qt (for the GUI), VisPy (for performant GPU-based rendering), and the scientific Python stack (NumPy, SciPy, and friends).

For more information, examples, and documentation, please visit our website: https://napari.org/

## Highlights

- HiLo 👋 colormaps!

napari now depends on VisPy 0.15.0 ([#7846](https://github.com/napari/napari/pull/7846))
which among other things gives us the HiLo colormap!

## New Features

- Add inheritance of spatial data for functional plugin that return layer data.  ([#6986](https://github.com/napari/napari/pull/6986))
- Bump to vispy 0.15 and update Colormap model ([#7846](https://github.com/napari/napari/pull/7846))
- Add multiplicative blending ([#7868](https://github.com/napari/napari/pull/7868))
- Features table widget as builtin ([#7877](https://github.com/napari/napari/pull/7877))

## Improvements

- Copy units from layer to layer ([#7727](https://github.com/napari/napari/pull/7727))
- Check return value is valid LayerDataTuple ([#7851](https://github.com/napari/napari/pull/7851))

## Bug Fixes

- Refresh extent on async slicing ([#7853](https://github.com/napari/napari/pull/7853))
- Do not expose vispy BaseColormaps ([#7858](https://github.com/napari/napari/pull/7858))
- Properly determine dtype for view of Labels ([#7883](https://github.com/napari/napari/pull/7883))
- Fix scalebar color toggle with theme change ([#7898](https://github.com/napari/napari/pull/7898))

## Documentation

- Update the version switcher for 0.6.0 ([docs#697](https://github.com/napari/docs/pull/697))
- Update conf.py to try to fix opengraph image for dev and future deployments ([docs#700](https://github.com/napari/docs/pull/700))
- Update sidebar-nav-bs.html to try to fix links ([docs#702](https://github.com/napari/docs/pull/702))

## Other Pull Requests

- Add codespell support (config, workflow to detect/not fix) and make it fix few typos ([#7619](https://github.com/napari/napari/pull/7619))
- Remove outdated QSS styling elements ([#7655](https://github.com/napari/napari/pull/7655))
- Add docs contraints for python 3.12 ([#7714](https://github.com/napari/napari/pull/7714))
- Update `hypothesis`, `ipython`, `numpy`, `pillow`, `pydantic` ([#7823](https://github.com/napari/napari/pull/7823))
- Update builtins read extensions ([#7826](https://github.com/napari/napari/pull/7826))
- Skip tests that are failing because of Qt bug ([#7884](https://github.com/napari/napari/pull/7884))
- Use `ViewerModel` instead of `make_napari_viewer` in `test_toggle_axes_scale_bar_attr` ([#7885](https://github.com/napari/napari/pull/7885))
- Update `pydantic`, `pyqt6`, `xarray` ([#7886](https://github.com/napari/napari/pull/7886))
- [pre-commit.ci] pre-commit autoupdate ([#7891](https://github.com/napari/napari/pull/7891))
- Fix `test_view_menu.py::test_toggle_menubar` to pass locally ([#7892](https://github.com/napari/napari/pull/7892))
- Add information about launch command to napari info dialog ([#7897](https://github.com/napari/napari/pull/7897))
- Add information about installed plugins to info dialog ([#7899](https://github.com/napari/napari/pull/7899))
- Surface original error when a selected plugin fails to read file. ([#7901](https://github.com/napari/napari/pull/7901))
- Update `hypothesis`, `matplotlib`, `psygnal`, `scipy`, `tifffile`, `virtualenv` ([#7906](https://github.com/napari/napari/pull/7906))
- Change @brisvag affiliation ([#7909](https://github.com/napari/napari/pull/7909))
- [pre-commit.ci] pre-commit autoupdate ([#7910](https://github.com/napari/napari/pull/7910))
- Update build_trigger.yml to fix Circle pipeline ([docs#701](https://github.com/napari/docs/pull/701))


## 5 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Peter Sobolewski](https://github.com/napari/docs/commits?author=psobolewskiPhD) - @psobolewskiPhD


## 9 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Carol Willing](https://github.com/napari/docs/commits?author=willingc) - @willingc
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Genevieve Buckley](https://github.com/napari/docs/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Peter Sobolewski](https://github.com/napari/docs/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/docs/commits?author=TimMonko) - @TimMonko
- [Yaroslav Halchenko](https://github.com/napari/docs/commits?author=yarikoptic) - @yarikoptic

