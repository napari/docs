# napari 0.6.4
⚠️ *Note: these release notes are still in draft while 0.6.4 is in release candidate testing.* ⚠️

*Tue, Aug 12, 2025*

We’re happy to announce the release of napari 0.6.4!

napari is a fast, interactive, multi-dimensional image viewer for Python. It’s designed for exploring, annotating, and analyzing multi-dimensional images. It’s built on Qt (for the GUI), VisPy (for performant GPU-based rendering), and the scientific Python stack (NumPy, SciPy, and friends).

For more information, examples, and documentation, please visit our website: https://napari.org/

## Highlights

### Run scripts with napari from the command line

As a follow-up to the ability to drag-n-drop scripts into the napari window from 0.6.3, you can now run scripts directly from the command line using the `napari` command and the path to the script ([#8185](https://github.com/napari/napari/pull/8185) and [#8187](https://github.com/napari/napari/pull/8187)). For example `napari examples/magic_immage_arithmetic.py` will open napari and run the local script.


## Improvements

- Remove old path handle in napari start ([#8185](https://github.com/napari/napari/pull/8185))
- Prevent `napari.run` from being executed when running scripts from napari ([#8187](https://github.com/napari/napari/pull/8187))

## Bug Fixes

- Set focus after toggling dockwidget via `DockWidgetToggleAction` ([#8182](https://github.com/napari/napari/pull/8182))
- Fix feature table widget sorting and editing of floats ([#8190](https://github.com/napari/napari/pull/8190))
- Explicit copy of layers data for balls example ([#8203](https://github.com/napari/napari/pull/8203))

## Documentation

- Reorganize bundle instructions page to make it easier to navigate and provide download links ([docs#813](https://github.com/napari/docs/pull/813))
- Simplify installation guide & better highlight bundle ([docs#814](https://github.com/napari/docs/pull/814))
- Update codespell config and minor corrections ([docs#816](https://github.com/napari/docs/pull/816))
- Add contracted roles to team page and rename core dev -> core TM ([docs#817](https://github.com/napari/docs/pull/817))

## Other Pull Requests

- Pin Github Actions actions to their hashes ([#8140](https://github.com/napari/napari/pull/8140))
- Move test that requires `make_napari_viewer` from `test_qt_viewer` ([#8176](https://github.com/napari/napari/pull/8176))
- Fix slider label shifted down, by overrwite QLineEdit qss rules ([#8184](https://github.com/napari/napari/pull/8184))
- [pre-commit.ci] pre-commit autoupdate ([#8193](https://github.com/napari/napari/pull/8193))
- Fix fallback version in setuptools_scm to pass schema validation ([#8196](https://github.com/napari/napari/pull/8196))
- Use napari url for test rather than Fiji ([#8198](https://github.com/napari/napari/pull/8198))
- [pre-commit.ci] pre-commit autoupdate ([#8204](https://github.com/napari/napari/pull/8204))
- Pin `pytest-qt` for python 3.10 to fix pyapp-kit projects tests ([#8205](https://github.com/napari/napari/pull/8205))
- Retry second fullscreen test ([#8206](https://github.com/napari/napari/pull/8206))
- Fix script for checking for updated dependecies. ([#8207](https://github.com/napari/napari/pull/8207))
- Update Version Switcher to 0.6.3 ([docs#808](https://github.com/napari/docs/pull/808))
- ci(dependabot): bump napari/napari from 0.6.2 to 0.6.3 in the github-actions group ([docs#810](https://github.com/napari/docs/pull/810))


## 8 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Carol Willing](https://github.com/napari/docs/commits?author=willingc) - @willingc
- [Daniel Althviz Moré](https://github.com/napari/napari/commits?author=dalthviz) - @dalthviz
- [Draga Doncila Pop](https://github.com/napari/docs/commits?author=DragaDoncila) - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [jaime rodraguez-guerra](https://github.com/napari/napari/commits?author=jaimergp) - @jaimergp
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Peter Sobolewski](https://github.com/napari/docs/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko


## 7 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Carol Willing](https://github.com/napari/docs/commits?author=willingc) - @willingc
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Sobolewski](https://github.com/napari/docs/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko

