# napari 0.6.2
⚠️ *Note: these release notes are still in draft while 0.6.2 is in release candidate testing.* ⚠️

*Mon, Jun 23, 2025*


We're happy to announce the release of napari 0.6.2!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website,
https://napari.org.

## Highlights

- Qt controls for thick slicing ([#6146](https://github.com/napari/napari/pull/6146))
- Add grid overlay ([#7827](https://github.com/napari/napari/pull/7827))
- Grid mode using vispy ViewBox and linked cameras ([#7870](https://github.com/napari/napari/pull/7870))
- Features table widget as builtin ([#7877](https://github.com/napari/napari/pull/7877))
- Move napari into `src` layout ([#7952](https://github.com/napari/napari/pull/7952))
- Add public API to get access to docked widgets ([#7965](https://github.com/napari/napari/pull/7965))

## New Features

- Qt controls for thick slicing ([#6146](https://github.com/napari/napari/pull/6146))
- Add automatic area and perimeter measurement for shapes + action ([#7262](https://github.com/napari/napari/pull/7262))
- Add canvas color to public API ([#7778](https://github.com/napari/napari/pull/7778))
- Add grid overlay ([#7827](https://github.com/napari/napari/pull/7827))
- Tiling canvas overlays ([#7836](https://github.com/napari/napari/pull/7836))
- Features table widget as builtin ([#7877](https://github.com/napari/napari/pull/7877))

## Improvements

- Allow use functions from PartSegCore-compiled-backend as numba alternative for data to texture mapping  ([#6617](https://github.com/napari/napari/pull/6617))
- Reduce warmup of numba if non numba backend is selected ([#7917](https://github.com/napari/napari/pull/7917))
- Optional rotation handle for selection box overlay + simplify inheritance for Vispy overlays ([#7958](https://github.com/napari/napari/pull/7958))
- Add public API to get access to docked widgets ([#7965](https://github.com/napari/napari/pull/7965))
- Implement pasting spatial information into higher dimensions ([#7973](https://github.com/napari/napari/pull/7973))
- Allow to use ViewerModel as annotation of plugin constructor argument ([#8002](https://github.com/napari/napari/pull/8002))
- speedup edge width set by use `batched_updates` context manager ([#8006](https://github.com/napari/napari/pull/8006))

## Performance

- Allow use functions from PartSegCore-compiled-backend as numba alternative for data to texture mapping  ([#6617](https://github.com/napari/napari/pull/6617))
- [Shapes] Use the plural methods to update colors of all selected shapes at once ([#7995](https://github.com/napari/napari/pull/7995))

## Bug Fixes

- Fix scalebar theme connection ([#7902](https://github.com/napari/napari/pull/7902))
- Don't add widgets to non-contributable menus ([#7926](https://github.com/napari/napari/pull/7926))
- Fix handle mouse events ([#7936](https://github.com/napari/napari/pull/7936))
- Fix moving of first/last vertex of polygons added in ring mode ([#7942](https://github.com/napari/napari/pull/7942))
- Update shapes highlight on zoom ([#7953](https://github.com/napari/napari/pull/7953))
- Fix invalidate of extent cache in Layers ([#7972](https://github.com/napari/napari/pull/7972))
- [Points] Fix events.data_indices for ActionType.ADDED event when adding single point ([#7983](https://github.com/napari/napari/pull/7983))
- Fix interaction box initialization ([#8011](https://github.com/napari/napari/pull/8011))
- Fix angles not showing correctly in UI ([#8013](https://github.com/napari/napari/pull/8013))

## API Changes

- Expose force_sync context manager ([#7908](https://github.com/napari/napari/pull/7908))

## Documentation

- Add example linking the cameras of two viewers ([#6881](https://github.com/napari/napari/pull/6881))
- Update README to use `imshow` and add example to generate image ([#7989](https://github.com/napari/napari/pull/7989))
- Update version switcher for 0.6.1 ([docs#713](https://github.com/napari/docs/pull/713))
- Update contributing docs page ([docs#715](https://github.com/napari/docs/pull/715))
- Update code of conduct committee members ([docs#716](https://github.com/napari/docs/pull/716))
- Add initial documentation about widget communication ([docs#721](https://github.com/napari/docs/pull/721))
- Update installation.md to link to conda getting started not miniconda ([docs#726](https://github.com/napari/docs/pull/726))
- Update governance docs ([docs#729](https://github.com/napari/docs/pull/729))
- Initial release notes for alpha of 0.6.2 ([docs#734](https://github.com/napari/docs/pull/734))

## Other Pull Requests

- Layer controls widgets refactor ([#7355](https://github.com/napari/napari/pull/7355))
- Add codespell support (config, workflow to detect/not fix) and make it fix few typos ([#7619](https://github.com/napari/napari/pull/7619))
- Add docs constraints for python 3.12 ([#7714](https://github.com/napari/napari/pull/7714))
- Include Qt PyPI server for pre-releases ([#7803](https://github.com/napari/napari/pull/7803))
- Refactor layer overlays visuals from VispyLayer to VispyCanvas ([#7835](https://github.com/napari/napari/pull/7835))
- Use information about units when calculate scale of layers when render ([#7889](https://github.com/napari/napari/pull/7889))
- Add cron check to update reader extensions ([#7907](https://github.com/napari/napari/pull/7907))
- Update `dask`, `hypothesis`, `numpy`, `tensorstore`, `vispy` ([#7948](https://github.com/napari/napari/pull/7948))
- Move export ROI implementation into qt_viewer ([#7950](https://github.com/napari/napari/pull/7950))
- [pre-commit.ci] pre-commit autoupdate ([#7951](https://github.com/napari/napari/pull/7951))
- Add cron check to update reader extensions v2 ([#7957](https://github.com/napari/napari/pull/7957))
- Restore image in Readme ([#7959](https://github.com/napari/napari/pull/7959))
- Add cron check to update reader extensions v3 ([#7966](https://github.com/napari/napari/pull/7966))
- Update `coverage`, `dask`, `fsspec`, `hypothesis`, `pydantic`, `tifffile`, `vispy` ([#7967](https://github.com/napari/napari/pull/7967))
- fix vendored script and trigger workflow on pull_request ([#7968](https://github.com/napari/napari/pull/7968))
- [pre-commit.ci] pre-commit autoupdate ([#7970](https://github.com/napari/napari/pull/7970))
- Remove `layers_change` event that is marked to be removed in 0.5.0 ([#7971](https://github.com/napari/napari/pull/7971))
- [maintenance] Use Wandalen/wretry.action to auto-retry fail in --pre tests ([#7986](https://github.com/napari/napari/pull/7986))
- Update `hypothesis`, `ipython`, `jsonschema`, `tifffile` ([#7987](https://github.com/napari/napari/pull/7987))
- [pre-commit.ci] pre-commit autoupdate ([#7988](https://github.com/napari/napari/pull/7988))
- Stop status thread on Keyboard Interruption (Ctrl+C) ([#7994](https://github.com/napari/napari/pull/7994))
- Update `hypothesis`, `magicgui`, `pandas`, `pyqt6`, `pytest`, `pytest-pretty` ([#8000](https://github.com/napari/napari/pull/8000))
- Update pyproject.toml to fix coverage paths (alt) ([#8001](https://github.com/napari/napari/pull/8001))
- [Maintenance] Remove redundant initialization in Points layer and restructure for clarity ([#8005](https://github.com/napari/napari/pull/8005))
- Update[shortcuts]: add Ctrl/Cmd-A as secondary keybinding for select_all_shapes ([#8015](https://github.com/napari/napari/pull/8015))
- Fix comment and manual dispatch triggered build jobs ([docs#723](https://github.com/napari/docs/pull/723))


## 10 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) ([docs](https://github.com/napari/docs/commits?author=DragaDoncila))  - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Jacopo Abramo](https://github.com/napari/napari/commits?author=jacopoabramo) - @jacopoabramo +
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Maximilian Mayrhauser](https://github.com/napari/napari/commits?author=Llewi) - @Llewi +
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) ([docs](https://github.com/napari/docs/commits?author=psobolewskiPhD))  - @psobolewskiPhD
- [Rahul Kumar](https://github.com/napari/napari/commits?author=rahul713rk) - @rahul713rk +
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko


## 13 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Ashley Anderson](https://github.com/napari/docs/commits?author=aganders3) - @aganders3
- [Carol Willing](https://github.com/napari/docs/commits?author=willingc) - @willingc
- [Daniel Althviz Moré](https://github.com/napari/docs/commits?author=dalthviz) - @dalthviz
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) ([docs](https://github.com/napari/docs/commits?author=DragaDoncila))  - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Jacopo Abramo](https://github.com/napari/napari/commits?author=jacopoabramo) - @jacopoabramo +
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) ([docs](https://github.com/napari/docs/commits?author=psobolewskiPhD))  - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko
- [Wouter-Michiel Vierdag](https://github.com/napari/docs/commits?author=melonora) - @melonora
- [Yaroslav Halchenko](https://github.com/napari/docs/commits?author=yarikoptic) - @yarikoptic

