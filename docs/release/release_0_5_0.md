# napari 0.5.0

*Note: these release notes are still in draft while 0.5.0 is in alpha/release
candidate testing.*

We're happy to announce the release of napari 0.5.0!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for exploring, annotating, and analyzing multi-dimensional
images. It's built on top of Qt (for the GUI), VisPy (for performant GPU-based
rendering), and the scientific Python stack (NumPy, SciPy, and friends).


For more information, examples, and documentation, please visit our website:
https://napari.org/

## Highlights

napari 0.5.0 is the beginning of an architectural overhaul of napari. The
architecture improvements, which are still ongoing, enable more responsive
asynchronous loading when slicing layers or panning and zooming in multiscale
2D layers ([#5816](https://github.com/napari/napari/pull/5816)).

Other architectural changes, refactoring napari on top of
[app-model](https://app-model.readthedocs.io/en/latest/), have enabled us to
(finally 😅) implement [NAP-6](nap-6-contributable-menus), which allows
plugins to organize their commands in defined menus in the napari menubar
and application. Please read [NAP-6](nap-6-contributable-menus) for all the
juicy details, including how to request more menus if the existing ones don't
meet your needs. 📋 ([#7011](https://github.com/napari/napari/pull/7011))

Another important development for plugins is that we have added fields for
axis names and physical units in layers
([#6979](https://github.com/napari/napari/pull/6979)). If you implement a
reader plugin, you can now specify the names of the axes in the data that you
are reading in, and the physical units of the scale and other transformations.
Currently, napari is *not* using this information, but we will in upcoming
versions, so plugins should start providing this information if they have it.

There's plenty of new features, too, including a polygon drawing tool when
painting labels ([#5806](https://github.com/napari/napari/pull/5806)),
pinch-to-zoom ([#5859](https://github.com/napari/napari/pull/5859)), better
ways to show/hide individual layers when exploring your data
([#5574](https://github.com/napari/napari/pull/5574))
([#5618](https://github.com/napari/napari/pull/5618)), and more:
Over 20 new features in all and over 100 bug fixes and improvements!
Please see below for the full list of changes since 0.4.19.

## New Features

- Add layer slicer base class for async slicing ([napari/napari#5170](https://github.com/napari/napari/pull/5170))
- Feature: add layer contextual menu to hide not-selected layers ([napari/napari#5574](https://github.com/napari/napari/pull/5574))
- Feature: alt-click visibility eye to toggle show just that layer (hide others) ([napari/napari#5618](https://github.com/napari/napari/pull/5618))
- Feature: Add action to set current label to background (with keybinding) ([napari/napari#5672](https://github.com/napari/napari/pull/5672))
- Use Dims margin in layer slicing code ([napari/napari#5697](https://github.com/napari/napari/pull/5697))
- Changing brush size with mouse movement while holding specified modifiers ([napari/napari#5753](https://github.com/napari/napari/pull/5753))
- Feature: polygon drawing in the Labels layer ([napari/napari#5806](https://github.com/napari/napari/pull/5806))
- Replace old async loading with new approach ([napari/napari#5816](https://github.com/napari/napari/pull/5816))
- Enable pinch-to-zoom with vispy 0.13+ ([napari/napari#5859](https://github.com/napari/napari/pull/5859))
- Keep shading light for Surface fixed relative to camera ([napari/napari#5893](https://github.com/napari/napari/pull/5893))
- Use Request/Response pattern for Vectors layer ([napari/napari#5918](https://github.com/napari/napari/pull/5918))
- Lock dimensions / axes while rolling ([napari/napari#5986](https://github.com/napari/napari/pull/5986))
- Added support for features in surface layers ([napari/napari#6515](https://github.com/napari/napari/pull/6515))
- Add creating image from clipboard ([napari/napari#6532](https://github.com/napari/napari/pull/6532))
- Add viewer keybinds to select & show only next/prev layer and to toggle visibility of unselected ([napari/napari#6590](https://github.com/napari/napari/pull/6590))
- Show `About napari` action on macOS application menu ([napari/napari#6666](https://github.com/napari/napari/pull/6666))
- Add points/shapes highlight color setting to Appereance settings and preference page ([napari/napari#6689](https://github.com/napari/napari/pull/6689))
- Include features index as key in FormatStringEncoding ([napari/napari#6703](https://github.com/napari/napari/pull/6703))
- Reset all dims to be rollable ([napari/napari#6797](https://github.com/napari/napari/pull/6797))
- implement copying spatial information via clipboard ([napari/napari#6864](https://github.com/napari/napari/pull/6864))
- Add `axis_labels` and `units` to layers and transforms  ([napari/napari#6979](https://github.com/napari/napari/pull/6979))
- Alpha implementation of NAP-6 ([napari/napari#7011](https://github.com/napari/napari/pull/7011))
- Screenshot without margins ([napari/napari#6730](https://github.com/napari/napari/pull/6730))

## Improvements

- use app-model for file menu ([napari/napari#4865](https://github.com/napari/napari/pull/4865))
- Show platform specific shortcut while editing. ([napari/napari#5064](https://github.com/napari/napari/pull/5064))
- Add secondary keybindings to restore mnemonic (non-numeric) shortcuts in layers ([napari/napari#5155](https://github.com/napari/napari/pull/5155))
- Add loading layer UI indicator ([napari/napari#5342](https://github.com/napari/napari/pull/5342))
- Clean up layer slicer before integration with viewer ([napari/napari#5435](https://github.com/napari/napari/pull/5435))
- Thick Slices (Dims  as nD-box instead of nD-point) ([napari/napari#5522](https://github.com/napari/napari/pull/5522))
- Add `font-size` to theme ([napari/napari#5607](https://github.com/napari/napari/pull/5607))
- Feature: Background color swapping for the Label layer (extends #5672) ([napari/napari#5744](https://github.com/napari/napari/pull/5744))
- Improve error message when user passes nonexistent plugin ([napari/napari#6016](https://github.com/napari/napari/pull/6016))
- Reduce comparison in evented model ([napari/napari#6075](https://github.com/napari/napari/pull/6075))
- Expose theme `font_size` as an `Appearance` setting ([napari/napari#6113](https://github.com/napari/napari/pull/6113))
- ENH Adds `LayerList` context ([napari/napari#6165](https://github.com/napari/napari/pull/6165))
- Add layer name to QFileDialog when only one layer is selected for saving. ([napari/napari#6360](https://github.com/napari/napari/pull/6360))
- Use blobs instead of random integers  ([napari/napari#6527](https://github.com/napari/napari/pull/6527))
- Show notification when using shortcut to change current selected label to largest used label plus one ([napari/napari#6546](https://github.com/napari/napari/pull/6546))
- Keep vertex selection after shape drawing finishes ([napari/napari#6640](https://github.com/napari/napari/pull/6640))
- Add GL_MAX_3D_TEXTURE_SIZE to `napari --info` ([napari/napari#6645](https://github.com/napari/napari/pull/6645))
- [ENH] use imageio.v3 for builtins io imread ([napari/napari#6677](https://github.com/napari/napari/pull/6677))
- Make new labels dtype configurable ([napari/napari#6695](https://github.com/napari/napari/pull/6695))
- Add `Optional` section to napari info with numba and triangle ([napari/napari#6710](https://github.com/napari/napari/pull/6710))
- [ENH] Add `repeatable` kwarg to register_viewer_action and use it for slider left/right keybind ([napari/napari#6769](https://github.com/napari/napari/pull/6769))
- "Shapes to Labels", "(float)Image to Labels": Don't pop layer being converted, append new one ([napari/napari#6859](https://github.com/napari/napari/pull/6859))
- [enh] Transform mode: shift to snap layer rotation to 45 deg ([napari/napari#6948](https://github.com/napari/napari/pull/6948))
- [UX/UI] flip the default for the reader plugin dialog to *not* have the Remember box checked ([napari/napari#7016](https://github.com/napari/napari/pull/7016))
- Extend "No Qt bindings found" error message with details about conda ([napari/napari#6095](https://github.com/napari/napari/pull/6095))
- Add convenience input validation for Labels colormaps ([napari/napari#7025](https://github.com/napari/napari/pull/7025))
- [UI/UX] Updated polygon button icon for Shapes & Labels regular polygon tool ([napari/napari#7019](https://github.com/napari/napari/pull/7019))

## Performance

- Do not copy label data when not necessary ([napari/napari#5542](https://github.com/napari/napari/pull/5542))
- Throttle mouse move event to fix high-polling-rate input ([napari/napari#5710](https://github.com/napari/napari/pull/5710))
- Speed up symbols validation in points layers ([napari/napari#6277](https://github.com/napari/napari/pull/6277))
- Making Tracks layers creation and update faster ([napari/napari#6671](https://github.com/napari/napari/pull/6671))
- Making Points layer creation and update faster ([napari/napari#6727](https://github.com/napari/napari/pull/6727))
- Remove unnecessary early call to np.asarray before thick slicing ([napari/napari#6735](https://github.com/napari/napari/pull/6735))
- perf: remove extra highlight calls ([napari/napari#6893](https://github.com/napari/napari/pull/6893))

## Bug Fixes

- Quick silo dev version settings in a dev sub-directory ([napari/napari#5322](https://github.com/napari/napari/pull/5322))
- Fix conda avaliability check ([napari/napari#5496](https://github.com/napari/napari/pull/5496))
- Bugfix: PR build of docs doesn't use proper napari versioning for substitutions ([napari/napari#5557](https://github.com/napari/napari/pull/5557))
- fix various keybinding/shortcut bugs ([napari/napari#5604](https://github.com/napari/napari/pull/5604))
- Bugfix (macOS): Remove PYTHONEXECUTABLE from `env` for conda installs ([napari/napari#5622](https://github.com/napari/napari/pull/5622))
- Fix waiting for multiple signals in threading progress bar test ([napari/napari#5637](https://github.com/napari/napari/pull/5637))
- Update the sliders `axis_label` widget to be a `QElidingLineEdit` instance ([napari/napari#5665](https://github.com/napari/napari/pull/5665))
- Fix usage of closed interval dims and unify extents calculations ([napari/napari#5751](https://github.com/napari/napari/pull/5751))
- Add aditional guard at the end of `test_worker_may_exceed_total` ([napari/napari#5781](https://github.com/napari/napari/pull/5781))
- Return full colormap dict in get_state ([napari/napari#5782](https://github.com/napari/napari/pull/5782))
- Add test coverage for async slicing of points and fix rounding bug ([napari/napari#5783](https://github.com/napari/napari/pull/5783))
- Add pydantic<2 constrains to plugin install ([napari/napari#5785](https://github.com/napari/napari/pull/5785))
- Readd exception to event proxy ([napari/napari#5797](https://github.com/napari/napari/pull/5797))
- Bugfix: do not allow drawing while adjusting the brush size with the mouse ([napari/napari#5842](https://github.com/napari/napari/pull/5842))
- Amend `pydantic` constraints in the plugin manager ([napari/napari#5851](https://github.com/napari/napari/pull/5851))
- Bugfix: Ensure bgcolor is set in __init__ of VispyCanvas ([napari/napari#5970](https://github.com/napari/napari/pull/5970))
- Make sure `open_sample` respects `reader_plugin` for sample URIs ([napari/napari#5971](https://github.com/napari/napari/pull/5971))
- Async refresh when experimental setting is on ([napari/napari#6008](https://github.com/napari/napari/pull/6008))
- Add validation logic for `Dims.last_used` to prevent slider selection errors when rolling dims ([napari/napari#6024](https://github.com/napari/napari/pull/6024))
- Update layer's loaded state before vispy and thumbnail ([napari/napari#6026](https://github.com/napari/napari/pull/6026))
- Fix string list JSON formatting ([napari/napari#6033](https://github.com/napari/napari/pull/6033))
- Remove 3D multiscale warning ([napari/napari#6070](https://github.com/napari/napari/pull/6070))
- A few small improvements to async slicing ([napari/napari#6080](https://github.com/napari/napari/pull/6080))
- Add toggle status view menu items ([napari/napari#6137](https://github.com/napari/napari/pull/6137))
- Fix PR html stripping workflow ([napari/napari#6139](https://github.com/napari/napari/pull/6139))
- Add test on top of #6142 ([napari/napari#6167](https://github.com/napari/napari/pull/6167))
- Bugfix: ensure thumbnail represents canvas when multiscale ([napari/napari#6200](https://github.com/napari/napari/pull/6200))
- Fix (N>4)D shapes. ([napari/napari#6210](https://github.com/napari/napari/pull/6210))
- Fix typing checks in PRs ([napari/napari#6230](https://github.com/napari/napari/pull/6230))
- convert Color to string ([napari/napari#6243](https://github.com/napari/napari/pull/6243))
- Fix link to artifacts in update dependecies comment ([napari/napari#6270](https://github.com/napari/napari/pull/6270))
- Fix setting shortcuts with modifier keys and only one modifier key as a shortcut on Windows/Linux ([napari/napari#6330](https://github.com/napari/napari/pull/6330))
- Pass key event from Main window to our internal mechanism ([napari/napari#6419](https://github.com/napari/napari/pull/6419))
- Restore old breakpointhook after console import in tests fixture ([napari/napari#6436](https://github.com/napari/napari/pull/6436))
- FIX: Remove `None` default from `_remove_dock_widget` ([napari/napari#6481](https://github.com/napari/napari/pull/6481))
- Fix crash on python -m napari ([napari/napari#6484](https://github.com/napari/napari/pull/6484))
- Bugfix: ensure gamma and opacity are floats ([napari/napari#6498](https://github.com/napari/napari/pull/6498))
- Restore quit shortcut ([napari/napari#6526](https://github.com/napari/napari/pull/6526))
- Fix contrast limits for single layer numpy case. ([napari/napari#6535](https://github.com/napari/napari/pull/6535))
- Fix check if plugin is available from conda ([napari/napari#6545](https://github.com/napari/napari/pull/6545))
- Set default dtype for empty `_ImageSliceResponse` ([napari/napari#6552](https://github.com/napari/napari/pull/6552))
- Ensure consistent layer tooltip ([napari/napari#6589](https://github.com/napari/napari/pull/6589))
- Make Shift-Up/Down in layer list expand and contract selection ([napari/napari#6606](https://github.com/napari/napari/pull/6606))
- Remove scaling of highlight width, fix showing shapes for uneven coordinates ([napari/napari#6629](https://github.com/napari/napari/pull/6629))
- Fix decomposition function to properly work with more than 2x2 matrices ([napari/napari#6636](https://github.com/napari/napari/pull/6636))
- Remove if that prevents from setting gamma in constructor ([napari/napari#6650](https://github.com/napari/napari/pull/6650))
- [Bugfix] update selection ctx keys before showing LayerList context menu ([napari/napari#6664](https://github.com/napari/napari/pull/6664))
- Fix offset in rendering of `TransformBox` of image/labels layers ([napari/napari#6679](https://github.com/napari/napari/pull/6679))
- Exclude size and symbol pts attributes from linking, because they depend on number of points ([napari/napari#6687](https://github.com/napari/napari/pull/6687))
- Fix shape layer infinite edge bug ([napari/napari#6706](https://github.com/napari/napari/pull/6706))
- [Dockerfile] update pip before installing napari ([napari/napari#6728](https://github.com/napari/napari/pull/6728))
- Fix npe1 samples menu building ([napari/napari#6739](https://github.com/napari/napari/pull/6739))
- [Maint, CI] Fix upgrade_test_constraints.yml to use pyproject.toml ([napari/napari#6749](https://github.com/napari/napari/pull/6749))
- Update description of `a`, `shift-a` points keybinds to reflect toggle ([napari/napari#6750](https://github.com/napari/napari/pull/6750))
- [Dockerfile] add missing opengl and x11 packages to the base image ([napari/napari#6754](https://github.com/napari/napari/pull/6754))
- Keep `qtpy` in headless tests and fix resulting failure ([napari/napari#6764](https://github.com/napari/napari/pull/6764))
- Fix sync slicing of not yet visible layers ([napari/napari#6766](https://github.com/napari/napari/pull/6766))
- Remove compression scheme when saving boolean arrays as tif  ([napari/napari#6807](https://github.com/napari/napari/pull/6807))
- Solving visual glitch when displaying tracks with missing timepoints ([napari/napari#6808](https://github.com/napari/napari/pull/6808))
- Fix `napari.utils.misc.is_iterable` function ([napari/napari#6811](https://github.com/napari/napari/pull/6811))
- Remove redundant `_view_actions.py` ([napari/napari#6821](https://github.com/napari/napari/pull/6821))
- refresh when canvas_size_limits are changed ([napari/napari#6834](https://github.com/napari/napari/pull/6834))
- Fix selection size when canvas limits are set for Points ([napari/napari#6853](https://github.com/napari/napari/pull/6853))
- Ensure bounding_box lines stay up to date between 2D and 3D ([napari/napari#6855](https://github.com/napari/napari/pull/6855))
- Fix zarr reading with unrelated files ([napari/napari#6857](https://github.com/napari/napari/pull/6857))
- Two bug fixes concerning 4D surfaces, ie surfaces with (t, z, y, x) vertices ([napari/napari#6874](https://github.com/napari/napari/pull/6874))
- [bugfix] Drop if guard on notification_manager to enable show_info from Jupyter ([napari/napari#6882](https://github.com/napari/napari/pull/6882))
- [bugfix] Warn if float image data being saved to non-tiff ([napari/napari#6884](https://github.com/napari/napari/pull/6884))
- Disable copying layer transform metadata when selecting multiple layers ([napari/napari#6887](https://github.com/napari/napari/pull/6887))
- Fix use of scaling in vispy points ([napari/napari#6894](https://github.com/napari/napari/pull/6894))
- Fix point highlight thickness ([napari/napari#6896](https://github.com/napari/napari/pull/6896))
- Fix shapes mouse click and double click behavior on partial shapes ([napari/napari#6912](https://github.com/napari/napari/pull/6912))
- Again fix translate of overlays (this time with tests) ([napari/napari#6927](https://github.com/napari/napari/pull/6927))
- Add warning notification when connectivity errors occur in when opening the plugin manager ([napari/napari#6931](https://github.com/napari/napari/pull/6931))
- Fix array data copy behavior for numpy 1 and 2 consistency ([napari/napari#6932](https://github.com/napari/napari/pull/6932))
- [bugfix] Swap digit and `backspace` for Shapes & Points `delete_selected` keybinds ([napari/napari#6933](https://github.com/napari/napari/pull/6933))
- Fix callback for `File -> Open Folder...` action ([napari/napari#6935](https://github.com/napari/napari/pull/6935))
- fix `create_func` to respect `rename_argument` decorator ([napari/napari#6970](https://github.com/napari/napari/pull/6970))
- Do not crash napari viewer if error happen on open file via cli ([napari/napari#6971](https://github.com/napari/napari/pull/6971))
- Fix viewer scale bar color update ([napari/napari#6989](https://github.com/napari/napari/pull/6989))
- Remove NumPy 2 pin, fix direct colormap with keys outside data dtype ([napari/napari#6998](https://github.com/napari/napari/pull/6998))
- Fix switching from 2d to 3d with 2d points ([napari/napari#7004](https://github.com/napari/napari/pull/7004))
- Fix importerror and message for lxml_html_clean ([napari/napari#7017](https://github.com/napari/napari/pull/7017))

## API Changes

- Add .to_rgb_dict() to Theme class. ([napari/napari#4759](https://github.com/napari/napari/pull/4759))
- Thick Slices (Dims  as nD-box instead of nD-point) ([napari/napari#5522](https://github.com/napari/napari/pull/5522))
- Lock dimensions / axes while rolling ([napari/napari#5986](https://github.com/napari/napari/pull/5986))
- Remove deprecated code from Labels layer ([napari/napari#6641](https://github.com/napari/napari/pull/6641))

## Deprecations

- MAINT: Remove unused function. ([napari/napari#5041](https://github.com/napari/napari/pull/5041))
- MAINT: remove deprecated Alias. ([napari/napari#5043](https://github.com/napari/napari/pull/5043))
- Fix typing in _app_model ([napari/napari#6059](https://github.com/napari/napari/pull/6059))
- Rename `edge_*` attributes and references to `border_*` on points layer ([napari/napari#6402](https://github.com/napari/napari/pull/6402))
- Add deprecation message to CallDefault function partly resolves issue#6257 ([napari/napari#6901](https://github.com/napari/napari/pull/6901))

## Build Tools

- ci(dependabot): bump WebFreak001/deploy-nightly from 1.1.0 to 1.2.0 ([napari/napari#5159](https://github.com/napari/napari/pull/5159))
- ci(dependabot): bump convictional/trigger-workflow-and-wait from 1.6.1 to 1.6.4 ([napari/napari#5293](https://github.com/napari/napari/pull/5293))
- ci(dependabot): bump bruceadams/get-release from 1.2.3 to 1.3.2 ([napari/napari#5294](https://github.com/napari/napari/pull/5294))
- ci(dependabot): bump convictional/trigger-workflow-and-wait from 1.6.4 to 1.6.5 ([napari/napari#5384](https://github.com/napari/napari/pull/5384))
- ci(dependabot): bump WebFreak001/deploy-nightly from 1.2.0 to 2.0.0 ([napari/napari#5385](https://github.com/napari/napari/pull/5385))
- ci(dependabot): bump docker/build-push-action from 3 to 4 ([napari/napari#5523](https://github.com/napari/napari/pull/5523))
- ci(dependabot): bump toshimaru/auto-author-assign from 1.6.1 to 1.6.2 ([napari/napari#5524](https://github.com/napari/napari/pull/5524))
- fix various keybinding/shortcut bugs ([napari/napari#5604](https://github.com/napari/napari/pull/5604))
- ci(dependabot): bump peter-evans/create-pull-request from 4 to 5 ([napari/napari#5792](https://github.com/napari/napari/pull/5792))
- ci(dependabot): bump actions/setup-python from 2 to 4 ([napari/napari#6201](https://github.com/napari/napari/pull/6201))
- ci(dependabot): bump docker/login-action from 2.1.0 to 3.0.0 ([napari/napari#6263](https://github.com/napari/napari/pull/6263))
- ci(dependabot): bump actions/checkout from 2 to 4 ([napari/napari#6264](https://github.com/napari/napari/pull/6264))
- ci(dependabot): bump docker/build-push-action from 4 to 5 ([napari/napari#6280](https://github.com/napari/napari/pull/6280))
- ci(dependabot): bump docker/metadata-action from 4 to 5 ([napari/napari#6282](https://github.com/napari/napari/pull/6282))

## Documentation

- DOCS: Consolidate Makefiles ([napari/napari#5011](https://github.com/napari/napari/pull/5011))
- Move docs to separate repo ([napari/napari#5216](https://github.com/napari/napari/pull/5216))
- DOC Fix actions file docstrings ([napari/napari#5285](https://github.com/napari/napari/pull/5285))
- Update build_docs workflow ([napari/napari#5405](https://github.com/napari/napari/pull/5405))
- Bugfix: PR build of docs doesn't use proper napari versioning for substitutions ([napari/napari#5557](https://github.com/napari/napari/pull/5557))
- Add link to napari/docs in Readme file.  ([napari/napari#5814](https://github.com/napari/napari/pull/5814))
- Fix typing in layers.labels ([napari/napari#5858](https://github.com/napari/napari/pull/5858))
- DOC: fix incorrect doc in layer-base ([napari/napari#5996](https://github.com/napari/napari/pull/5996))
- Add vortex optical flow example ([napari/napari#6041](https://github.com/napari/napari/pull/6041))
- DOC Amend `open_sample` docstring str->URI ([napari/napari#6108](https://github.com/napari/napari/pull/6108))
- DOC: misc syntax/typos ([napari/napari#6387](https://github.com/napari/napari/pull/6387))
- DOC: misc fixes ([napari/napari#6429](https://github.com/napari/napari/pull/6429))
- Change `vortex.py` example to enable its page build in the documentation ([napari/napari#6475](https://github.com/napari/napari/pull/6475))
- Fix generation of layer creation functions docstrings ([napari/napari#6558](https://github.com/napari/napari/pull/6558))
- Update docs constraints for napari-sphinx-theme 0.3.0 ([napari/napari#6598](https://github.com/napari/napari/pull/6598))
- Update docstrings in `colormap_utils` for seed parameter effective range ([napari/napari#6688](https://github.com/napari/napari/pull/6688))
- Update shapes.py add_rectangle and add_ellipse docstrings ([napari/napari#6704](https://github.com/napari/napari/pull/6704))
- Update docstring for _get_console method of QtViewer class ([napari/napari#6723](https://github.com/napari/napari/pull/6723))
- DOC Explicitly describe use of `show` in `make_napari_viewer` ([napari/napari#6724](https://github.com/napari/napari/pull/6724))
- DOC Add info to `make_napari_viewer` docstring ([napari/napari#6774](https://github.com/napari/napari/pull/6774))
- Expose NotebookScreenshot docstring ([napari/napari#6833](https://github.com/napari/napari/pull/6833))
- DOC Update `_mock_app` docstring ([napari/napari#6903](https://github.com/napari/napari/pull/6903))
- DOC Update menu action file docstrings ([napari/napari#6904](https://github.com/napari/napari/pull/6904))
- Front-load core devs in citation.cff, sorted by commits ([napari/napari#6949](https://github.com/napari/napari/pull/6949))
- Update CITATION.cff with contributors for 0.5.0 ([napari/napari#6958](https://github.com/napari/napari/pull/6958))
- Remove examples from docs repo and use main repo instead ([napari/docs#1](https://github.com/napari/docs/pull/1))
- Add build_docs action to PRs ([napari/docs#6](https://github.com/napari/docs/pull/6))
- Fix examples path in build_docs PR workflow ([napari/docs#8](https://github.com/napari/docs/pull/8))
- Updated issue and PR templates for this repo ([napari/docs#36](https://github.com/napari/docs/pull/36))
- how to use annotation with create_widget ([napari/docs#68](https://github.com/napari/docs/pull/68))
- Fix docs deployment with gallery env variable ([napari/docs#70](https://github.com/napari/docs/pull/70))
- Switch from GabrielBB/xvfb-action to aganders3/headless-gui ([napari/docs#94](https://github.com/napari/docs/pull/94))
- Update deploy_docs.yml to use metadata to use proper napari version substitution ([napari/docs#99](https://github.com/napari/docs/pull/99))
- CircleCI setup for PR documentation previews ([napari/docs#104](https://github.com/napari/docs/pull/104))
- Change `CIRCLECI_TOKEN` to `GITHUB_TOKEN` in `circleci.yml`  workflow file.  ([napari/docs#108](https://github.com/napari/docs/pull/108))
- Documentation for alt-click visibility icon to show only that layer (napari/napari#5618) ([napari/docs#121](https://github.com/napari/docs/pull/121))
- Add pr dependency check ([napari/docs#124](https://github.com/napari/docs/pull/124))
- Layer documentation enhancements ([napari/docs#125](https://github.com/napari/docs/pull/125))
- Using Dask and Napari to view and process 100µm resolution human brain dataset ([napari/docs#132](https://github.com/napari/docs/pull/132))
- Fix CircleCI token name and remove outdated artifact action ([napari/docs#136](https://github.com/napari/docs/pull/136))
- Add instructions on how to check preview of built docs ([napari/docs#140](https://github.com/napari/docs/pull/140))
- Add documentation of udpate tokens for automated actions.  ([napari/docs#144](https://github.com/napari/docs/pull/144))
- Use constraints file when installing dependencies to build docs ([napari/docs#162](https://github.com/napari/docs/pull/162))
- Fix build and deploy workflow ([napari/docs#164](https://github.com/napari/docs/pull/164))
- Update README to display CZI logo for dark and light GitHub themes ([napari/docs#165](https://github.com/napari/docs/pull/165))
- Use constraints during build docs on circleCI ([napari/docs#167](https://github.com/napari/docs/pull/167))
- Fix closing of html comment in PR template ([napari/docs#168](https://github.com/napari/docs/pull/168))
- Add documentation for #5806 ([napari/docs#177](https://github.com/napari/docs/pull/177))
- Update Viewer tutorial for extra layer contextual menu visibility options (napari/#5574) ([napari/docs#183](https://github.com/napari/docs/pull/183))
- Use python version range instead of min version ([napari/docs#194](https://github.com/napari/docs/pull/194))
- Fix trailing whitespace with pre-commit ([napari/docs#198](https://github.com/napari/docs/pull/198))
- Add extra note for Windows and Make to avoid running `rm -rf C:\Users` ([napari/docs#201](https://github.com/napari/docs/pull/201))
- Plugin docs restructure of content ([napari/docs#203](https://github.com/napari/docs/pull/203))
- Add documentation how to avoid fickering windows when running test locally ([napari/docs#215](https://github.com/napari/docs/pull/215))
- Run PR depenecy check on every comment added to PR ([napari/docs#216](https://github.com/napari/docs/pull/216))
- Adds guide on CI setup for docs building and website deployment ([napari/docs#220](https://github.com/napari/docs/pull/220))
- Add TOML lexer to pygments set up ([napari/docs#229](https://github.com/napari/docs/pull/229))
- Remove items not relevant to documentation in PR template ([napari/docs#234](https://github.com/napari/docs/pull/234))
- [Content] Add docs for the new lock dims  of the roll button ([napari/docs#242](https://github.com/napari/docs/pull/242))
- Fix pydantic import ([napari/docs#255](https://github.com/napari/docs/pull/255))
- Add option to fail docs build on gallery example execution error ([napari/docs#256](https://github.com/napari/docs/pull/256))
- Uniform circleCI and build_docs workflows across repositories ([napari/docs#266](https://github.com/napari/docs/pull/266))
- Improve next steps part of installation guide ([napari/docs#275](https://github.com/napari/docs/pull/275))
- Re-apply: Image layers can't have converted data type ([napari/docs#276](https://github.com/napari/docs/pull/276))
- Add section on extending napari ([napari/docs#286](https://github.com/napari/docs/pull/286))
- Add env constraint to 'deploy_docs' workflow ([napari/docs#287](https://github.com/napari/docs/pull/287))
- Add to console details to "How to launch `napari`" ([napari/docs#292](https://github.com/napari/docs/pull/292))
- Add mp4 and png fallback to webm videos ([napari/docs#298](https://github.com/napari/docs/pull/298))
- Use reference labels instead of paths ([napari/docs#301](https://github.com/napari/docs/pull/301))
- Add theme page to 'how tos' ([napari/docs#302](https://github.com/napari/docs/pull/302))
- Expand headless env testing in "Test organization"  ([napari/docs#303](https://github.com/napari/docs/pull/303))
- Add/improve documentation about napari's software architecture ([napari/docs#304](https://github.com/napari/docs/pull/304))
- Replace references to 'edge' attributes with 'border' in Points docs ([napari/docs#306](https://github.com/napari/docs/pull/306))
- Add documentation for `New from clipboard` feature ([napari/docs#307](https://github.com/napari/docs/pull/307))
- NAP-6: Updates after discussion and review ([napari/docs#312](https://github.com/napari/docs/pull/312))
- Use tabs for the install as Python package guide ([napari/docs#313](https://github.com/napari/docs/pull/313))
- Fix execution of magicgui guide ([napari/docs#314](https://github.com/napari/docs/pull/314))
- Exclude inherited tqdm members from documentation ([napari/docs#316](https://github.com/napari/docs/pull/316))
- Re-organise 'Contributing' section ([napari/docs#318](https://github.com/napari/docs/pull/318))
- Update packaging guide by removing outdated `constructor` fork details ([napari/docs#319](https://github.com/napari/docs/pull/319))
- Update app-model documentation ([napari/docs#325](https://github.com/napari/docs/pull/325))
- Remove sphinx pin to rely on upstream constraints ([napari/docs#334](https://github.com/napari/docs/pull/334))
- Move note after screeenshot in install guide ([napari/docs#335](https://github.com/napari/docs/pull/335))
- Update links to napari hub guide ([napari/docs#336](https://github.com/napari/docs/pull/336))
- Fix broken links and references ([napari/docs#338](https://github.com/napari/docs/pull/338))
- Add announcement banner html to enable config ([napari/docs#341](https://github.com/napari/docs/pull/341))
- Add release notes for 0.4.19 ([napari/docs#346](https://github.com/napari/docs/pull/346))
- Update version switcher for 0.4.19 release ([napari/docs#347](https://github.com/napari/docs/pull/347))
- Add 0.4.19 to toc ([napari/docs#349](https://github.com/napari/docs/pull/349))
- Fix execution of magicgui guide (2) ([napari/docs#351](https://github.com/napari/docs/pull/351))
- Replace survey with help banner ([napari/docs#356](https://github.com/napari/docs/pull/356))
- [ENH] Add napari.utils.transforms to API docs ([napari/docs#359](https://github.com/napari/docs/pull/359))
- [Content] Add docs for napari/napari#6590 shift-option arrows to cycle through layers one at a time ([napari/docs#360](https://github.com/napari/docs/pull/360))
- Clarify optionality of type annotations for writing a plugin ([napari/docs#367](https://github.com/napari/docs/pull/367))
- Dynamicly calculate supported python version range ([napari/docs#368](https://github.com/napari/docs/pull/368))
- Add info on testing `QWidget` visibility ([napari/docs#370](https://github.com/napari/docs/pull/370))
- Summary of local setup for quickstart for devs ([napari/docs#372](https://github.com/napari/docs/pull/372))
- Add info about tests that require window focus and `pyautogui` permissions setup on macOS ([napari/docs#375](https://github.com/napari/docs/pull/375))
- Inlcude docstring of `make_napari_viewer` in `testing.md` ([napari/docs#378](https://github.com/napari/docs/pull/378))
- Add cross reference to other testing info in `testing.md` ([napari/docs#379](https://github.com/napari/docs/pull/379))
- Add note on using str instead of importing for napari type annot in plugins ([napari/docs#381](https://github.com/napari/docs/pull/381))
- Use intersphinx for magicgui objects in `magicgui.md` ([napari/docs#382](https://github.com/napari/docs/pull/382))
- Fix napari.org rendering ([napari/docs#386](https://github.com/napari/docs/pull/386))
- Fix doc preview in PR CI ([napari/docs#389](https://github.com/napari/docs/pull/389))
- Update `docs_deployment.md` and add paths to workflow ([napari/docs#390](https://github.com/napari/docs/pull/390))
- Fix ALL Sphinx warnings ([napari/docs#393](https://github.com/napari/docs/pull/393))
- Add note about autogeneration of plugin docs ([napari/docs#395](https://github.com/napari/docs/pull/395))
- Add page on `magicgui` type registration ([napari/docs#399](https://github.com/napari/docs/pull/399))
- Minor update to instructions for updating tokens ([napari/docs#401](https://github.com/napari/docs/pull/401))
- Fix typo in `app_model.md` ([napari/docs#402](https://github.com/napari/docs/pull/402))
- Update `app-model` doc with new information about `_mock_app` fixture ([napari/docs#403](https://github.com/napari/docs/pull/403))
- Fixes display of inherited members of classes ([napari/docs#404](https://github.com/napari/docs/pull/404))
- Improve our 'Creating widgets' section ([napari/docs#407](https://github.com/napari/docs/pull/407))
- Fix broken magicgui and app-model docs links ([napari/docs#410](https://github.com/napari/docs/pull/410))
- Add Python resources to Installation tutorial ([napari/docs#411](https://github.com/napari/docs/pull/411))
- Update IFP rep on the SC to be Kyle and not Nick ([napari/docs#412](https://github.com/napari/docs/pull/412))
- [Content] clarify Image to labels, Labels to Image, and add docs for shapes to labels behavior ([napari/docs#414](https://github.com/napari/docs/pull/414))
- Update where app-model actions/providers/processors live in codebase  ([napari/docs#416](https://github.com/napari/docs/pull/416))
- Update conda section of install docs ([napari/docs#417](https://github.com/napari/docs/pull/417))
- MacOS -> macOS ([napari/docs#418](https://github.com/napari/docs/pull/418))
- Replace use of properties with features ([napari/docs#425](https://github.com/napari/docs/pull/425))
- DOC Update finding submenu action in app-model ([napari/docs#426](https://github.com/napari/docs/pull/426))

## Other Pull Requests

- Add tests to cover slicing behavior when changing layers and data ([napari/napari#4819](https://github.com/napari/napari/pull/4819))
- Add examples to remote sample data & synthetic tests [for async work] ([napari/napari#4987](https://github.com/napari/napari/pull/4987))
- Use app model for plugins menu ([napari/napari#4991](https://github.com/napari/napari/pull/4991))
- MAINT: Misc unused variables and import. ([napari/napari#5051](https://github.com/napari/napari/pull/5051))
- Use same name in yml file and test name. ([napari/napari#5065](https://github.com/napari/napari/pull/5065))
- MAINT: Remove QtStateButton, marked for removal in 0.4.14 ([napari/napari#5066](https://github.com/napari/napari/pull/5066))
- Update config directory paths for perfmon tools ([napari/napari#5081](https://github.com/napari/napari/pull/5081))
- Use app-model keybindings internally ([napari/napari#5103](https://github.com/napari/napari/pull/5103))
- Ignore tags directory generated by Sphinx build ([napari/napari#5104](https://github.com/napari/napari/pull/5104))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5105](https://github.com/napari/napari/pull/5105))
- Clarify package installer interface with abstract base class, and Pip/Conda subclasses (continued) ([napari/napari#5124](https://github.com/napari/napari/pull/5124))
- MAINT: comment out macos briefcase bundle ([napari/napari#5144](https://github.com/napari/napari/pull/5144))
- Use nightly.link to add comment to docs artifacts on PRs ([napari/napari#5148](https://github.com/napari/napari/pull/5148))
- Attempt to fix benchmark failing. ([napari/napari#5175](https://github.com/napari/napari/pull/5175))
- MAINT: Use positional only to make code a bit more idiomatic. ([napari/napari#5179](https://github.com/napari/napari/pull/5179))
- Update vendoring tool to check on matplotlib colormap ([napari/napari#5181](https://github.com/napari/napari/pull/5181))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5197](https://github.com/napari/napari/pull/5197))
- Update plugin dialog design & functionality to add conda install ([napari/napari#5198](https://github.com/napari/napari/pull/5198))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5237](https://github.com/napari/napari/pull/5237))
- Benchmark PR reporting fix ([napari/napari#5246](https://github.com/napari/napari/pull/5246))
- Image slice request and response for async slicing ([napari/napari#5259](https://github.com/napari/napari/pull/5259))
- Points slice request and response for new async slicing ([napari/napari#5264](https://github.com/napari/napari/pull/5264))
- Do not use random shapes in napari_builtins conftest fixtures ([napari/napari#5287](https://github.com/napari/napari/pull/5287))
- Add async slicing "force sync"  ([napari/napari#5299](https://github.com/napari/napari/pull/5299))
- Use plugin display_name for widget parent menu ([napari/napari#5305](https://github.com/napari/napari/pull/5305))
- update benchmark ci ([napari/napari#5309](https://github.com/napari/napari/pull/5309))
- Fix text label translation ([napari/napari#5321](https://github.com/napari/napari/pull/5321))
- Exclude vendored things from absolutify imports ([napari/napari#5324](https://github.com/napari/napari/pull/5324))
- Add test coverage for async slicing of labels ([napari/napari#5325](https://github.com/napari/napari/pull/5325))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5336](https://github.com/napari/napari/pull/5336))
- Fully specify cache path in pip install job ([napari/napari#5357](https://github.com/napari/napari/pull/5357))
- Add pre commit steep for remove unused imports ([napari/napari#5359](https://github.com/napari/napari/pull/5359))
- Add titles and tags to new gallery examples ([napari/napari#5364](https://github.com/napari/napari/pull/5364))
- Add GUI test coverage for changes to Labels.show_selected_label ([napari/napari#5372](https://github.com/napari/napari/pull/5372))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5375](https://github.com/napari/napari/pull/5375))
- Calculate text positions for constant strings ([napari/napari#5387](https://github.com/napari/napari/pull/5387))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5392](https://github.com/napari/napari/pull/5392))
- Configure `fail_on_no_env` for `tox-gh-actions` ([napari/napari#5408](https://github.com/napari/napari/pull/5408))
- Wait until a blocked test task is actually running ([napari/napari#5424](https://github.com/napari/napari/pull/5424))
- Refactor: Qt viewer and VispyCanvas  ([napari/napari#5432](https://github.com/napari/napari/pull/5432))
- Installation: don't include pyqt5 (from [all]) in [dev] installs ([napari/napari#5438](https://github.com/napari/napari/pull/5438))
- Add auto canceling previous test after a new PR commit ([napari/napari#5453](https://github.com/napari/napari/pull/5453))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5462](https://github.com/napari/napari/pull/5462))
- Add digital watermark to napari PNG screenshots ([napari/napari#5494](https://github.com/napari/napari/pull/5494))
- MAINT: add time limit for CI. ([napari/napari#5495](https://github.com/napari/napari/pull/5495))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5502](https://github.com/napari/napari/pull/5502))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5518](https://github.com/napari/napari/pull/5518))
- MAINT: Fix vendoring script and track closest commit. ([napari/napari#5537](https://github.com/napari/napari/pull/5537))
- Fix translation checks in CI ([napari/napari#5562](https://github.com/napari/napari/pull/5562))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5575](https://github.com/napari/napari/pull/5575))
- Maint: Add time limit to --pre and comprehensive tests. ([napari/napari#5597](https://github.com/napari/napari/pull/5597))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5606](https://github.com/napari/napari/pull/5606))
- Bugfix: ensure `tool` is set to conda for conda-installed packages ([napari/napari#5624](https://github.com/napari/napari/pull/5624))
- FIX: fix translation checking script. ([napari/napari#5626](https://github.com/napari/napari/pull/5626))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5627](https://github.com/napari/napari/pull/5627))
- [maint] Update translation string wizard to offer auto-suggestions ([napari/napari#5643](https://github.com/napari/napari/pull/5643))
- Update PR template to front-load issue references ([napari/napari#5659](https://github.com/napari/napari/pull/5659))
- MAINT: Move suspected segfaulting test into its own file. ([napari/napari#5676](https://github.com/napari/napari/pull/5676))
- Unvendor lazy_loader ([napari/napari#5681](https://github.com/napari/napari/pull/5681))
- Add CircleCI to enable docs preview on PRs ([napari/napari#5714](https://github.com/napari/napari/pull/5714))
- Check that release labels are added to each PR ([napari/napari#5733](https://github.com/napari/napari/pull/5733))
- [MAINT] Remove plugin manager source (move to napari/napari-plugin-manager) ([napari/napari#5743](https://github.com/napari/napari/pull/5743))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5765](https://github.com/napari/napari/pull/5765))
- Use `GITHUB_TOKEN` to create test dependecies PR ([napari/napari#5774](https://github.com/napari/napari/pull/5774))
- Use fine grained personal token for test contrains and vendored update ([napari/napari#5777](https://github.com/napari/napari/pull/5777))
- Add tests for io utils to save images ([napari/napari#5780](https://github.com/napari/napari/pull/5780))
- Use tox-min-req for min-req tests ([napari/napari#5784](https://github.com/napari/napari/pull/5784))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5793](https://github.com/napari/napari/pull/5793))
- Update README to display CZI logo for dark and light GitHub themes ([napari/napari#5800](https://github.com/napari/napari/pull/5800))
- Improve discoverability of napari/docs repository. ([napari/napari#5821](https://github.com/napari/napari/pull/5821))
- MAINT: Add backend info to CI comprehensive test names ([napari/napari#5822](https://github.com/napari/napari/pull/5822))
- Move mypy config to pyproject.toml ([napari/napari#5825](https://github.com/napari/napari/pull/5825))
- Fix some typing in colormap utils ([napari/napari#5832](https://github.com/napari/napari/pull/5832))
- Improve type annotation for image layer and related ([napari/napari#5843](https://github.com/napari/napari/pull/5843))
- Fix typing errors in layers.image ([napari/napari#5852](https://github.com/napari/napari/pull/5852))
- Add tests/more tests to widgets with low coverage ([napari/napari#5864](https://github.com/napari/napari/pull/5864))
- Fix type checking for layers.vectors ([napari/napari#5870](https://github.com/napari/napari/pull/5870))
- Fix type checking in layers.surface ([napari/napari#5871](https://github.com/napari/napari/pull/5871))
- test: [Automatic] Constraints upgrades: `dask`, `hypothesis`, `imageio`, `napari-svg`, `pandas`, `pint`, `pydantic`, `pytest-cov`, `tensorstore` ([napari/napari#5881](https://github.com/napari/napari/pull/5881))
- Use a nightly pypi index for numpy & scipy, used by the --pre build ([napari/napari#5882](https://github.com/napari/napari/pull/5882))
- Remove pycln (redundant with ruff F401 rule) ([napari/napari#5887](https://github.com/napari/napari/pull/5887))
- Mock QtConsole in tests ([napari/napari#5890](https://github.com/napari/napari/pull/5890))
- Consistent types for vector inputs/outputs in base layer ([napari/napari#5892](https://github.com/napari/napari/pull/5892))
- MAINT: Fix more typing and enable mypy on more files. ([napari/napari#5897](https://github.com/napari/napari/pull/5897))
- Add __all__ to qthreading and progress ([napari/napari#5898](https://github.com/napari/napari/pull/5898))
- Fix typing in translations ([napari/napari#5900](https://github.com/napari/napari/pull/5900))
- ENH: Use dict to set `MenuID` in view actions ([napari/napari#5903](https://github.com/napari/napari/pull/5903))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#5906](https://github.com/napari/napari/pull/5906))
- [Maint] CI: Use `RUNNER_OS` instead of `PLATFORM` ([napari/napari#5907](https://github.com/napari/napari/pull/5907))
- MAINT: GitHub action Timeout increased by 5 minutes ([napari/napari#5934](https://github.com/napari/napari/pull/5934))
- Some napari.utils typing fixes ([napari/napari#5936](https://github.com/napari/napari/pull/5936))
- Add documentation, enhancement and maintenance fields to PR template ([napari/napari#5943](https://github.com/napari/napari/pull/5943))
- Add docs constraints file ([napari/napari#5988](https://github.com/napari/napari/pull/5988))
- Fix optional arg typing in napari._qt.containers ([napari/napari#6004](https://github.com/napari/napari/pull/6004))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6009](https://github.com/napari/napari/pull/6009))
- Partially fix translations testing ([napari/napari#6014](https://github.com/napari/napari/pull/6014))
- Fix typing in napari.layers.base ([napari/napari#6028](https://github.com/napari/napari/pull/6028))
- Add test for `QtToolTipEventFilter` ([napari/napari#6066](https://github.com/napari/napari/pull/6066))
- Pin numpy below 2 ([napari/napari#6073](https://github.com/napari/napari/pull/6073))
- Fix typing in napari.components.overlays ([napari/napari#6076](https://github.com/napari/napari/pull/6076))
- Fix transform_utils typing ([napari/napari#6082](https://github.com/napari/napari/pull/6082))
- Task: remove html comments from pr description ([napari/napari#6086](https://github.com/napari/napari/pull/6086))
- Reduce noise in PR template ([napari/napari#6092](https://github.com/napari/napari/pull/6092))
- Allow contributors to update test constraints using a comment ([napari/napari#6101](https://github.com/napari/napari/pull/6101))
- Exclude ... from coverage  ([napari/napari#6103](https://github.com/napari/napari/pull/6103))
- Pass `QT_QPA_PLATFORM` through tox configuration ([napari/napari#6110](https://github.com/napari/napari/pull/6110))
- Remove unused parameters from private function. ([napari/napari#6131](https://github.com/napari/napari/pull/6131))
- Fix typing in napari.utils.perf ([napari/napari#6132](https://github.com/napari/napari/pull/6132))
- Use faster version of black ([napari/napari#6133](https://github.com/napari/napari/pull/6133))
- Fix some typing in napari.utils.events ([napari/napari#6142](https://github.com/napari/napari/pull/6142))
- test: [Automatic] Constraints upgrades: `hypothesis`, `magicgui`, `psygnal`, `tensorstore`, `tifffile`, `tqdm`, `virtualenv` ([napari/napari#6143](https://github.com/napari/napari/pull/6143))
- Update PR editing script to remove html. ([napari/napari#6144](https://github.com/napari/napari/pull/6144))
- Update PR editing action script to remove double empty lines in PR description ([napari/napari#6150](https://github.com/napari/napari/pull/6150))
- More typing of napari/utils. ([napari/napari#6152](https://github.com/napari/napari/pull/6152))
- Update typing informations in `_app_model/injection/_processors.py` and `components/layerlist.py` ([napari/napari#6153](https://github.com/napari/napari/pull/6153))
- Fix types in 'napari.utils.colormaps.categorical_colormap' ([napari/napari#6154](https://github.com/napari/napari/pull/6154))
- Fix incorrect types in color_transformations. ([napari/napari#6155](https://github.com/napari/napari/pull/6155))
- Refactor test running for reduce CI time ([napari/napari#6156](https://github.com/napari/napari/pull/6156))
- Check if milestone and label is added to PR ([napari/napari#6158](https://github.com/napari/napari/pull/6158))
- Enable type-checking for `napari.components.experimental`. ([napari/napari#6166](https://github.com/napari/napari/pull/6166))
- Fix typing and clearer code in evented-set. ([napari/napari#6168](https://github.com/napari/napari/pull/6168))
- Fix and enable typing of selectable lists ([napari/napari#6169](https://github.com/napari/napari/pull/6169))
- Add PyQt6 to tox -e mypy ([napari/napari#6170](https://github.com/napari/napari/pull/6170))
- Remove an "if" that prevents proper run of "upgrade dependecies" wokflow if triggered by comment ([napari/napari#6171](https://github.com/napari/napari/pull/6171))
- Misc typing fixes ([napari/napari#6172](https://github.com/napari/napari/pull/6172))
- Fix typo in path to file for upgrade dependencies ([napari/napari#6173](https://github.com/napari/napari/pull/6173))
- Update constraints upgrade script to run with appropriate events ([napari/napari#6175](https://github.com/napari/napari/pull/6175))
- Add missed "and milestone" ([napari/napari#6176](https://github.com/napari/napari/pull/6176))
- Do not clone repository to subdirectory in examples test ([napari/napari#6181](https://github.com/napari/napari/pull/6181))
- Add a timeout to some GH actions tests. ([napari/napari#6187](https://github.com/napari/napari/pull/6187))
- Fix typing in components.viewer_model ([napari/napari#6188](https://github.com/napari/napari/pull/6188))
- DOC Add comment in `_instantiate_dock_widget` ([napari/napari#6189](https://github.com/napari/napari/pull/6189))
- Fix some typing in napari.components ([napari/napari#6203](https://github.com/napari/napari/pull/6203))
- Allow to use all ViewerModel kwargs in Viewer constructor ([napari/napari#6209](https://github.com/napari/napari/pull/6209))
- Fix upgrade dependencies wokflow  ([napari/napari#6211](https://github.com/napari/napari/pull/6211))
- Replace more np.all( ... = ...) with np.array_equal ([napari/napari#6213](https://github.com/napari/napari/pull/6213))
- cleanup np.all(... == ...) from test_points.py ([napari/napari#6217](https://github.com/napari/napari/pull/6217))
- remove np.all(... == ...) in test_surface.py ([napari/napari#6218](https://github.com/napari/napari/pull/6218))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6221](https://github.com/napari/napari/pull/6221))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6229](https://github.com/napari/napari/pull/6229))
- Move `test_file_menu.py` to new app model location ([napari/napari#6233](https://github.com/napari/napari/pull/6233))
- More removal of np.all(... == ...) ([napari/napari#6238](https://github.com/napari/napari/pull/6238))
- Remove sphinx dependency from defaults dependecies ([napari/napari#6239](https://github.com/napari/napari/pull/6239))
- MAINT: Use scipy builtins rotation to compute quaternions. ([napari/napari#6241](https://github.com/napari/napari/pull/6241))
- MAINT: Replace `assert np.all(? == ?)` with `assert_array_equal` ([napari/napari#6244](https://github.com/napari/napari/pull/6244))
- Fix some typing in napari._vispy ([napari/napari#6245](https://github.com/napari/napari/pull/6245))
- Type _WeakCounter ([napari/napari#6246](https://github.com/napari/napari/pull/6246))
- Fix typing in napari.utils.theme ([napari/napari#6247](https://github.com/napari/napari/pull/6247))
- remove: napari.qt.progress (deprecated in 0.4.11) ([napari/napari#6252](https://github.com/napari/napari/pull/6252))
- Restore 'V' keybinding for layer visibiltiy toggle ([napari/napari#6261](https://github.com/napari/napari/pull/6261))
- Update `app-model`, `dask`, `fsspec`, `hypothesis`, `imageio`, `ipython`, `jsonschema`, `matplotlib`, `numpy`, `pandas`, `pillow`, `psygnal`, `pytest`, `qtconsole`, `qtpy`, `rich`, `scipy`, `superqt`, `tensorstore`, `tifffile`, `virtualenv`, `xarray`, `zarr` ([napari/napari#6265](https://github.com/napari/napari/pull/6265))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6266](https://github.com/napari/napari/pull/6266))
- Fix nitpicks in `id` and `title` `Action` fields in samples menu ([napari/napari#6267](https://github.com/napari/napari/pull/6267))
- ENH Make `_open_preferences_dialog` return `PreferencesDialog` ([napari/napari#6269](https://github.com/napari/napari/pull/6269))
- Bump app-model ([napari/napari#6271](https://github.com/napari/napari/pull/6271))
- Use `MenuID` in sample menu tests ([napari/napari#6273](https://github.com/napari/napari/pull/6273))
- Fix benchmark suite virtualenvs, and disable broken memory benchmarks ([napari/napari#6278](https://github.com/napari/napari/pull/6278))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6287](https://github.com/napari/napari/pull/6287))
- Adding helper function for events and property deprecation ([napari/napari#6288](https://github.com/napari/napari/pull/6288))
- Fix labels for dependabot ([napari/napari#6290](https://github.com/napari/napari/pull/6290))
- [Maintenance] Fix missing v in the docker-login action version ([napari/napari#6291](https://github.com/napari/napari/pull/6291))
- MAINT: Remove auto-author-assign ([napari/napari#6292](https://github.com/napari/napari/pull/6292))
- Remove a few of the last instance of np.all(? == ?). ([napari/napari#6293](https://github.com/napari/napari/pull/6293))
- Enable memory benchmarks for layers ([napari/napari#6295](https://github.com/napari/napari/pull/6295))
- [Maint] Add zarr to optional dependencies in pyproject.toml ([napari/napari#6297](https://github.com/napari/napari/pull/6297))
- Set permissions to `allow upgrate_test_contstraints` work  ([napari/napari#6298](https://github.com/napari/napari/pull/6298))
- Revert "MAINT: Use scipy builtins rotation to compute quaternions. (#6241)" ([napari/napari#6299](https://github.com/napari/napari/pull/6299))
- Add pystack to debug hanging linux test ([napari/napari#6310](https://github.com/napari/napari/pull/6310))
- [Maintenance] Update bug_report template to add napari --info ([napari/napari#6312](https://github.com/napari/napari/pull/6312))
- Use yaml for bug report Issue template ([napari/napari#6313](https://github.com/napari/napari/pull/6313))
- Add pre-commit check for basic formattings bugs  ([napari/napari#6315](https://github.com/napari/napari/pull/6315))
- Add coverage report upload to comprehensive test ([napari/napari#6316](https://github.com/napari/napari/pull/6316))
- Update `dask`, `hypothesis`, `numpy`, `pillow`, `pretend`, `psutil`, `pyqt5`, `pyqt6`, `pyside6`, `superqt` ([napari/napari#6322](https://github.com/napari/napari/pull/6322))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6323](https://github.com/napari/napari/pull/6323))
- Fix pre-commit configuration ([napari/napari#6328](https://github.com/napari/napari/pull/6328))
- Directly set author of commit in vendored workflow ([napari/napari#6329](https://github.com/napari/napari/pull/6329))
- Bump Mypy and some type fixes. ([napari/napari#6332](https://github.com/napari/napari/pull/6332))
- Add 'raise' option back to `strict_qt` in `make_napari_viewer` ([napari/napari#6335](https://github.com/napari/napari/pull/6335))
- Rename test_strings to validate_strings to stop confusing pytest ([napari/napari#6338](https://github.com/napari/napari/pull/6338))
- "no-commit-to-branch" is preventing contribution. ([napari/napari#6341](https://github.com/napari/napari/pull/6341))
- MAINT: Refine Mypy config for qtpy. ([napari/napari#6342](https://github.com/napari/napari/pull/6342))
- Disable ptrace protection to make pytest-pystack work ([napari/napari#6343](https://github.com/napari/napari/pull/6343))
- Fix labeler configuration ([napari/napari#6344](https://github.com/napari/napari/pull/6344))
- Add codecov token to reduce propability of fail to upload from main branch ([napari/napari#6346](https://github.com/napari/napari/pull/6346))
- Fix upstream deprecation: change `np.alltrue` to `np.array_equiv` ([napari/napari#6347](https://github.com/napari/napari/pull/6347))
- Maint: mypy opt-in to opt-out. ([napari/napari#6352](https://github.com/napari/napari/pull/6352))
- Full typing of a few more files in napari.utils.* ([napari/napari#6356](https://github.com/napari/napari/pull/6356))
- Fix build wheel workflow file name ([napari/napari#6357](https://github.com/napari/napari/pull/6357))
- Fix make release workflow ([napari/napari#6359](https://github.com/napari/napari/pull/6359))
- Typing: Fully type 5 more files ([napari/napari#6361](https://github.com/napari/napari/pull/6361))
- Update examples/clipboard_.py to fix FutureWarning ([napari/napari#6365](https://github.com/napari/napari/pull/6365))
- Update `fsspec`, `imageio`, `magicgui`, `napari-console`, `npe2`, `pillow`, `tensorstore`, `xarray` ([napari/napari#6367](https://github.com/napari/napari/pull/6367))
- fix `TransformChain.__getitem__` signature ([napari/napari#6369](https://github.com/napari/napari/pull/6369))
- Fix permission for JasonEtco/create-an-issue@v2 action ([napari/napari#6370](https://github.com/napari/napari/pull/6370))
- Automatic add `maintenance` label to upgrade dependecies workflow ([napari/napari#6371](https://github.com/napari/napari/pull/6371))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6373](https://github.com/napari/napari/pull/6373))
- Ensure the conda bundle workflows have the appropriate permissions ([napari/napari#6379](https://github.com/napari/napari/pull/6379))
- Skip redundant pre-commit hooks ([napari/napari#6389](https://github.com/napari/napari/pull/6389))
- Update `babel`, `dask`, `pandas`, `pooch`, `pytest`, `qtpy`, `virtualenv` ([napari/napari#6398](https://github.com/napari/napari/pull/6398))
- Fix environment variable name name in docs build ([napari/napari#6401](https://github.com/napari/napari/pull/6401))
- ci(dependabot): bump actions/checkout from 3 to 4 ([napari/napari#6403](https://github.com/napari/napari/pull/6403))
- Fix some weird behaviors when using delete and backspace keys as shortcuts (with or without modifiers) ([napari/napari#6406](https://github.com/napari/napari/pull/6406))
- Use ruff to format strings to single quotes. ([napari/napari#6407](https://github.com/napari/napari/pull/6407))
- Fix linter warnings in qt_main_window ([napari/napari#6409](https://github.com/napari/napari/pull/6409))
- Unify circleci and build_docs workflows across repositories  ([napari/napari#6417](https://github.com/napari/napari/pull/6417))
- Fix `test_singlescreen_window_settings` to allow it to run locally on multiscreen configuration ([napari/napari#6422](https://github.com/napari/napari/pull/6422))
- refactor `napari/_qt/_tests/test_async_slicing.py` to reduce fragility of test ([napari/napari#6423](https://github.com/napari/napari/pull/6423))
- Simplify unused parameters of Quaternion functions. ([napari/napari#6424](https://github.com/napari/napari/pull/6424))
- Still More typing V ([napari/napari#6427](https://github.com/napari/napari/pull/6427))
- Synchronize `rgb` docstring of `ViewerModel.add_image` and `Image` constructor ([napari/napari#6428](https://github.com/napari/napari/pull/6428))
- Fix milestone and label checker to be triggered by `milestoned`/`demilestoned` events ([napari/napari#6430](https://github.com/napari/napari/pull/6430))
- Refactor Skipped test ([napari/napari#6431](https://github.com/napari/napari/pull/6431))
- Update `dask`, `hypothesis`, `numpy`, `pandas`, `tensorstore`, `wrapt` ([napari/napari#6441](https://github.com/napari/napari/pull/6441))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6447](https://github.com/napari/napari/pull/6447))
- add addtional pystack arguments ([napari/napari#6457](https://github.com/napari/napari/pull/6457))
- Bump docker image version to most recent from 3.x.x line ([napari/napari#6458](https://github.com/napari/napari/pull/6458))
- MAINT Bump magicgui version to v0.7.0 ([napari/napari#6462](https://github.com/napari/napari/pull/6462))
- Update `certifi`, `hypothesis`, `imageio`, `jsonschema`, `matplotlib`, `numba`, `pillow`, `psygnal`, `pydantic`, `pygments`, `qtconsole`, `rich`, `scipy`, `tensorstore`, `xarray` ([napari/napari#6470](https://github.com/napari/napari/pull/6470))
- Change default labels layer to uint8. ([napari/napari#6471](https://github.com/napari/napari/pull/6471))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6474](https://github.com/napari/napari/pull/6474))
- Update `app-model`, `babel`, `coverage`, `dask`, `fsspec`, `hypothesis`, `imageio`, `ipython`, `lxml`, `magicgui`, `pandas`, `pint`, `psutil`, `pydantic`, `pyqt6`, `pytest-qt`, `tensorstore`, `tifffile`, `virtualenv`, `xarray` ([napari/napari#6478](https://github.com/napari/napari/pull/6478))
- [Maint, CI] Update circleci.yml for artifact location to fix redirector ([napari/napari#6480](https://github.com/napari/napari/pull/6480))
- Upload test artifacts on failure ([napari/napari#6486](https://github.com/napari/napari/pull/6486))
- Add testing_extra and optional dependencies when creating constraints ([napari/napari#6487](https://github.com/napari/napari/pull/6487))
- Add size and ndim to LayerDataProtocol ([napari/napari#6494](https://github.com/napari/napari/pull/6494))
- Fix scheduled benchmarks to test both last release and main ([napari/napari#6496](https://github.com/napari/napari/pull/6496))
- Type napari.layers.image helper sub-modules ([napari/napari#6499](https://github.com/napari/napari/pull/6499))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6505](https://github.com/napari/napari/pull/6505))
- Add import lint back to CI ([napari/napari#6506](https://github.com/napari/napari/pull/6506))
- Finish typing layers.base helper files ([napari/napari#6508](https://github.com/napari/napari/pull/6508))
- Add lots of typing to layers.base ([napari/napari#6509](https://github.com/napari/napari/pull/6509))
- Add `_block_refresh()` to layers ([napari/napari#6525](https://github.com/napari/napari/pull/6525))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6528](https://github.com/napari/napari/pull/6528))
- Add cache to Transform calculation ([napari/napari#6536](https://github.com/napari/napari/pull/6536))
- Rescale image data if outside `float32` precision  ([napari/napari#6537](https://github.com/napari/napari/pull/6537))
- MNT: Use `partial` in samples menu to avoid leaking  ([napari/napari#6538](https://github.com/napari/napari/pull/6538))
- Type two sub-modules in napari.layers.utils ([napari/napari#6539](https://github.com/napari/napari/pull/6539))
- Print a whole stack if throttler is not finished ([napari/napari#6549](https://github.com/napari/napari/pull/6549))
- Minimal changes for mlx (and jax) compatibility for Image layers ([napari/napari#6553](https://github.com/napari/napari/pull/6553))
- Improve repo configuration based on scientific python suggestions  ([napari/napari#6554](https://github.com/napari/napari/pull/6554))
- Bump mypy version and fix errors  ([napari/napari#6557](https://github.com/napari/napari/pull/6557))
- ci(dependabot): bump aganders3/headless-gui from 1 to 2 ([napari/napari#6563](https://github.com/napari/napari/pull/6563))
- ci(dependabot): bump actions/labeler from 4 to 5 ([napari/napari#6565](https://github.com/napari/napari/pull/6565))
- ci(dependabot): bump actions/setup-python from 4 to 5 ([napari/napari#6567](https://github.com/napari/napari/pull/6567))
- Fix test in napari_builtins to remove import from conftest ([napari/napari#6568](https://github.com/napari/napari/pull/6568))
- Update test to work with `app-model==0.2.4` ([napari/napari#6573](https://github.com/napari/napari/pull/6573))
- Add some more typing to utils.misc ([napari/napari#6574](https://github.com/napari/napari/pull/6574))
- Fix typing in utils.perf ([napari/napari#6575](https://github.com/napari/napari/pull/6575))
- Add more typing to utils.events.containers ([napari/napari#6576](https://github.com/napari/napari/pull/6576))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6581](https://github.com/napari/napari/pull/6581))
- Try fix hanging tests by move `self.stop()` on end of functions that update GUI ([napari/napari#6594](https://github.com/napari/napari/pull/6594))
- Cache linear matrix decomposition in `Affine` class ([napari/napari#6635](https://github.com/napari/napari/pull/6635))
- bump actions/download-artifact and actions/upload-artifact from 3 to 4 ([napari/napari#6638](https://github.com/napari/napari/pull/6638))
- Fix labeler configuration after update to v5 ([napari/napari#6639](https://github.com/napari/napari/pull/6639))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6648](https://github.com/napari/napari/pull/6648))
- Update `app-model`, `dask`, `hypothesis`, `ipython`, `lxml`, `matplotlib`, `npe2`, `numba`, `numpydoc`, `pandas`, `pillow`, `psygnal`, `pyside2`, `pyside6`, `scipy`, `superqt`, `xarray`, `zarr` ([napari/napari#6655](https://github.com/napari/napari/pull/6655))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6656](https://github.com/napari/napari/pull/6656))
- Disallow incomplete defs in layers.image ([napari/napari#6659](https://github.com/napari/napari/pull/6659))
- Check untyped defs in _shapes_models ([napari/napari#6660](https://github.com/napari/napari/pull/6660))
- Typing improvements to vectors layer ([napari/napari#6661](https://github.com/napari/napari/pull/6661))
- Exclude problematic surface texture example from tests and docs building ([napari/napari#6663](https://github.com/napari/napari/pull/6663))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6672](https://github.com/napari/napari/pull/6672))
- Migrate from setup.cfg to pyproject.toml ([napari/napari#6673](https://github.com/napari/napari/pull/6673))
- Raise exception on TransformChain.simplified when chain is empty ([napari/napari#6674](https://github.com/napari/napari/pull/6674))
- Add human readable names for Points layer subvisual ([napari/napari#6675](https://github.com/napari/napari/pull/6675))
- Refactor perf module for better readabiity ([napari/napari#6686](https://github.com/napari/napari/pull/6686))
- Fix upload of benchmarks ([napari/napari#6697](https://github.com/napari/napari/pull/6697))
- Bump minimum dask version ([napari/napari#6698](https://github.com/napari/napari/pull/6698))
- ci(dependabot): bump peter-evans/create-pull-request from 5 to 6 ([napari/napari#6700](https://github.com/napari/napari/pull/6700))
- ci(dependabot): bump codecov/codecov-action from 3 to 4 ([napari/napari#6701](https://github.com/napari/napari/pull/6701))
- ci(dependabot): bump aganders3/headless-gui from 1 to 2 ([napari/napari#6702](https://github.com/napari/napari/pull/6702))
- Disable pyside2 test on windows CI ([napari/napari#6711](https://github.com/napari/napari/pull/6711))
- Fix `--pre` workflow: missing setup to enable `pyautogui` usage on Linux ([napari/napari#6713](https://github.com/napari/napari/pull/6713))
- Typing improvements in layers.shapes ([napari/napari#6716](https://github.com/napari/napari/pull/6716))
- Improve typing in layers.surface ([napari/napari#6717](https://github.com/napari/napari/pull/6717))
- Create .Xauthority file in conftest.py rather than GHA workflows ([napari/napari#6719](https://github.com/napari/napari/pull/6719))
- use cross group dependecy in pyproject.toml ([napari/napari#6720](https://github.com/napari/napari/pull/6720))
- Exclude pyside 2 test on comprehensive workflow ([napari/napari#6721](https://github.com/napari/napari/pull/6721))
- Move base class for Image and Labels to its own file ([napari/napari#6725](https://github.com/napari/napari/pull/6725))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6737](https://github.com/napari/napari/pull/6737))
- Drop Python 3.8, add Python 3.12 testing ([napari/napari#6738](https://github.com/napari/napari/pull/6738))
- Fix Remove lambdas when updating menus from context in `Window` ([napari/napari#6740](https://github.com/napari/napari/pull/6740))
- Improve widget clean up in `test_widget_hide_destroy` ([napari/napari#6741](https://github.com/napari/napari/pull/6741))
- Move providers from `_providers.py` to `_qproviders.py` ([napari/napari#6743](https://github.com/napari/napari/pull/6743))
- [Maint] Exclude pyqt6 6.6.1 on macOS in  pyproject.toml ([napari/napari#6748](https://github.com/napari/napari/pull/6748))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6756](https://github.com/napari/napari/pull/6756))
- [Maint] Put testing dependencies in [dev] as napari[testing] ([napari/napari#6757](https://github.com/napari/napari/pull/6757))
- bump tifffile dependency and remove deprecation-handling code ([napari/napari#6765](https://github.com/napari/napari/pull/6765))
- Move Qt view menu actions inside Qt folder ([napari/napari#6767](https://github.com/napari/napari/pull/6767))
- Improve typing in layers.points ([napari/napari#6770](https://github.com/napari/napari/pull/6770))
- [Maint] Correct a few more setup.cfg to pyproject.toml ([napari/napari#6771](https://github.com/napari/napari/pull/6771))
- [maint] drop unused experimental vendor humanize and cachetools ([napari/napari#6772](https://github.com/napari/napari/pull/6772))
- Switch from black to ruff-format ([napari/napari#6775](https://github.com/napari/napari/pull/6775))
- numpy version 2.0 compatibility ([napari/napari#6776](https://github.com/napari/napari/pull/6776))
- Remove app-model CommandId enum in favor of plain strings ([napari/napari#6777](https://github.com/napari/napari/pull/6777))
- Sort parameters in docstring and `__init__` of `Layer` ([napari/napari#6779](https://github.com/napari/napari/pull/6779))
- Implement validation of docstrings and kwargs order ([napari/napari#6782](https://github.com/napari/napari/pull/6782))
- Sort docstring and kwargs of Points layer ([napari/napari#6784](https://github.com/napari/napari/pull/6784))
- Sort docstring and kwargs of Shapes layer ([napari/napari#6786](https://github.com/napari/napari/pull/6786))
- Sort docstring and kwargs of Surface layer ([napari/napari#6787](https://github.com/napari/napari/pull/6787))
- Sort docstring and kwargs of Tracks layer ([napari/napari#6788](https://github.com/napari/napari/pull/6788))
- improve stack trace of autogenerated `ViewerModel.add_xxxx` methods ([napari/napari#6791](https://github.com/napari/napari/pull/6791))
- Move _is_moving property from Layer to Shapes ([napari/napari#6795](https://github.com/napari/napari/pull/6795))
- Fix `ImportError: lxml.html.clean module is now a separate project lxml_html_clean` over test suite (Ubuntu 20.04 and benchmarks) ([napari/napari#6799](https://github.com/napari/napari/pull/6799))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6800](https://github.com/napari/napari/pull/6800))
- Add more typing to two napari.layers sub-modules ([napari/napari#6803](https://github.com/napari/napari/pull/6803))
- [maint] Fix deploy_docs.yml for change in napari/docs workflow ([napari/napari#6809](https://github.com/napari/napari/pull/6809))
- Sort docstring and kwargs of Vectors layer ([napari/napari#6810](https://github.com/napari/napari/pull/6810))
- Fix some rst syntax in docstrings ([napari/napari#6812](https://github.com/napari/napari/pull/6812))
- Speedup `napari.layers.utils._test.test_stack_utils.py`  ([napari/napari#6813](https://github.com/napari/napari/pull/6813))
- [Maint] Update CircleCI config.yml for changes in napari/docs Makefile ([napari/napari#6814](https://github.com/napari/napari/pull/6814))
- Add possibility to test consistency of docstring content between base class and class ([napari/napari#6816](https://github.com/napari/napari/pull/6816))
- Rename `axes_labels` to `axis_labels` in some internal variables and docstrings ([napari/napari#6817](https://github.com/napari/napari/pull/6817))
- Add workflow for automatically remove `ready to merge` label ([napari/napari#6818](https://github.com/napari/napari/pull/6818))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6820](https://github.com/napari/napari/pull/6820))
- Move `_mock_app` fixture to `_testsupport.py` and add it to `make_napari_viewer` ([napari/napari#6823](https://github.com/napari/napari/pull/6823))
- add test for ScalarField docstring, fix pointed bugs ([napari/napari#6824](https://github.com/napari/napari/pull/6824))
- Add write permission to `remove_ready_to_merge.yml` workflow ([napari/napari#6825](https://github.com/napari/napari/pull/6825))
- Bump python from 3.9 to 3.12 in pre-release tests ([napari/napari#6826](https://github.com/napari/napari/pull/6826))
- fix "Remove ready to merge label" ([napari/napari#6830](https://github.com/napari/napari/pull/6830))
- Remove "ready to merge" label action part 3 ([napari/napari#6832](https://github.com/napari/napari/pull/6832))
- ci(dependabot): bump the actions group with 2 updates ([napari/napari#6835](https://github.com/napari/napari/pull/6835))
- DeprecationWarning in ensure_iterable and is_iterable, Closes #6256 ([napari/napari#6836](https://github.com/napari/napari/pull/6836))
- Do not crash test on graphviz installation fail ([napari/napari#6837](https://github.com/napari/napari/pull/6837))
- Update `hypothesis`, `pandas`, `pydantic` ([napari/napari#6838](https://github.com/napari/napari/pull/6838))
- Allow to use "remove ready to merge lablel" and "edit PR description" callable from another repository ([napari/napari#6839](https://github.com/napari/napari/pull/6839))
- Add a few ruff lint rules: ASYNC, EXE, FA and LOG ([napari/napari#6840](https://github.com/napari/napari/pull/6840))
- Add extra field to store plugin display name ([napari/napari#6841](https://github.com/napari/napari/pull/6841))
- Add pytest-style rules for ruff ([napari/napari#6842](https://github.com/napari/napari/pull/6842))
- Enable ruff SLOT linting rule ([napari/napari#6843](https://github.com/napari/napari/pull/6843))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6844](https://github.com/napari/napari/pull/6844))
- Define submenus with their actions, remove submenus.py file ([napari/napari#6848](https://github.com/napari/napari/pull/6848))
- Add T20 ruff rule (print calls) ([napari/napari#6849](https://github.com/napari/napari/pull/6849))
- Test dev examples ([napari/napari#6854](https://github.com/napari/napari/pull/6854))
- Check prereleases testing with macOS + Python 3.12 + PyQt6 ([napari/napari#6858](https://github.com/napari/napari/pull/6858))
- Update `dask`, `imageio`, `scikit-image`, `tifffile`, `virtualenv` ([napari/napari#6861](https://github.com/napari/napari/pull/6861))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6863](https://github.com/napari/napari/pull/6863))
- Update `hypothesis`, `pytest`, `virtualenv`, bump mypy constraints and resolve pointed problems.  ([napari/napari#6866](https://github.com/napari/napari/pull/6866))
- Fix compile constraints by compile per operating system and using `uv`  ([napari/napari#6873](https://github.com/napari/napari/pull/6873))
- Fix benchmark reporting ([napari/napari#6877](https://github.com/napari/napari/pull/6877))
- Move help actions under `_qt` and remove lambdas ([napari/napari#6883](https://github.com/napari/napari/pull/6883))
- Fix citation cff and add worflow for future validation ([napari/napari#6888](https://github.com/napari/napari/pull/6888))
- Update `app-model`, `babel`, `coverage`, `dask`, `fsspec`, `hypothesis`, `jsonschema`, `lxml`, `matplotlib`, `psygnal`, `pygments`, `pytest`, `qtconsole`, `superqt`, `tensorstore`, `tifffile`, `tqdm`, `virtualenv`, `xarray`, `zarr` ([napari/napari#6891](https://github.com/napari/napari/pull/6891))
- Add longer description to pytest fail in `fail_obj_graph` ([napari/napari#6899](https://github.com/napari/napari/pull/6899))
- Migrate Window menu to app-model ([napari/napari#6905](https://github.com/napari/napari/pull/6905))
- [Maint] On PRs, dont run benchmarks unless initial tests pass ([napari/napari#6909](https://github.com/napari/napari/pull/6909))
- Fix `PIP_CONSTRAINT` to not crash python installation on macos arm and python 3.10 ([napari/napari#6911](https://github.com/napari/napari/pull/6911))
- Migrate Debug menu to app-model ([napari/napari#6915](https://github.com/napari/napari/pull/6915))
- remove error reporter code ([napari/napari#6923](https://github.com/napari/napari/pull/6923))
- MNT: Fix layerlist context creation ([napari/napari#6926](https://github.com/napari/napari/pull/6926))
- Automatically remove run-benchmarks label once benchmarks are executed ([napari/napari#6929](https://github.com/napari/napari/pull/6929))
- Use `superqt.utils.CodeSyntaxHighlight` instead of `napari._qt.code_syntax_highlight.Pylighter` ([napari/napari#6938](https://github.com/napari/napari/pull/6938))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6939](https://github.com/napari/napari/pull/6939))
- Add a test for viewer.close_all. ([napari/napari#6942](https://github.com/napari/napari/pull/6942))
- Add more file menu actions tests ([napari/napari#6943](https://github.com/napari/napari/pull/6943))
- [Maint] Update docs constraints for new napari-sphinx-theme release ([napari/napari#6947](https://github.com/napari/napari/pull/6947))
- ci(dependabot): bump docker/login-action from 3.1.0 to 3.2.0 in the actions group ([napari/napari#6951](https://github.com/napari/napari/pull/6951))
- Update `certifi`, `dask`, `fsspec`, `hypothesis`, `ipython`, `magicgui`, `pint`, `pooch`, `pydantic`, `pytest`, `superqt` ([napari/napari#6953](https://github.com/napari/napari/pull/6953))
- Add some tests for view menu actions ([napari/napari#6955](https://github.com/napari/napari/pull/6955))
- [pre-commit.ci] pre-commit autoupdate ([napari/napari#6956](https://github.com/napari/napari/pull/6956))
- Add some tests for plugins menu actions ([napari/napari#6962](https://github.com/napari/napari/pull/6962))
- Add some tests for help menu actions ([napari/napari#6963](https://github.com/napari/napari/pull/6963))
- Add a test for window menu actions ([napari/napari#6972](https://github.com/napari/napari/pull/6972))
- [maint] Update docker-singularity-publish.yml to run on PR ([napari/napari#6973](https://github.com/napari/napari/pull/6973))
- More numpy 2.0 related fixes ([napari/napari#6974](https://github.com/napari/napari/pull/6974))
- Add some tests for debug menu actions and fix validation to create the menu ([napari/napari#6975](https://github.com/napari/napari/pull/6975))
- Remove redundant `NapariMenu` ([napari/napari#6977](https://github.com/napari/napari/pull/6977))
- Update `rename_argument` to use `FutureWarning` instead of `DeprecationWarning` ([napari/napari#6980](https://github.com/napari/napari/pull/6980))
- Add attributes to `DummyTimer` ([napari/napari#6982](https://github.com/napari/napari/pull/6982))
- Update `test_create_func_renamed` test to use `FutureWarning` instead of `DeprecationWarning` ([napari/napari#6987](https://github.com/napari/napari/pull/6987))
- restore numpy 2.0 constraints ([napari/napari#6994](https://github.com/napari/napari/pull/6994))
- Update `dask`, `hypothesis`, `numba`, `pydantic`, `tensorstore`, `vispy`, `xarray` ([napari/napari#6995](https://github.com/napari/napari/pull/6995))
- Make test log easier to read by removing `-v` from pytest call ([napari/napari#6996](https://github.com/napari/napari/pull/6996))
- Add tests for viewer scale bar attributes (`colored` and `ticks`) ([napari/napari#7006](https://github.com/napari/napari/pull/7006))
- Add tox-uv to test environment for speedup installation, fix codecov upload ([napari/napari#7013](https://github.com/napari/napari/pull/7013))
- Update CircleCI config.yml to not overwrite requirements ([napari/docs#184](https://github.com/napari/docs/pull/184))
- Update CI actions versions ([napari/docs#213](https://github.com/napari/docs/pull/213))
- [Maintenance] Use permissions for labeler action (and set v4) ([napari/docs#247](https://github.com/napari/docs/pull/247))
- [maintenance] Fix missing v in labeler action version ([napari/docs#248](https://github.com/napari/docs/pull/248))
- Use docs constraints in circleci workflow ([napari/docs#251](https://github.com/napari/docs/pull/251))
- Add missed pinning dependencies ([napari/docs#260](https://github.com/napari/docs/pull/260))
- [Maintenance] Update deploy_docs.yml to use constraints ([napari/docs#263](https://github.com/napari/docs/pull/263))
- [Maintenance] fix path to requirements.txt in deploy_docs workflow ([napari/docs#264](https://github.com/napari/docs/pull/264))
- Delete vestigial docs/requirements.txt ([napari/docs#270](https://github.com/napari/docs/pull/270))
- [Maint] use concurrency to cancel in-progress build_docs  ([napari/docs#277](https://github.com/napari/docs/pull/277))
- [Maintenance] Update CIrcleCI redirector circleci.yml to fix artifact path ([napari/docs#278](https://github.com/napari/docs/pull/278))
- fix napari repo path to constraints ([napari/docs#290](https://github.com/napari/docs/pull/290))
- Update headless-gui action in build (fix screenshots) ([napari/docs#294](https://github.com/napari/docs/pull/294))
- Update .gitignore ([napari/docs#300](https://github.com/napari/docs/pull/300))
- Set `NAPARI_CONFIG` to clean settings ([napari/docs#310](https://github.com/napari/docs/pull/310))
- Unify docs workflows ([napari/docs#348](https://github.com/napari/docs/pull/348))
- For this repo, link contributions to documentation contribution guide ([napari/docs#366](https://github.com/napari/docs/pull/366))
- [Maint] fix the download and deploy part of workflow ([napari/docs#380](https://github.com/napari/docs/pull/380))
- [Maint] fix build_and_deploy.yml paths ([napari/docs#384](https://github.com/napari/docs/pull/384))
- fix build_and_deploy.yml take 2 ([napari/docs#385](https://github.com/napari/docs/pull/385))
- [maint] fix app-model intersphinx link ([napari/docs#388](https://github.com/napari/docs/pull/388))
- Fix make html-noplot command ([napari/docs#394](https://github.com/napari/docs/pull/394))
- [Maint] use lxml[html_clean] in requirements.txt ([napari/docs#397](https://github.com/napari/docs/pull/397))
- Add maintenance workflows from main repo (edit PR description/clean up ready to merge label) ([napari/docs#406](https://github.com/napari/docs/pull/406))
- Bump napari sphinx theme version ([napari/docs#423](https://github.com/napari/docs/pull/423))


## 43 authors added to this release (alphabetical)

- [aeisenbarth](https://github.com/napari/napari/commits?author=aeisenbarth) - @aeisenbarth
- [Amirreza Aflakparast](https://github.com/napari/napari/commits?author=AmirAflak) - @AmirAflak
- [andrew sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Ashley Anderson](https://github.com/napari/napari/commits?author=aganders3) - @aganders3
- [Christopher Nauroth-Kreß](https://github.com/napari/napari/commits?author=Chris-N-K) - @Chris-N-K
- [Daniel Althviz Moré](https://github.com/napari/napari/commits?author=dalthviz) - @dalthviz
- [Daniel Zhang](https://github.com/napari/napari/commits?author=DanGonite57) - @DanGonite57
- [David Paleček](https://github.com/napari/napari/commits?author=palec87) - @palec87
- [David Pinto](https://github.com/napari/napari/commits?author=MarchisLost) - @MarchisLost
- [David Stansby](https://github.com/napari/napari/commits?author=dstansby) - @dstansby
- [Dr. Andrew Annex](https://github.com/napari/napari/commits?author=AndrewAnnex) - @AndrewAnnex
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Eric Perlman](https://github.com/napari/napari/commits?author=perlman) - @perlman
- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [jaime rodriguez-guerra](https://github.com/napari/napari/commits?author=jaimergp) - @jaimergp
- [James Ryan](https://github.com/napari/napari/commits?author=jamesyan-git) - @jamesyan-git
- [Jan Eglinger](https://github.com/napari/napari/commits?author=imagejan) - @imagejan
- [Johannes Soltwedel](https://github.com/napari/napari/commits?author=jo-mueller) - @jo-mueller
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Jules Vanaret](https://github.com/napari/napari/commits?author=jules-vanaret) - @jules-vanaret
- [Kabilar Gunalan](https://github.com/napari/napari/commits?author=kabilar) - @kabilar
- [Kim Pevey](https://github.com/napari/napari/commits?author=kcpevey) - @kcpevey
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Konstantin Sofiiuk](https://github.com/napari/napari/commits?author=ksofiyuk) - @ksofiyuk
- [kyle i. s. harrington](https://github.com/napari/napari/commits?author=kephale) - @kephale
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Lucy Liu](https://github.com/napari/napari/commits?author=lucyleeow) - @lucyleeow
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [M Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Markus Stabrin](https://github.com/napari/napari/commits?author=mstabrin) - @mstabrin
- [Martin Weigert](https://github.com/napari/napari/commits?author=maweigert) - @maweigert
- [Melissa Weber Mendonça](https://github.com/napari/napari/commits?author=melissawm) - @melissawm
- [nadalyn miller](https://github.com/napari/napari/commits?author=Nadalyn-CZI) - @Nadalyn-CZI
- [odinsbane](https://github.com/napari/napari/commits?author=odinsbane) - @odinsbane
- [pam wadhwa](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Sam Cunliffe](https://github.com/napari/napari/commits?author=samcunliffe) - @samcunliffe
- [Stefan van der Walt](https://github.com/napari/napari/commits?author=stefanv) - @stefanv
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Wouter-Michiel Vierdag](https://github.com/napari/napari/commits?author=melonora) - @melonora


## 41 reviewers added to this release (alphabetical)

- [alister burt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [andrew sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Ashley Anderson](https://github.com/napari/napari/commits?author=aganders3) - @aganders3
- [Daniel Althviz Moré](https://github.com/napari/napari/commits?author=dalthviz) - @dalthviz
- [David Paleček](https://github.com/napari/napari/commits?author=palec87) - @palec87
- [David Stansby](https://github.com/napari/napari/commits?author=dstansby) - @dstansby
- [Dr. Andrew Annex](https://github.com/napari/napari/commits?author=AndrewAnnex) - @AndrewAnnex
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Eric Perlman](https://github.com/napari/napari/commits?author=perlman) - @perlman
- [Ganes Pandey](https://github.com/napari/napari/commits?author=pganes) - @pganes
- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [jaime rodriguez-guerra](https://github.com/napari/napari/commits?author=jaimergp) - @jaimergp
- [James Ryan](https://github.com/napari/napari/commits?author=jamesyan-git) - @jamesyan-git
- [Johannes Soltwedel](https://github.com/napari/napari/commits?author=jo-mueller) - @jo-mueller
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Jules Vanaret](https://github.com/napari/napari/commits?author=jules-vanaret) - @jules-vanaret
- [Kabilar Gunalan](https://github.com/napari/napari/commits?author=kabilar) - @kabilar
- [Kandarp Khandwala](https://github.com/napari/napari/commits?author=kandarpksk) - @kandarpksk
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kim Pevey](https://github.com/napari/napari/commits?author=kcpevey) - @kcpevey
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Konstantin Sofiiuk](https://github.com/napari/napari/commits?author=ksofiyuk) - @ksofiyuk
- [kyle i. s. harrington](https://github.com/napari/napari/commits?author=kephale) - @kephale
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Lucy Liu](https://github.com/napari/napari/commits?author=lucyleeow) - @lucyleeow
- [M Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Markus Stabrin](https://github.com/napari/napari/commits?author=mstabrin) - @mstabrin
- [Martin Weigert](https://github.com/napari/napari/commits?author=maweigert) - @maweigert
- [Melissa Weber Mendonça](https://github.com/napari/napari/commits?author=melissawm) - @melissawm
- [Nathan Clack](https://github.com/napari/napari/commits?author=nclack) - @nclack
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [odinsbane](https://github.com/napari/napari/commits?author=odinsbane) - @odinsbane
- [pam wadhwa](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Stefan van der Walt](https://github.com/napari/napari/commits?author=stefanv) - @stefanv
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Wouter-Michiel Vierdag](https://github.com/napari/napari/commits?author=melonora) - @melonora
- [Ziyang Liu](https://github.com/napari/napari/commits?author=liu-ziyang) - @liu-ziyang


## 18 docs authors added to this release (alphabetical)

- [andrew sweet](https://github.com/napari/docs/commits?author=andy-sweet) - @andy-sweet
- [Ashley Anderson](https://github.com/napari/docs/commits?author=aganders3) - @aganders3
- [Daniel Althviz Moré](https://github.com/napari/docs/commits?author=dalthviz) - @dalthviz
- [David Stansby](https://github.com/napari/docs/commits?author=dstansby) - @dstansby
- [Draga Doncila Pop](https://github.com/napari/docs/commits?author=DragaDoncila) - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/docs/commits?author=Czaki) - @Czaki
- [jaime rodriguez-guerra](https://github.com/napari/docs/commits?author=jaimergp) - @jaimergp
- [James Ryan](https://github.com/napari/docs/commits?author=jamesyan-git) - @jamesyan-git
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Kabilar Gunalan](https://github.com/napari/docs/commits?author=kabilar) - @kabilar
- [Lorenzo Gaifas](https://github.com/napari/docs/commits?author=brisvag) - @brisvag
- [Lucy Liu](https://github.com/napari/docs/commits?author=lucyleeow) - @lucyleeow
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [niklas netter](https://github.com/napari/docs/commits?author=gatoniel) - @gatoniel
- [Peter Sobolewski](https://github.com/napari/docs/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Sean Martin](https://github.com/napari/docs/commits?author=seankmartin) - @seankmartin
- [Vince](https://github.com/napari/docs/commits?author=vreuter) - @vreuter
- [Wouter-Michiel Vierdag](https://github.com/napari/docs/commits?author=melonora) - @melonora


## 19 docs reviewers added to this release (alphabetical)

- [alister burt](https://github.com/napari/docs/commits?author=alisterburt) - @alisterburt
- [andrew sweet](https://github.com/napari/docs/commits?author=andy-sweet) - @andy-sweet
- [Ashley Anderson](https://github.com/napari/docs/commits?author=aganders3) - @aganders3
- [Daniel Althviz Moré](https://github.com/napari/docs/commits?author=dalthviz) - @dalthviz
- [Draga Doncila Pop](https://github.com/napari/docs/commits?author=DragaDoncila) - @DragaDoncila
- [Genevieve Buckley](https://github.com/napari/docs/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Grzegorz Bokota](https://github.com/napari/docs/commits?author=Czaki) - @Czaki
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/docs/commits?author=kevinyamauchi) - @kevinyamauchi
- [kyle i. s. harrington](https://github.com/napari/docs/commits?author=kephale) - @kephale
- [Lorenzo Gaifas](https://github.com/napari/docs/commits?author=brisvag) - @brisvag
- [Lucy Liu](https://github.com/napari/docs/commits?author=lucyleeow) - @lucyleeow
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [nadalyn miller](https://github.com/napari/docs/commits?author=Nadalyn-CZI) - @Nadalyn-CZI
- [niklas netter](https://github.com/napari/docs/commits?author=gatoniel) - @gatoniel
- [Peter Sobolewski](https://github.com/napari/docs/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Sean Martin](https://github.com/napari/docs/commits?author=seankmartin) - @seankmartin
- [Vince](https://github.com/napari/docs/commits?author=vreuter) - @vreuter
- [Wouter-Michiel Vierdag](https://github.com/napari/docs/commits?author=melonora) - @melonora

## New Contributors

There are 11 new contributors for this release:

- Amirreza Aflakparast [napari](https://github.com/napari/napari/commits?author=AmirAflak) - @AmirAflak
- Daniel Zhang [napari](https://github.com/napari/napari/commits?author=DanGonite57) - @DanGonite57
- David Paleček [napari](https://github.com/napari/napari/commits?author=palec87) - @palec87
- David Pinto [napari](https://github.com/napari/napari/commits?author=MarchisLost) - @MarchisLost
- Dr. Andrew Annex [napari](https://github.com/napari/napari/commits?author=AndrewAnnex) - @AndrewAnnex
- Johannes Soltwedel [napari](https://github.com/napari/napari/commits?author=jo-mueller) - @jo-mueller
- niklas netter [docs](https://github.com/napari/docs/commits?author=gatoniel) - @gatoniel
- odinsbane [napari](https://github.com/napari/napari/commits?author=odinsbane) - @odinsbane
- Sam Cunliffe [napari](https://github.com/napari/napari/commits?author=samcunliffe) - @samcunliffe
- Stefan van der Walt [napari](https://github.com/napari/napari/commits?author=stefanv) - @stefanv
- Vince [docs](https://github.com/napari/docs/commits?author=vreuter) - @vreuter
