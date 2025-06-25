# napari 0.6.2
⚠️ *Note: these release notes are still in draft while 0.6.2 is in release candidate testing.* ⚠️

*Wed, Jun 25, 2025*

We’re happy to announce the release of napari 0.6.2!

napari is a fast, interactive, multi-dimensional image viewer for Python. It’s designed for exploring, annotating, and analyzing multi-dimensional images. It’s built on Qt (for the GUI), VisPy (for performant GPU-based rendering), and the scientific Python stack (NumPy, SciPy, and friends).

For more information, examples, and documentation, please visit our website: https://napari.org/

## Highlights

### The amazing new Grid mode! 🗺️

The visualization of Grid mode has been redone from the ground up! This new Grid mode [(#7870)](https://github.com/napari/napari/pull/7870) now puts each layer into its own view (a VisPy Viewbox) with cameras linked together. Now, you can pan and zoom one view, and all other views in the grid will follow along. No longer are layers awkwardly transformed into the same world space and displayed in a grid, only to make comparing the details of each a challenge. Grid based exploration is now fluid, fast, and intuitive, especially when working with large images and 3D+ data! The mouse can even be used over one View, while updating the data, such as a label or shape annotation, in the selected layer of a different view. The usual napari overlays can now also be added to each grid, instead of just the canvas (eg. `viewer.scale_bar.gridded = True`).

### The Features Table Widget is now a napari builtin! 📊

The features table from [napari-properties-viewer](https://github.com/kevinyamauchi/napari-properties-viewer) is now a builtin widget in napari [(#7877)](https://github.com/napari/napari/pull/7877) *and* greatly improved! This widget allows you to view (and even edit) the properties of Points, Shapes, and Labels layers in a table widget. The widget can be opened from the `Layers` menu -> `Visualize` -> `Features table widget (napari builtins)` or from the command palette.  You can also save the properties table to a CSV file. Check out the [Features table widget](https://napari.org/dev/gallery/features_table_widget.html) example to learn more.

### Community developments! 📅

We are excited to share our new [active roadmap](https://napari.org/stable/roadmaps/active_roadmap.html) which is a living document that will be updated as we continue to develop napari. This document is intended to help the community understand the priorities of the napari team and to help us all work together to make napari better. We are also now including all napari related events in the [community calendar](https://napari.org/stable/community/meeting_schedule.html) and as an [image.sc post](https://forum.image.sc/t/napari-community-meetings-and-events/113689), including conferences, tutorials, sprints, virtual seminars, and more. If you have an event you would like to add, please reach out to us!

### Some big changes for contributors! 🛠️

1. **Contributing documentation is now a much smoother experience!** By default, new documentation will build in around 3 minutes, instead of the previous 20 minutes. This speed is thanks to new, slimmer `make` commands (`slimfast` by default) that can also be triggered in PRs with a bot (eg. `@napari-bot make docs`). Read our updated [docs contribution guide](https://napari.org/dev/developers/contributing/documentation/index.html) and reach out for help.
2. **The organization of the napari repo has been updated by moving into a `src/` directory [(#7952)](https://github.com/napari/napari/pull/7952).** This is modern best practice in Python projects (and what has long been standard in our [napari-plugin-template](https://github.com/napari/napari-plugin-template)) to avoid issues with relative imports and *should* now always result in importing the napari version installed in the current environment. For developers, especially of pull requests prior to this release, you may have many merge conflicts to resolve. Please ping the napari team if you would like help resolving these conflicts.
3. **There is now public API to access widgets docked in the viewer [(#7965)](https://github.com/napari/napari/pull/7965).** Check out the new documentation on the napari website to learn more about using this API to [communicate between widgets](https://napari.org/dev/plugins/advanced_topics/widget_communication.html). If you previously used `viewer.window._dock_widgets`, you should now use `viewer.window.dock_widgets`.

## New Features

- Features table widget as builtin ([#7877](https://github.com/napari/napari/pull/7877))
- Add 'zoom-box' to the viewer ([#8004](https://github.com/napari/napari/pull/8004))

## Improvements

- Reduce warmup of numba if non numba backend is selected ([#7917](https://github.com/napari/napari/pull/7917))
- Optional rotation handle for selection box overlay + simplify inheritance for Vispy overlays ([#7958](https://github.com/napari/napari/pull/7958))
- Add public API to get access to docked widgets ([#7965](https://github.com/napari/napari/pull/7965))
- Allow to use ViewerModel as annotation of plugin constructor argument ([#8002](https://github.com/napari/napari/pull/8002))
- speedup edge width set by use `batched_updates` context manager ([#8006](https://github.com/napari/napari/pull/8006))
- Update [shapes]: 'make select_all_shapes' keybinding a toggle ([#8014](https://github.com/napari/napari/pull/8014))
- Update[shortcuts]: add Ctrl/Cmd-A as secondary keybinding for select_all_shapes ([#8015](https://github.com/napari/napari/pull/8015))
- "Reverse" ordering of layers in grid mode, now matching LayerList index ([#8044](https://github.com/napari/napari/pull/8044))
- Fix Shapes layer to work with Features Table ([#8048](https://github.com/napari/napari/pull/8048))

## Performance

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
- Bugfix: ensure multiscale images can be merged using contextual action ([#8025](https://github.com/napari/napari/pull/8025))
- Fix Shapes layer to work with Features Table ([#8048](https://github.com/napari/napari/pull/8048))

## Build Tools

- Bump requests from 2.32.3 to 2.32.4 in /resources ([#8010](https://github.com/napari/napari/pull/8010))

## Documentation

- Update README to use `imshow` and add example to generate image ([#7989](https://github.com/napari/napari/pull/7989))
- Update docstring in `mouse_drag_callback.py` ([#8019](https://github.com/napari/napari/pull/8019))
- Update version switcher for 0.6.1 ([docs#713](https://github.com/napari/docs/pull/713))
- Update contributing docs page ([docs#715](https://github.com/napari/docs/pull/715))
- Update code of conduct committee members ([docs#716](https://github.com/napari/docs/pull/716))
- Add features table widget ([docs#718](https://github.com/napari/docs/pull/718))
- Update docker build links ([docs#720](https://github.com/napari/docs/pull/720))
- Add initial documentation about widget communication ([docs#721](https://github.com/napari/docs/pull/721))
- Update installation.md to link to conda getting started not miniconda ([docs#726](https://github.com/napari/docs/pull/726))
- Update governance docs ([docs#729](https://github.com/napari/docs/pull/729))
- Initial release notes for alpha of 0.6.2 ([docs#734](https://github.com/napari/docs/pull/734))
- Add active roadmap document ([docs#735](https://github.com/napari/docs/pull/735))
- Use darker blue for community meetings in napari calendar ([docs#736](https://github.com/napari/docs/pull/736))

## Other Pull Requests

- Add docs constraints for python 3.12 ([#7714](https://github.com/napari/napari/pull/7714))
- Include Qt PyPI server for pre-releases ([#7803](https://github.com/napari/napari/pull/7803))
- Refactor layer overlays visuals from VispyLayer to VispyCanvas ([#7835](https://github.com/napari/napari/pull/7835))
- Add cron check to update reader extensions ([#7907](https://github.com/napari/napari/pull/7907))
- Update `dask`, `hypothesis`, `numpy`, `tensorstore`, `vispy` ([#7948](https://github.com/napari/napari/pull/7948))
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
- Remove the reset_scroll_progress action and keybinding ([#7990](https://github.com/napari/napari/pull/7990))
- Stop status thread on Keyboard Interruption (Ctrl+C) ([#7994](https://github.com/napari/napari/pull/7994))
- Update `hypothesis`, `magicgui`, `pandas`, `pyqt6`, `pytest`, `pytest-pretty` ([#8000](https://github.com/napari/napari/pull/8000))
- Update pyproject.toml to fix coverage paths (alt) ([#8001](https://github.com/napari/napari/pull/8001))
- [Maintenance] Remove redundant initialization in Points layer and restructure for clarity ([#8005](https://github.com/napari/napari/pull/8005))
- Fix numba fail of compile on GHA macOS runners ([#8018](https://github.com/napari/napari/pull/8018))
- Update `certifi`, `coverage`, `hypothesis`, `pydantic`, `superqt`, `tifffile`, `xarray` ([#8029](https://github.com/napari/napari/pull/8029))
- [Update] Added `remove` , `remove_selected` and `pop` in Shapes and Points ([#8031](https://github.com/napari/napari/pull/8031))
- Update `hypothesis`, `pytest`, `superqt` ([#8036](https://github.com/napari/napari/pull/8036))
- Stop benchmark reporting if benchmark action is skipped ([#8037](https://github.com/napari/napari/pull/8037))
- Update `app-model`, `hypothesis`, `pygments`, `scipy` ([#8040](https://github.com/napari/napari/pull/8040))
- Update `app-model` pin to >=0.4.0, update `hypothesis`, `pygments`, `scipy` ([#8041](https://github.com/napari/napari/pull/8041))
- [pre-commit.ci] pre-commit autoupdate ([#8042](https://github.com/napari/napari/pull/8042))
- Fix comment and manual dispatch triggered build jobs ([docs#723](https://github.com/napari/docs/pull/723))
- Test passing PR number instead of ref on triggered build ([docs#738](https://github.com/napari/docs/pull/738))
- [maint] fix circleCI branch naming in trigger action ([docs#739](https://github.com/napari/docs/pull/739))


## 13 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Ashley Anderson](https://github.com/napari/docs/commits?author=aganders3) - @aganders3
- [Carol Willing](https://github.com/napari/docs/commits?author=willingc) - @willingc
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) ([docs](https://github.com/napari/docs/commits?author=DragaDoncila))  - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Jacopo Abramo](https://github.com/napari/napari/commits?author=jacopoabramo) - @jacopoabramo +
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) ([docs](https://github.com/napari/docs/commits?author=brisvag))  - @brisvag
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [Maximilian Mayrhauser](https://github.com/napari/napari/commits?author=Llewi) - @Llewi +
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) ([docs](https://github.com/napari/docs/commits?author=psobolewskiPhD))  - @psobolewskiPhD
- [Rahul Kumar](https://github.com/napari/napari/commits?author=rahul713rk) - @rahul713rk +
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko


## 12 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Ashley Anderson](https://github.com/napari/docs/commits?author=aganders3) - @aganders3
- [Carol Willing](https://github.com/napari/docs/commits?author=willingc) - @willingc
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) ([docs](https://github.com/napari/docs/commits?author=DragaDoncila))  - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Jacopo Abramo](https://github.com/napari/napari/commits?author=jacopoabramo) - @jacopoabramo +
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) ([docs](https://github.com/napari/docs/commits?author=brisvag))  - @brisvag
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) ([docs](https://github.com/napari/docs/commits?author=psobolewskiPhD))  - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko
- [Wouter-Michiel Vierdag](https://github.com/napari/docs/commits?author=melonora) - @melonora

