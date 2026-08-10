# napari 0.9.0
⚠️ *Note: these release notes are still in draft while 0.9.0a2 is in prerelease testing.* ⚠️

*Mon, Aug 17, 2026*

We're happy to announce the release of napari 0.9.0!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website,
https://napari.org.

napari follows [EffVer (Intended Effort Versioning)](https://effver.org/); this is a **Macro** release containing awesome new features, but may require dedication of some significant time when upgrading projects to use this version.

## Highlights

### Fuzzy find in command palette

Implement fuzzy find for the command palette ([#8661](https://github.com/napari/napari/pull/8661))

### Adjust grid rendering with hidden layers

If using grid layout without using stride, there are no blanks fields for hidden layers
thanks to [#9244](https://github.com/napari/napari/pull/9244)

### Inherit axis labels from layers

Thanks to [#9282](https://github.com/napari/napari/pull/9282) the axis labels in interface, next to slide and `Dims.axis_labels`
are calculated based on axis labels of layers

### Status bar coordinates as floats

Thanks to [#9287](https://github.com/napari/napari/pull/9287) we no longer render coordinates on scale bar
as integers, but as floats. It is important for all who use fractional
`Layer.scale`

### Public API for auto contrast limit

In [#9271](https://github.com/napari/napari/pull/9271) the public API for auto contrast limits is added



- Canvas model ([#8633](https://github.com/napari/napari/pull/8633))
- Implement Surface slicing with async request/response ([#8783](https://github.com/napari/napari/pull/8783))
- Remove translations code ([#8935](https://github.com/napari/napari/pull/8935))
- Add builtin Wavefront OBJ to surfaces reader ([#9228](https://github.com/napari/napari/pull/9228))


- Fix hidden grids when stride is not abs(1) ([#9311](https://github.com/napari/napari/pull/9311))
- Inherit axis label, scale, unit, and translate from Xarrays ([#9316](https://github.com/napari/napari/pull/9316))
- Dynamically construct layer controls based on selection ([#9318](https://github.com/napari/napari/pull/9318))

## New Features

- Implement fuzzy find for the command palette ([#8661](https://github.com/napari/napari/pull/8661))
- Implement Surface slicing with async request/response ([#8783](https://github.com/napari/napari/pull/8783))
- feat: add `new` label button to the labels controls ([#9215](https://github.com/napari/napari/pull/9215))
- Add builtin Wavefront OBJ to surfaces reader ([#9228](https://github.com/napari/napari/pull/9228))
- Add guided viewer tour ([#9290](https://github.com/napari/napari/pull/9290))
- Inherit axis label, scale, unit, and translate from Xarrays ([#9316](https://github.com/napari/napari/pull/9316))
- Dynamically construct layer controls based on selection ([#9318](https://github.com/napari/napari/pull/9318))

## Improvements

- MAINT Always raise error when `widget_name` given in `get_widget_contribution` ([#6544](https://github.com/napari/napari/pull/6544))
- Small refactor of point slicing + `rescale` projection mode to replace out_of_slice_display ([#8786](https://github.com/napari/napari/pull/8786))
- Refactor out-of-slice display for vectors into a projection mode ([#9032](https://github.com/napari/napari/pull/9032))
- [perf] Use chunk-aware loading for 2d multiscale ([#9145](https://github.com/napari/napari/pull/9145))
- move features table widget command to the Metadata menu ([#9231](https://github.com/napari/napari/pull/9231))
- fix: change the order of edge/face color and border ([#9232](https://github.com/napari/napari/pull/9232))
- Move the layer lock to group with link/unlink in layer list context menu ([#9235](https://github.com/napari/napari/pull/9235))
- fix: adjust the layout based on the hidden layers in grid ([#9244](https://github.com/napari/napari/pull/9244))
- Improve slider handle conspicuity by using theme's `current` color for active dim  ([#9255](https://github.com/napari/napari/pull/9255))
- publicly expose auto contrast limits ([#9271](https://github.com/napari/napari/pull/9271))
- update dims axis labels from layers axis labels ([#9282](https://github.com/napari/napari/pull/9282))
- Status bar coordinates as floats ([#9287](https://github.com/napari/napari/pull/9287))
- UX: Indicate web links in Help menu with ↗ (unicode character) ([#9291](https://github.com/napari/napari/pull/9291))
- New layer inherits axis labels when derived from another layer ([#9293](https://github.com/napari/napari/pull/9293))
- Adding histogram to surfaces ([#9306](https://github.com/napari/napari/pull/9306))
- Fix hidden grids when stride is not abs(1) ([#9311](https://github.com/napari/napari/pull/9311))
- Dynamically construct layer controls based on selection ([#9318](https://github.com/napari/napari/pull/9318))
- UX/UI: Bump the splitter (separator) size by 1px ([#9344](https://github.com/napari/napari/pull/9344))
- Add middle position to canvas overlays (in addition to top and bottom) ([#9374](https://github.com/napari/napari/pull/9374))

## Performance

- [perf] Use chunk-aware loading for 2d multiscale ([#9145](https://github.com/napari/napari/pull/9145))
- [perf] Defer PIL import in labels.py polygon mask ([#9205](https://github.com/napari/napari/pull/9205))

## Bug Fixes

- Fix multiscale level selection for anisotropic data ([#9201](https://github.com/napari/napari/pull/9201))
- fix async colormap ([#9209](https://github.com/napari/napari/pull/9209))
- Fix cross layer in multiple viewer example to use line vectors. ([#9213](https://github.com/napari/napari/pull/9213))
- Do not update `current_properties` on Shapes selection changed  ([#9221](https://github.com/napari/napari/pull/9221))
- fix: action binding the `new-label` tooltips  with shortcuts ([#9230](https://github.com/napari/napari/pull/9230))
- fix: add minimum value to grid mode strides to allow negative strides ([#9236](https://github.com/napari/napari/pull/9236))
- fix(qt): dimension sliders need a minimum width ([#9254](https://github.com/napari/napari/pull/9254))
- fix(key_bindings): make navigation keys auto-repeat however they are bound ([#9257](https://github.com/napari/napari/pull/9257))
- Fix sync slicing when toggling to 3D with auto contrast ([#9263](https://github.com/napari/napari/pull/9263))
- Fix enum breaks from translations removal ([#9274](https://github.com/napari/napari/pull/9274))
- Fix auto_contrast button state initialization ([#9289](https://github.com/napari/napari/pull/9289))
- Vectors: make edge_color_mode = 'direct' actually leave the feature mapping ([#9333](https://github.com/napari/napari/pull/9333))
- Use magnitude of `Layer.scale` for points/shape handles ([#9339](https://github.com/napari/napari/pull/9339))
- fix(layer_utils): handle non-native byte order in convert_to_uint8 ([#9345](https://github.com/napari/napari/pull/9345))
- Vectors: redraw after edge color mode remaps colors ([#9353](https://github.com/napari/napari/pull/9353))
- Change `Dims` slider connection from `textChanged` to `textEdited` to stop wrong updates ([#9355](https://github.com/napari/napari/pull/9355))
- fix(vectors): stop edge-color controls mutating the layer and hiding mode changes ([#9364](https://github.com/napari/napari/pull/9364))
- Fix missing `f` for strings modified in #8935 ([#9371](https://github.com/napari/napari/pull/9371))
- Fix the built-in `nan` colormap setting `bad_color` instead of `nan_color` ([#9373](https://github.com/napari/napari/pull/9373))

## Deprecations

- Canvas model ([#8633](https://github.com/napari/napari/pull/8633))
- Small refactor of point slicing + `rescale` projection mode to replace out_of_slice_display ([#8786](https://github.com/napari/napari/pull/8786))
- Refactor out-of-slice display for vectors into a projection mode ([#9032](https://github.com/napari/napari/pull/9032))
- Refactor floating_axes/axes into canvas_axes/scene_axes ([#9363](https://github.com/napari/napari/pull/9363))

## Documentation

- Update homepage video for 0.8.0/.1 changes ([docs#1070](https://github.com/napari/docs/pull/1070))
- Enhance contributing documentation with GitHub edit info ([docs#1075](https://github.com/napari/docs/pull/1075))
- Adding uv to getting started - installation ([docs#1076](https://github.com/napari/docs/pull/1076))
- make napari logo usage page ([docs#1077](https://github.com/napari/docs/pull/1077))
- Delete useless line ([docs#1078](https://github.com/napari/docs/pull/1078))
- Update auto-fill-labels loop video to extend end frame ([docs#1082](https://github.com/napari/docs/pull/1082))
-  NAP 10 migration events ([docs#1086](https://github.com/napari/docs/pull/1086))
- Bring several NAPs up to date ([docs#1091](https://github.com/napari/docs/pull/1091))
- Update dev instructions to use prek ([docs#1096](https://github.com/napari/docs/pull/1096))
- Add initial release notes for 0.9.0 ([docs#1097](https://github.com/napari/docs/pull/1097))
- Update release notes for napari 0.9.0a2 ([docs#1099](https://github.com/napari/docs/pull/1099))
- Fix building docs with PyQt6 ([docs#1102](https://github.com/napari/docs/pull/1102))
- Update overlay docstrings ([#9081](https://github.com/napari/napari/pull/9081))
- Add stereo 3D viewer widget example ([#9219](https://github.com/napari/napari/pull/9219))
- Update recommended Python version in README from 3.11 to 3.13 ([#9223](https://github.com/napari/napari/pull/9223))
- Add (Euro)SciPy Sprint Authors to Citation ([#9234](https://github.com/napari/napari/pull/9234))
- Gallery example of using a background map ([#9245](https://github.com/napari/napari/pull/9245))
- Adding 4D sample data as a heat diffusion ([#9246](https://github.com/napari/napari/pull/9246))
- Add guided viewer tour ([#9290](https://github.com/napari/napari/pull/9290))
- deprecate setting dims axis labels in examples ([#9297](https://github.com/napari/napari/pull/9297))
- Load data from zarr in map example if contextily fails ([#9307](https://github.com/napari/napari/pull/9307))
- Example: combine points and vectors to build a 3D structured object ([#9340](https://github.com/napari/napari/pull/9340))
- Add projection mode to class Image attributes docstring ([#9378](https://github.com/napari/napari/pull/9378))

## Other Pull Requests

- Update label name in condition of label trigger build ([docs#1067](https://github.com/napari/docs/pull/1067))
- [pre-commit.ci] pre-commit autoupdate ([docs#1069](https://github.com/napari/docs/pull/1069))
- Update version switcher to point to 0.8.0 as stable ([docs#1071](https://github.com/napari/docs/pull/1071))
- Remove contributing text about adding translations ([docs#1081](https://github.com/napari/docs/pull/1081))
- Update info about Canvas and Scene models ([docs#1083](https://github.com/napari/docs/pull/1083))
- ci(dependabot): bump the github-actions group with 4 updates ([docs#1094](https://github.com/napari/docs/pull/1094))
- [pre-commit.ci] pre-commit autoupdate ([docs#1095](https://github.com/napari/docs/pull/1095))
- Add auto labeling as maintenance PR that edit `.pre-commit-config.yml` ([docs#1098](https://github.com/napari/docs/pull/1098))
- fix(typing): add type hints and fix mypy errors in `qt_viewer.py` ([#9076](https://github.com/napari/napari/pull/9076))
- fix(typing): add typing and fix mypy error in `qt_mode_buttons.py` ([#9110](https://github.com/napari/napari/pull/9110))
- Use shared version of label clean workflow ([#9116](https://github.com/napari/napari/pull/9116))
- Remove `qt_dict_table.py` as its unused  ([#9119](https://github.com/napari/napari/pull/9119))
- fix(typing): add typing and fix mypy error in `qt_face_color.py`  ([#9123](https://github.com/napari/napari/pull/9123))
- fix(typing): add typing and fix mypy error in `_base_item_model.py` ([#9126](https://github.com/napari/napari/pull/9126))
- fix(typing): add typing and fix mypy error in `_base_item_view.py` ([#9127](https://github.com/napari/napari/pull/9127))
- fix(typing): add typing and fix mypy error in `qt_axis_model.py` ([#9167](https://github.com/napari/napari/pull/9167))
- fix(typing): add typing and fix mypy error in `qt_list_model.py` ([#9169](https://github.com/napari/napari/pull/9169))
- typing: remove `experimental.qt_poll.py` from mypy ignore ([#9171](https://github.com/napari/napari/pull/9171))
- Add hint for missing qt6-wayland when conda Qt cannot start napari on Wayland ([#9174](https://github.com/napari/napari/pull/9174))
- fix(typing): add typing and fix mypy error in `qt_border_color.py` ([#9179](https://github.com/napari/napari/pull/9179))
- fix(typing): add typing and fix mypy error in `qt_current_size_slider.py` ([#9180](https://github.com/napari/napari/pull/9180))
- fix(typing): add typing and fix mypy error in `qt_edge_color.py` ([#9183](https://github.com/napari/napari/pull/9183))
- fix(typing): resolve mypy errors for `qt_widget_controls_base` ([#9185](https://github.com/napari/napari/pull/9185))
- Update `coverage`, `dask`, `hypothesis`, `imageio`, `matplotlib`, `platformdirs`, `tifffile`, `tqdm`, `virtualenv`, `xarray` ([#9194](https://github.com/napari/napari/pull/9194))
- [pre-commit.ci] pre-commit autoupdate ([#9197](https://github.com/napari/napari/pull/9197))
- Update dev dependencies of napari ([#9211](https://github.com/napari/napari/pull/9211))
- Add ``example`` to ``allowed_labels`` in ``check_labels`` job of ``label_and_milestone_checker.yml`` workflow ([#9214](https://github.com/napari/napari/pull/9214))
- TST: parameterizing with iterables is deprecated in pytest ([#9217](https://github.com/napari/napari/pull/9217))
- Make tensorstore optional dependency of `test_labels` again ([#9220](https://github.com/napari/napari/pull/9220))
- Remove unnecessary ``FutureWarning`` ignore for ``test_layers_save_svg`` ([#9225](https://github.com/napari/napari/pull/9225))
- Disable part of test matrix to increase runner availability during sprints/hackathon ([#9226](https://github.com/napari/napari/pull/9226))
- fix(typing): add typing and fix mypy error in `qt_brush_size_slider.py` ([#9238](https://github.com/napari/napari/pull/9238))
- fix(typing): add typing and fix mypy error in `qt_color_mode_combobox.py` ([#9239](https://github.com/napari/napari/pull/9239))
- fix(typing): add typing and fix mypy error in `_evented_dict.py` ([#9240](https://github.com/napari/napari/pull/9240))
- Disable interaction with vispy.gloo in test_vispy_labels_polygon_overlay ([#9264](https://github.com/napari/napari/pull/9264))
- ci(dependabot): bump the actions group across 1 directory with 11 updates ([#9265](https://github.com/napari/napari/pull/9265))
- Remove missing translations GH action ([#9266](https://github.com/napari/napari/pull/9266))
- Asynchronous loading text fix ([#9267](https://github.com/napari/napari/pull/9267))
- Pin octokit to tag, not use main branch ([#9268](https://github.com/napari/napari/pull/9268))
- Fix typing problem by provide strict version of _BaseEventedItemModel.getItem ([#9272](https://github.com/napari/napari/pull/9272))
- Fix test failures when running napari in tiling window managers by forcing the screenshot size. ([#9284](https://github.com/napari/napari/pull/9284))
- Enable coverage annotation in PR changes view ([#9288](https://github.com/napari/napari/pull/9288))
- Update `certifi`, `hypothesis`, `pandas`, `platformdirs`, `tqdm`, `virtualenv` ([#9295](https://github.com/napari/napari/pull/9295))
- [pre-commit.ci] pre-commit autoupdate ([#9303](https://github.com/napari/napari/pull/9303))
- Add plugin-defined settings through `ConfigurationContribution`s ([#9308](https://github.com/napari/napari/pull/9308))
- Simplify tox configuration ([#9309](https://github.com/napari/napari/pull/9309))
- Update latlon with map example to follow PEP8 ([#9312](https://github.com/napari/napari/pull/9312))
- Remove `make_napari_viewer` from `test_vispy_labels_polygon_overlay` ([#9314](https://github.com/napari/napari/pull/9314))
- Scene model ([#9323](https://github.com/napari/napari/pull/9323))
- Revert "Disable part of test matrix to increase runner availability during sprints/hackathon (#9226)" ([#9348](https://github.com/napari/napari/pull/9348))
- Drop colormap translation dictionaries ([#9358](https://github.com/napari/napari/pull/9358))
- Use LF for all files in gitattributes ([#9359](https://github.com/napari/napari/pull/9359))
- Change tox and codecov configuration to simplify local reports ([#9368](https://github.com/napari/napari/pull/9368))
- Update `coverage`, `hypothesis`, `platformdirs`, `pydantic-settings`, `tensorstore`, `virtualenv` ([#9380](https://github.com/napari/napari/pull/9380))


## 28 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Aniket](https://github.com/napari/napari/commits?author=Aniketsy) - @Aniketsy
- [Anwai Archit](https://github.com/napari/napari/commits?author=anwai98) - @anwai98
- [Arne Defauw](https://github.com/napari/napari/commits?author=ArneDefauw) - @ArneDefauw +
- [Aroj Hada](https://github.com/napari/napari/commits?author=ArozHada) - @ArozHada +
- [BadPrograms](https://github.com/napari/napari/commits?author=BadPrograms) - @BadPrograms +
- [Bas Bloemsaat](https://github.com/napari/napari/commits?author=basbloemsaat) - @basbloemsaat +
- [Carlos Mario Rodriguez Reza](https://github.com/napari/napari/commits?author=carlosmariorr) - @carlosmariorr
- [Christophe Creeten](https://github.com/napari/napari/commits?author=ccreeten) - @ccreeten +
- [Edouard Coussoux](https://github.com/napari/napari/commits?author=ecoussoux-ansys) - @ecoussoux-ansys +
- [Filippo  Maria Castelli, PhD](https://github.com/napari/napari/commits?author=filippocastelli) - @filippocastelli +
- [girochat](https://github.com/napari/napari/commits?author=girochat) - @girochat +
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Jacopo Abramo](https://github.com/napari/napari/commits?author=jacopoabramo) - @jacopoabramo
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) ([docs](https://github.com/napari/docs/commits?author=jni))  - @jni
- [Kamil Kania](https://github.com/napari/napari/commits?author=Grzyb33k) - @Grzyb33k +
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) ([docs](https://github.com/napari/docs/commits?author=brisvag))  - @brisvag
- [Margot Chazotte](https://github.com/napari/napari/commits?author=MargotCh) - @MargotCh
- [Matthias Schabel](https://github.com/napari/napari/commits?author=matthiasschabel) - @matthiasschabel +
- [michalslabs](https://github.com/napari/napari/commits?author=michalslabs) ([docs](https://github.com/napari/docs/commits?author=michalslabs))  - @michalslabs +
- [Mridul Seth](https://github.com/napari/napari/commits?author=MridulS) - @MridulS +
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Revathy Venugopal](https://github.com/napari/napari/commits?author=Revathyvenugopal162) - @Revathyvenugopal162 +
- [Sara Czasak](https://github.com/napari/docs/commits?author=sara-czasak) - @sara-czasak +
- [Sébastien Morais](https://github.com/napari/napari/commits?author=SMoraisAnsys) - @SMoraisAnsys +
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko
- [Venkateswarlu Nagineni](https://github.com/napari/napari/commits?author=VenkateswarluNagineni) - @VenkateswarluNagineni +
- [Wouter-Michiel Vierdag](https://github.com/napari/docs/commits?author=melonora) - @melonora
- [Zuzana Čočková](https://github.com/napari/napari/commits?author=cockovaz) - @cockovaz

## 24 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Aniket](https://github.com/napari/napari/commits?author=Aniketsy) - @Aniketsy
- [Anwai Archit](https://github.com/napari/napari/commits?author=anwai98) - @anwai98
- [arbor](https://github.com/napari/docs/commits?author=arbormoss) - @arbormoss
- [Arne Defauw](https://github.com/napari/napari/commits?author=ArneDefauw) - @ArneDefauw +
- [Carlos Mario Rodriguez Reza](https://github.com/napari/napari/commits?author=carlosmariorr) - @carlosmariorr
- [Carol Willing](https://github.com/napari/docs/commits?author=willingc) - @willingc
- [Draga Doncila Pop](https://github.com/napari/docs/commits?author=DragaDoncila) - @DragaDoncila
- [Filippo  Maria Castelli, PhD](https://github.com/napari/napari/commits?author=filippocastelli) - @filippocastelli +
- [girochat](https://github.com/napari/napari/commits?author=girochat) - @girochat +
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Ian Hunt-Isaak](https://github.com/napari/docs/commits?author=ianhi) - @ianhi
- [Jacopo Abramo](https://github.com/napari/napari/commits?author=jacopoabramo) - @jacopoabramo
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) ([docs](https://github.com/napari/docs/commits?author=jni))  - @jni
- [Justus Magin](https://github.com/napari/docs/commits?author=keewis) - @keewis
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) ([docs](https://github.com/napari/docs/commits?author=brisvag))  - @brisvag
- [Margot Chazotte](https://github.com/napari/napari/commits?author=MargotCh) - @MargotCh
- [Matthias Schabel](https://github.com/napari/napari/commits?author=matthiasschabel) - @matthiasschabel +
- [Maxime Rey](https://github.com/napari/docs/commits?author=MaxJPRey) - @MaxJPRey
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Samuel Le Meur-Diebolt](https://github.com/napari/docs/commits?author=sdiebolt) - @sdiebolt
- [Sara Czasak](https://github.com/napari/docs/commits?author=sara-czasak) - @sara-czasak +
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko
- [Wouter-Michiel Vierdag](https://github.com/napari/docs/commits?author=melonora) - @melonora
- [Zuzana Čočková](https://github.com/napari/napari/commits?author=cockovaz) - @cockovaz
