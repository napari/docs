# napari 0.4.17

We're happy to announce the release of napari 0.4.17!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).


For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## Highlights

This release is focused on documentation improvements and bug fixes, with few changes to napari’s API.
We picked out a few highlights, but keep reading below for the full list of changes!

### Minimum blending and inverted colormaps

We added a new blending mode, `minimum`, in {pr}`4875`, along with some inverted colormaps by @cleterrier.
The new mode and colormaps enable visualizing data as color intensities on a white background.
This is particularly nice when using the Light theme.
For more inspiration see [#invertedLUT on Twitter](https://twitter.com/hashtag/invertedLUT)
and the built-in napari example [examples/minimum_blending.py](https://github.com/napari/napari/blob/main/examples/minimum_blending.py).

### Option to edit second shortcut in preferences

We improved customization of napari preferences by allowing you to define a second,
alternative shortcut for each napari action.
This allows you, for example, to have both numeric (e.g. 1, 2, 3 - related to button positions) and semantic (F - for fill) shortcuts
defined for use in napari.

### One line image loading

We added `napari.imshow` in {pr}`4928` as a convenience function to load image data and return both a `Viewer` and the image `Layer` all in one line.

```python
viewer, layer = napari.imshow(data)
```

See the docstring of `napari.imshow` for more details.

### Experimental support for Qt6

We added some basic support for PyQt6 and PySide6 in {pr}`3707`, though we expect some issues.
If you need or want to use Qt6, please try this out and report any bugs you find.

### Multi-color text

We added support for assigning multiple colors for text annotations of points and shapes in {pr}`4464`.
See [examples/add_points_with_multicolor_text.py](https://github.com/napari/napari/blob/main/examples/add_points_with_multicolor_text.py)
This uses the API that we intend to spread elsewhere for other style attributes like `Points.face_color`,
so if you are a heavy user of those types of attributes you should try this out and leave feedback on Zulip
or create issues on GitHub.


## New Features

- Multi-color text with color encodings ({pr}`4464`)
- add layer reader in tooltip and info dialog ({pr}`4664`)
- Feature: Minimum blending ({pr}`4875`)
- Add option for forcing plugin choice when opening files in the GUI ({pr}`4882`)
- Add saving folders to preferences ({pr}`4902`)
- Add napari.imshow to return viewer and layers ({pr}`4928`)
- Option to load all dock widgets ({pr}`4954`)
- Feature: register a keyboard shortcut for `preserve_labels` checkbox ({pr}`5017`)
- Add option to edit second shortcut in settings ({pr}`5018`)
- Autorepeatable keybindings & keybindings for label brush size ({pr}`5086`)

## Improvements

- support PyQt6, remove logic for `compile_qt_svgs` ({pr}`3707`)
- Improvements on scale bar ({pr}`4511`)
- allow use of validate_all=True on nested evented models ({pr}`4551`)
- Add modal dialogs for window/application closure ({pr}`4637`)
- Optimization: convert point slice indices to floats ({pr}`4648`)
- honor confirm close settings when quitting ({pr}`4700`)
- Use custom color field classes in all models ({pr}`4704`)
- napari.viewer.current_viewer fallback ancestor ({pr}`4715`)
- Add public API for dims transpose ({pr}`4727`)
- Add a public API for the setGeometry method of _qt_window ({pr}`4729`)
- Expose points layer antialiasing control publicly ({pr}`4735`)
- Use `npe2 list` to show plugin info ({pr}`4739`)
- Allow pandas.Series as properties values ({pr}`4755`)
- Allow stack to be specified multiple times ({pr}`4783`)
- Refactor: use app-model and in-n-out ({pr}`4784`)
- Fix point `experimental_canvas_size_limits` and set sane defaults ({pr}`4790`)
- Improve "select all" logic in points layer, adding "select all across slices" behavior ({pr}`4809`)
- Make docked widgets of `qt_viewer` lazy ({pr}`4811`)
- Restore Labels, Points and Shapes layer mode after hold key ({pr}`4814`)
- Confirmation on close, alternative approach ({pr}`4820`)
- add path specificity scoring ({pr}`4830`)
- [Automatic] Update albertosottile/darkdetect vendored module ({pr}`4845`)
- Add plugin reader warning dialog ({pr}`4852`)
- Fix `python` name in macOS menu bar ({pr}`4989`)
- Explicit convert color to string when compile resources ({pr}`4997`)
- Add link to docs artifact to pull requests ({pr}`5014`)
- Reverse order of plugin name and widget name ({pr}`5054`)

## Performance

- Optimization: convert vector slice indices to floats ({pr}`4794`)

## Bug Fixes

- Fix: Always save settings after migration ({pr}`4490`)
- Make sure reader dialog pops open if File -> Open Sample is compatible with multiple readers ({pr}`4500`)
- Do not add duplicate layers ({pr}`4544`)
- Disconnect a removed slider's _pull_label callback from the axis label change event  ({pr}`4557`)
- Clean status message after leave canvas ({pr}`4607`)
- Alternate fix for alt-text issues ({pr}`4617`)
- Fix numpy version comparison for dev versions of numpy ({pr}`4622`)
- Restore "show all key bindings" shortcut  ({pr}`4628`)
- Raise error when rgb True but data not correct dims ({pr}`4630`)
- Define different shortcuts for different screenshot actions in file menu ({pr}`4636`)
- Do not use keyword argument for `QListWidgetItem` parent set in constructor ({pr}`4661`)
- fix: fix manifest reader extensions, ensure that all builtins go through npe2 ({pr}`4668`)
- Fix source of copied layer events by use `layer.as_layer_data_tuple` ({pr}`4681`)
- Tracks tail update fix beyond _max_length ({pr}`4688`)
- Keep order of layers when select to save multiple selected layers ({pr}`4689`)
- Apply shown mask to points._view_size_scale ({pr}`4699`)
- Color edit without tooltip fix ({pr}`4717`)
- fix presentation and enablement of npe1 plugins ({pr}`4721`)
- fix clim init for dask arrays ({pr}`4724`)
- split Image `interpolation` on two properties, `interpoltion2d` and `interpolation3d`  ({pr}`4725`)
- Fix bug in deepcopy of utils.context.Expr ({pr}`4730`)
- Fix `_get_state` for empty Vectors and Points layers ({pr}`4748`)
- Stop slider animation on display and dimension changes ({pr}`4761`)
- Fix deepcopy for trans objects when passing args ({pr}`4786`)
- Make newly added points editable ({pr}`4829`)
- Allow empty tuple layer to be returned #4571 ({pr}`4831`)
- Disable notifications if no main window ({pr}`4839`)
- Fix multiscale level selection when zoomed out ({pr}`4842`)
- Move vector mesh generation to napari vispy visual and fix vectors refesh ({pr}`4846`)
- Fix creation `QtViewer` for `ViewerModel` with already added layers ({pr}`4854`)
- Update hub.py ({pr}`4863`)
- Fix viewer.reset() throws TypeError ({pr}`4868`)
- fix icon urls for close dialog ({pr}`4887`)
- Fix missing slice from dims ({pr}`4889`)
- Raise exception when layer created with a scale value of 0 ({pr}`4906`)
- Fix for display of label colors ({pr}`4935`)
- Initialize plugins before validating widget in `napari -w {plugin}` ({pr}`4948`)
- Fix resize window problem by to long text in help  ({pr}`4981`)
- Fix throttled status updates by ensuring GUI updates occur on the main thread ({pr}`4983`)
- Fix throttled status updates by use `QSignalThrottler` in `_QtMainWindow` constructor ({pr}`4985`)
- Ensure non-negative edge width ({pr}`5035`)
- Fix the wrong guardian for the build tooltip when bind button ({pr}`5075`)
- disable mip and minip cutoffs if opaque blending ({pr}`5085`)
- Fix blending presets. ({pr}`5087`)
- Bugfix:  disable opacity slider for opaque blending ({pr}`5088`)
- Add extra garbage collection for some viewer tests ({pr}`5108`)
- Fix typestub and check manifest problems with build package ({pr}`5112`)
- Fix error with "None" key press ({pr}`5115`)
- Fix shortcuts deleting ({pr}`5119`)
- Standardise file extension when reading ({pr}`5121`)
- Fix slow points ({pr}`5133`)
- Use cross shape when cursor is small ({pr}`5141`)

## API Changes

- Removed unused private Layer._position ({pr}`4604`)
- Add public API for dims transpose ({pr}`4727`)
- Add a public API for the setGeometry method of _qt_window ({pr}`4729`)
- Expose points layer antialiasing control publicly ({pr}`4735`)

## Deprecations

- Deprecate layers.move_selected ({pr}`4559`)
- Update deprecation warnings with versions ({pr}`4757`)
- Make `viewer.events.layers_change` event deprecated ({pr}`4895`)

## Build Tools

- [pre-commit.ci] pre-commit autoupdate ({pr}`4506`)
- Limit workflows runs based on file changes ({pr}`4555`)
- [Automatic] Update albertosottile/darkdetect vendored module ({pr}`4561`)
- Dockerfile: stay on 20.04/LTS for python3.8 ({pr}`4572`)
- Block lxml 4.9.0 version ({pr}`4616`)
- Remove meshzoo from napari ({pr}`4620`)
- ci(dependabot): bump peter-evans/create-pull-request from 3 to 4 ({pr}`4675`)
- ci(dependabot): bump docker/build-push-action from 2.5.0 to 3 ({pr}`4676`)
- ci(dependabot): bump actions/setup-python from 3 to 4 ({pr}`4677`)
- ci(dependabot): bump toshimaru/auto-author-assign from 1.3.4 to 1.5.0 ({pr}`4678`)
- ci(dependabot): bump docker/metadata-action from 3 to 4 ({pr}`4679`)
- ci(dependabot): bump styfle/cancel-workflow-action from 0.9.1 to 0.10.0 ({pr}`4770`)
- ci(dependabot): bump actions/download-artifact from 2 to 3 ({pr}`4771`)
- ci(dependabot): bump actions/github-script from 5 to 6 ({pr}`4772`)
- ci(dependabot): bump bruceadams/get-release from 1.2.2 to 1.2.3 ({pr}`4773`)
- ci(dependabot): bump docker/login-action from 1.9.0 to 2 ({pr}`4774`)
- Bump vispy 0.11.0 ({pr}`4778`)
- [pre-commit.ci] pre-commit autoupdate ({pr}`4779`)
- ci(dependabot): bump toshimaru/auto-author-assign from 1.5.0 to 1.6.1 ({pr}`4890`)
- Docker: Update xpra's apt too ({pr}`4901`)

## Documentation

- Proposal to accept NAP-1 - add institutional and funding partners to governance ({pr}`4458`)
- Fix ImportErrors for instance attributes when building docs ({pr}`4471`)
- Update viewer tutorial ({pr}`4473`)
- Fix selection events documentation for LayerList  ({pr}`4478`)
- add ABRF LMRG workshop recording ({pr}`4487`)
- Add alt_text ({pr}`4502`)
- DOC: misc syntax updates and typoes ({pr}`4517`)
- Start a NAP about conda packaging for napari ({pr}`4519`)
- Add CZI as an Institutional and Funding Partner ({pr}`4524`)
- add I2K workshop ({pr}`4528`)
- Add NAP1 to ToC. ({pr}`4552`)
- Forward port of release note updates for 0.4.16rc2 and rc3 ({pr}`4563`)
- Add option to use npe2 shim/adaptor for npe1 plugins ({pr}`4564`)
- Forward port further 0.4.16 release note changes ({pr}`4592`)
- Discuss the approval of NAP-2 (conda-based packaging for napari) ({pr}`4602`)
- Add versioned API docs workflow ({pr}`4635`)
- Update installation instruction in documentation ({pr}`4639`)
- Fix docs for shape/points layer properties ({pr}`4659`)
- Embeding viewers in plugins widget example ({pr}`4665`)
- Add NAP-3: Spaces ({pr}`4684`)
- Fix NAP-1 status/type ({pr}`4685`)
- Add new core devs to docs ({pr}`4691`)
- add 'napari-xpra' target to dockerfile ({pr}`4703`)
- Fix Image parameter docs ({pr}`4750`)
- Make references to examples link there ({pr}`4767`)
- Add documentation about apply napari style to separate windows ({pr}`4780`)
- Fix documentation link errors. ({pr}`4787`)
- Fixing readme typo ({pr}`4791`)
- Add Talley to the steering council ({pr}`4798`)
- Update documenation : install plugin from URL  ({pr}`4799`)
- Accept NAP-2: Distributing napari with conda-based packaging ({pr}`4810`)
- Fixes duplicate label warnings in the documentation ({pr}`4823`)
- added description of how to save layers without compression ({pr}`4832`)
- Add the ability to return a List[Layer] in magicgui ({pr}`4851`)
- Fix NAP-3 table of contents ({pr}`4872`)
- Feature: Minimum blending ({pr}`4875`)
- NAP 4: asynchronous slicing ({pr}`4892`)
- Correct minor typo in quick_start.md ({pr}`4908`)
- Add Google Calendar ID to directive ({pr}`4914`)
- Fix docs dependencies ({pr}`4915`)
- Maintenance: Add title to example and remove unused redirect configuration ({pr}`4921`)
- Use `napari/packaging` for Conda CI ({pr}`4923`)
- Correct minor typos on 'Contributing resources' page ({pr}`4927`)
- DOC Add docs on napari models and events ({pr}`4929`)
- DOC Fix add image examples ({pr}`4932`)
- add SciPy 2022 materials ({pr}`4934`)
- Remove repeated items in gallery ToC. ({pr}`4936`)
- DOC Remove references to old `add_volume` ({pr}`4939`)
- Fix calendar ID ({pr}`4944`)
- DOC Add docs on how to run napari headless ({pr}`4955`)
- Removes deprecated configuration options for notebooks from docs build ({pr}`4958`)
- Update async slicing discussion section with PR feedback ({pr}`4959`)
- DOC Add section on downloading CI built docs ({pr}`4961`)
- DOC Expand explanation of interaction_box_image example ({pr}`4962`)
- DOC: Fix some incorrect parameters names. ({pr}`4965`)
- DOC Add headless doc to toc ({pr}`4970`)
- Remove preliminary admonition for last two release notes ({pr}`4974`)
- Enabe tags in gallery examples. ({pr}`4975`)
- Update viewer screenshot in docs and make more prominent on napari.org ({pr}`4988`)
- Move the docs downloading screenshots to LFS ({pr}`4990`)
- DOC Enable intersphinx linking in examples ({pr}`4992`)
- Fix broken links in Napari Code of Conduct ({pr}`5005`)
- Add linkcheck ({pr}`5008`)
- Add link to docs artifact to pull requests ({pr}`5014`)
- Add release notes for 0.4.17 ({pr}`5031`)
- add #4954 to release notes ({pr}`5038`)
- add new PRs merged for 0.4.17 to release notes ({pr}`5045`)
- Proposal to accept NAP #4: asynchronous slicing ({pr}`5052`)
- Update v0.4.17.rc0 release notes ({pr}`5058`)
- update core dev group to remove Ziyang and Justine ({pr}`5059`)
- Better script for prepare release notes ({pr}`5061`)
- Bugfix:  disable opacity slider for opaque blending ({pr}`5088`)
- Update links in NAP-2 ({pr}`5099`)
- Update release notes for v0.4.17rc1 ({pr}`5110`)
- Update release notes for v0.4.17rc3 ({pr}`5147`)

## Other Pull Requests

- Fire features event on Labels feature change ({pr}`4481`)
- Image layer control dtype normalization for tensorstore compatibility ({pr}`4482`)
- Reorder tests ({pr}`4483`)
- Test if events for all properties are defined ({pr}`4486`)
- throttle status update ({pr}`4488`)
- use inject_napari_dependencies in layer_actions commands ({pr}`4489`)
- Add _get_value_3d to surface ({pr}`4492`)
- Reduce canvas margin ({pr}`4496`)
- Fix trailing comma fixes black formatting ({pr}`4498`)
- Update layer list context keys ({pr}`4499`)
- Do not allow None when coercing encodings ({pr}`4504`)
- [Automatic] Update albertosottile/darkdetect vendored module ({pr}`4508`)
- Try to upload pytest json report as artifact. ({pr}`4518`)
- Try to speedup tests. ({pr}`4521`)
- change default blending mode on image layer to translucent no depth ({pr}`4523`)
- Accessor refactor ({pr}`4533`)
- Add explanation what `EmitterGroup.block_all` and `EmitterGroup.unblock_all` do in docstring ({pr}`4536`)
- Revert "change default blending mode on image layer to translucent no depth" ({pr}`4540`)
- add ci for asv benchmark suite ({pr}`4554`)
- Fixes/modifications to nested list model and Group in prep for layergroups ({pr}`4560`)
- Fix macos release version comparison in __main__ ({pr}`4565`)
- Update base docker image to ubuntu 22.04, optimize container size. ({pr}`4568`)
- Patch scikit-image cells3d data function when testing examples ({pr}`4578`)
- Add question about qt backends to PR tests ({pr}`4583`)
- Don't build bundle in PRs on doc changes ({pr}`4584`)
- Fix Auto-open trans issue. ({pr}`4586`)
- Internationalisation testing. ({pr}`4588`)
- Add test for QtPerformance widget ({pr}`4591`)
- Split coverage on parts ({pr}`4595`)
- More updates to the ignored translations file and translation CI infrastructure ({pr}`4596`)
- feat: add codespace ({pr}`4599`)
- Enable patch coverage reporting ({pr}`4632`)
- Add tests for qt_progress_bar.py ({pr}`4634`)
- Remove some sleepy tests, wait with timeout instead ({pr}`4638`)
- Speed up notebook display tests  ({pr}`4641`)
- build: slight updates/de-dups in setupcfg ({pr}`4645`)
- test: Speed up test_viewer tests, split out pyqt5/pyside2 tests again ({pr}`4646`)
- Move test examples on end of test run them in different CI job  ({pr}`4647`)
- Allow to trigger test_translation manually ({pr}`4652`)
- Limit comprehensive test concurrency to 1. ({pr}`4655`)
- Do not run `asv` on push ({pr}`4656`)
- ci: fix tox factor names in tests ({pr}`4660`)
- test: speed up magicgui forward ref tests ({pr}`4662`)
- Remove unused points _color state ({pr}`4666`)
- test: Cleanup usage of npe2 plugin manager in tests ({pr}`4669`)
- add dependabot for github actions dependencies ({pr}`4671`)
- Use `cache: pip` from actions setup-python ({pr}`4672`)
- Remove `restore_settings_on_exit` test util ({pr}`4673`)
- bump npe2 version, use new features ({pr}`4686`)
- [pre-commit.ci] pre-commit autoupdate ({pr}`4687`)
- Remove unnecessary uses of make_napari_viewer (replace with ViewerModel) ({pr}`4690`)
- Design issue template assignees ({pr}`4701`)
- Refactor label painting by moving code from mouse bindings onto layer, adding staged history and paint event ({pr}`4702`)
- Split out builtins into another top-level module ({pr}`4706`)
- use python 3.9 for mac tests until numcodecs 3.10 wheels are available ({pr}`4707`)
- Remove print statement in settings ({pr}`4718`)
- Use some features from npe2 v0.5.0 ({pr}`4719`)
- use same coverage report like in pull requests ({pr}`4722`)
- Update translation documentation link in pull request template ({pr}`4728`)
- Cleanup list of non-translatable strings. ({pr}`4732`)
- Add mini interactive prompt to edit string_list.json ({pr}`4733`)
- Do not inform about coverage untill all CI jobs are done ({pr}`4751`)
- Refactor `NapariQtNotification` test for better cleaning Qt objects ({pr}`4763`)
- Set focus on `QtViewer` object after creating main window ({pr}`4768`)
- Add missed call of `running_as_bundled_app` in `__main__` ({pr}`4777`)
- test: fix ability to use posargs with tox ({pr}`4788`)
- Allow dunder methods use in `PublicOnlyProxy` ({pr}`4792`)
- add update_mesh method ({pr}`4793`)
- mock npe1 plugin manager during tests (fix tests with npe1 plugins installed) ({pr}`4806`)
- [Automatic] Update albertosottile/darkdetect vendored module ({pr}`4808`)
- Improve using Qt flags by direct use enums. ({pr}`4817`)
- Move searching parent outside NapariQtNotification constructor ({pr}`4841`)
- Enable plugin menu contributions with app-model ({pr}`4847`)
- Raise better errors from lazy __getattr__ ({pr}`4848`)
- Allow to undock docked viewers in multiple viewers example ({pr}`4859`)
- MAINT: disable failing conda bundling. ({pr}`4878`)
- MAINT: Work around conda bundling issue. ({pr}`4883`)
- remove a few more qtbot.wait calls in tests ({pr}`4888`)
- use npe2api in plugin install dialog ({pr}`4893`)
- Add perfmon directory for shared configs and tools ({pr}`4898`)
- Conda: fix MacOS signing ({pr}`4904`)
- Improve error message for a failed write ({pr}`4913`)
- Minor type fix (add Optional) ({pr}`4916`)
- add user keymap ({pr}`4946`)
- MAINT: temporary mypy disabling as it's failing everywhere. ({pr}`4950`)
- Adjust the slider value to include current_size ({pr}`4951`)
- MAINT: re-enable type checking workflow ({pr}`4960`)
- MAINT: bump napari-console to 0.0.6. ({pr}`4967`)
- [pre-commit.ci] pre-commit autoupdate ({pr}`4968`)
- Fix: bump app-model, add test for layer buttons ({pr}`4972`)
- Add `FUNDING.yml` file to enable sponsor button and increase discoverability of option to sponsor napari ({pr}`4978`)
- Start adding a CODEOWNERS file. ({pr}`4993`)
- Add emacs temporary & local files to .gitignore ({pr}`4998`)
- Set fixpoint before move for shapes ({pr}`4999`)
- Fix sys.path issue with subprocess relaunch in macOS ({pr}`5007`)
- MAINT: update issue failing template ({pr}`5012`)
- [pre-commit.ci] pre-commit autoupdate ({pr}`5015`)
- Fix shift selection for points ({pr}`5022`)
- Revert "Fix sys.path issue with subprocess relaunch in macOS" ({pr}`5027`)
- Use Source object to track if a layer is duplicated ({pr}`5028`)
- Revert "Revert "Fix sys.path issue with subprocess relaunch in macOS"" ({pr}`5029`)
- update some of the ignored translations ({pr}`5032`)
- MAINT: fix a couple of trans._. ({pr}`5034`)
- MAINT: Update Future Warning. ({pr}`5037`)
- MAINT: Unnecessary formatting of constant. ({pr}`5044`)
- Small shortcuts preference pane wording update after #5018 ({pr}`5049`)
- Small changes to points defaults. ({pr}`5050`)
- MAINT: Don't deprecate something that was never stable. ({pr}`5068`)
- Try to avoid latest shiboken that break CI ({pr}`5073`)
- Add new core libraries to napari info ({pr}`5077`)
- Update config directory paths for perfmon tools ({pr}`5081`)
- Update some strings to be translated, some to be ignored ({pr}`5082`)


## 48 authors added to this release (alphabetical)

- [alisterburt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [Andy Sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Ashley Anderson](https://github.com/napari/napari/commits?author=aganders3) - @aganders3
- [Cajon Gonzales](https://github.com/napari/napari/commits?author=cajongonzales) - @cajongonzales
- [chili-chiu](https://github.com/napari/napari/commits?author=chili-chiu) - @chili-chiu
- [cnstt](https://github.com/napari/napari/commits?author=cnstt) - @cnstt
- [Curtis Rueden](https://github.com/napari/napari/commits?author=ctrueden) - @ctrueden
- [David Stansby](https://github.com/napari/napari/commits?author=dstansby) - @dstansby
- [dependabot[bot]](https://github.com/napari/napari/commits?author=dependabot[bot]) - @dependabot[bot]
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Eric Perlman](https://github.com/napari/napari/commits?author=perlman) - @perlman
- [Gabriel Selzer](https://github.com/napari/napari/commits?author=gselzer) - @gselzer
- [github-actions[bot]](https://github.com/napari/napari/commits?author=github-actions[bot]) - @github-actions[bot]
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Guillaume Witz](https://github.com/napari/napari/commits?author=guiwitz) - @guiwitz
- [Jaime Rodríguez-Guerra](https://github.com/napari/napari/commits?author=jaimergp) - @jaimergp
- [James Ryan](https://github.com/napari/napari/commits?author=jamesyan-git) - @jamesyan-git
- [Jeremy Asuncion](https://github.com/napari/napari/commits?author=codemonkey800) - @codemonkey800
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kandarp Khandwala](https://github.com/napari/napari/commits?author=kandarpksk) - @kandarpksk
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kim Pevey](https://github.com/napari/napari/commits?author=kcpevey) - @kcpevey
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Kushaan Gupta](https://github.com/napari/napari/commits?author=kushaangupta) - @kushaangupta
- [Kyle I S Harrington](https://github.com/napari/napari/commits?author=kephale) - @kephale
- [laysa uchoa](https://github.com/napari/napari/commits?author=laysauchoa) - @laysauchoa
- [Lia Prins](https://github.com/napari/napari/commits?author=liaprins-czi) - @liaprins-czi
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Lucy Liu](https://github.com/napari/napari/commits?author=lucyleeow) - @lucyleeow
- [Markus Stabrin](https://github.com/napari/napari/commits?author=mstabrin) - @mstabrin
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Melissa Weber Mendonça](https://github.com/napari/napari/commits?author=melissawm) - @melissawm
- [Nathan Clack](https://github.com/napari/napari/commits?author=nclack) - @nclack
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pam](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Pierre Thibault](https://github.com/napari/napari/commits?author=pierrethibault) - @pierrethibault
- [pre-commit-ci[bot]](https://github.com/napari/napari/commits?author=pre-commit-ci[bot]) - @pre-commit-ci[bot]
- [Robert Haase](https://github.com/napari/napari/commits?author=haesleinhuepf) - @haesleinhuepf
- [Robin Koch](https://github.com/napari/napari/commits?author=RobAnKo) - @RobAnKo
- [rwkozar](https://github.com/napari/napari/commits?author=rwkozar) - @rwkozar
- [Ryan Savill](https://github.com/napari/napari/commits?author=Cryaaa) - @Cryaaa
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Tru Huynh](https://github.com/napari/napari/commits?author=truatpasteurdotfr) - @truatpasteurdotfr
- [vcwai](https://github.com/napari/napari/commits?author=victorcwai) - @victorcwai
- [Ziyang Liu](https://github.com/napari/napari/commits?author=potating-potato) - @potating-potato


## 32 reviewers added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [alisterburt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [Andy Sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [cnstt](https://github.com/napari/napari/commits?author=cnstt) - @cnstt
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Eric Perlman](https://github.com/napari/napari/commits?author=perlman) - @perlman
- [Gabriel Selzer](https://github.com/napari/napari/commits?author=gselzer) - @gselzer
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Isabela Presedo-Floyd](https://github.com/napari/napari/commits?author=isabela-pf) - @isabela-pf
- [Jaime Rodríguez-Guerra](https://github.com/napari/napari/commits?author=jaimergp) - @jaimergp
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Justin Kiggins](https://github.com/napari/napari/commits?author=neuromusic) - @neuromusic
- [Justine Larsen](https://github.com/napari/napari/commits?author=justinelarsen) - @justinelarsen
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kim Pevey](https://github.com/napari/napari/commits?author=kcpevey) - @kcpevey
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Kushaan Gupta](https://github.com/napari/napari/commits?author=kushaangupta) - @kushaangupta
- [Kyle I S Harrington](https://github.com/napari/napari/commits?author=kephale) - @kephale
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Lucy Liu](https://github.com/napari/napari/commits?author=lucyleeow) - @lucyleeow
- [Markus Stabrin](https://github.com/napari/napari/commits?author=mstabrin) - @mstabrin
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Melissa Weber Mendonça](https://github.com/napari/napari/commits?author=melissawm) - @melissawm
- [Nathan Clack](https://github.com/napari/napari/commits?author=nclack) - @nclack
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pam](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Robert Haase](https://github.com/napari/napari/commits?author=haesleinhuepf) - @haesleinhuepf
- [Robin Koch](https://github.com/napari/napari/commits?author=RobAnKo) - @RobAnKo
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Ziyang Liu](https://github.com/napari/napari/commits?author=potating-potato) - @potating-potato

