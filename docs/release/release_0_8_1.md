# napari 0.8.1
⚠️ *Note: these release notes are still in draft while 0.8.1a1 is in prerelease testing.* ⚠️

*Wed, Jul 29, 2026*

We're happy to announce the release of napari 0.8.1!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website,
https://napari.org.

napari follows [EffVer (Intended Effort Versioning)](https://effver.org/); this is a **Meso** release containing awesome new features, but some effort may be needed when updating previous projects to use this version.

## New Features

- feat: add `new` label button to the labels controls ([#9215](https://github.com/napari/napari/pull/9215))

## Improvements

- move features table widget command to the Metadata menu ([#9231](https://github.com/napari/napari/pull/9231))
- fix: change the order of edge/face color and border ([#9232](https://github.com/napari/napari/pull/9232))
- Move the layer lock to group with link/unlink, rather than with visib… ([#9235](https://github.com/napari/napari/pull/9235))

## Bug Fixes

- Fix multiscale level selection for anisotropic data ([#9201](https://github.com/napari/napari/pull/9201))
- Fix cross layer in multiple viewer example to use line vectors. ([#9213](https://github.com/napari/napari/pull/9213))
- Do not update `current_properties` on Shapes selection changed  ([#9221](https://github.com/napari/napari/pull/9221))
- fix: action binding the `new-label` tooltips  with shortcuts ([#9230](https://github.com/napari/napari/pull/9230))
- fix: add minimum value to grid mode strides to allow negative strides ([#9236](https://github.com/napari/napari/pull/9236))
- Fix sync slicing when toggling to 3D with auto contrast ([#9263](https://github.com/napari/napari/pull/9263))

## Documentation

- [pre-commit.ci] pre-commit autoupdate ([docs#1069](https://github.com/napari/docs/pull/1069))
- Update homepage video for 0.8 changes ([docs#1070](https://github.com/napari/docs/pull/1070))
- Start creating 0.8.1 release notes ([docs#1073](https://github.com/napari/docs/pull/1073))
- Enhance contributing documentation with GitHub edit info ([docs#1075](https://github.com/napari/docs/pull/1075))
- Adding uv to getting started - installation ([docs#1076](https://github.com/napari/docs/pull/1076))
- make napari logo usage page ([docs#1077](https://github.com/napari/docs/pull/1077))
- Delete useless line ([docs#1078](https://github.com/napari/docs/pull/1078))
- Update auto-fill-labels loop video to extend end frame ([docs#1082](https://github.com/napari/docs/pull/1082))

## Other Pull Requests

- Update label name in condition of label trigger build ([docs#1067](https://github.com/napari/docs/pull/1067))
- Update version switcher to point to 0.8.0 as stable ([docs#1071](https://github.com/napari/docs/pull/1071))
- Remove contributing text about adding translations ([docs#1081](https://github.com/napari/docs/pull/1081))
- Remove translations code ([#8935](https://github.com/napari/napari/pull/8935))
- fix(typing): add typing and fix mypy error in `qt_mode_buttons.py` ([#9110](https://github.com/napari/napari/pull/9110))
- Use shared version of label clean workflow ([#9116](https://github.com/napari/napari/pull/9116))
- fix(typing): add typing and fix mypy error in `qt_face_color.py`  ([#9123](https://github.com/napari/napari/pull/9123))
- fix(typing): add typing and fix mypy error in `_base_item_model.py` ([#9126](https://github.com/napari/napari/pull/9126))
- fix(typing): add typing and fix mypy error in `_base_item_view.py` ([#9127](https://github.com/napari/napari/pull/9127))
- fix(typing): add typing and fix mypy error in `qt_axis_model.py` ([#9167](https://github.com/napari/napari/pull/9167))
- fix(typing): add typing and fix mypy error in `qt_list_model.py` ([#9169](https://github.com/napari/napari/pull/9169))
- fix(typing): add typing and fix mypy error in `qt_border_color.py` ([#9179](https://github.com/napari/napari/pull/9179))
- fix(typing): resolve mypy errors for `qt_widget_controls_base` ([#9185](https://github.com/napari/napari/pull/9185))
- Update `coverage`, `dask`, `hypothesis`, `imageio`, `matplotlib`, `platformdirs`, `tifffile`, `tqdm`, `virtualenv`, `xarray` ([#9194](https://github.com/napari/napari/pull/9194))
- [pre-commit.ci] pre-commit autoupdate ([#9197](https://github.com/napari/napari/pull/9197))
- Add ``example`` to ``allowed_labels`` in ``check_labels`` job of ``label_and_milestone_checker.yml`` workflow ([#9214](https://github.com/napari/napari/pull/9214))
- TST: parameterizing with iterables is deprecated in pytest ([#9217](https://github.com/napari/napari/pull/9217))
- Make tensorstore optional dependency of `test_labels` again ([#9220](https://github.com/napari/napari/pull/9220))
- Disable part of test matrix to increase runner availability during sprints/hackathon ([#9226](https://github.com/napari/napari/pull/9226))
- Add (Euro)SciPy Sprint Authors to Citation ([#9234](https://github.com/napari/napari/pull/9234))
- fix(typing): add typing and fix mypy error in `qt_brush_size_slider.py` ([#9238](https://github.com/napari/napari/pull/9238))
- Gallery example of using a background map ([#9245](https://github.com/napari/napari/pull/9245))
- Adding 4D sample data as a heat diffusion ([#9246](https://github.com/napari/napari/pull/9246))
- Disable interaction with vispy.gloo in test_vispy_labels_polygon_overlay ([#9264](https://github.com/napari/napari/pull/9264))
- ci(dependabot): bump the actions group across 1 directory with 11 updates ([#9265](https://github.com/napari/napari/pull/9265))
- Remove missing translations GH action ([#9266](https://github.com/napari/napari/pull/9266))
- Asynchronous loading text fix ([#9267](https://github.com/napari/napari/pull/9267))
- Pin octokit to tag, not use main branch ([#9268](https://github.com/napari/napari/pull/9268))


## 18 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Aniket](https://github.com/napari/napari/commits?author=Aniketsy) - @Aniketsy
- [BadPrograms](https://github.com/napari/napari/commits?author=BadPrograms) - @BadPrograms +
- [Bas Bloemsaat](https://github.com/napari/napari/commits?author=basbloemsaat) - @basbloemsaat +
- [Edouard Coussoux](https://github.com/napari/napari/commits?author=ecoussoux-ansys) - @ecoussoux-ansys +
- [Filippo  Maria Castelli, PhD](https://github.com/napari/napari/commits?author=filippocastelli) - @filippocastelli +
- [girochat](https://github.com/napari/napari/commits?author=girochat) - @girochat +
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Jacopo Abramo](https://github.com/napari/napari/commits?author=jacopoabramo) - @jacopoabramo
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) ([docs](https://github.com/napari/docs/commits?author=jni))  - @jni
- [Kamil Kania](https://github.com/napari/napari/commits?author=Grzyb33k) - @Grzyb33k +
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [michalslabs](https://github.com/napari/napari/commits?author=michalslabs) ([docs](https://github.com/napari/docs/commits?author=michalslabs))  - @michalslabs +
- [Mridul Seth](https://github.com/napari/napari/commits?author=MridulS) - @MridulS +
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Revathy Venugopal](https://github.com/napari/napari/commits?author=Revathyvenugopal162) - @Revathyvenugopal162 +
- [Sara Czasak](https://github.com/napari/docs/commits?author=sara-czasak) - @sara-czasak +
- [Sébastien Morais](https://github.com/napari/napari/commits?author=SMoraisAnsys) - @SMoraisAnsys +
- [Tim Monko](https://github.com/napari/docs/commits?author=TimMonko) - @TimMonko

## 13 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Aniket](https://github.com/napari/napari/commits?author=Aniketsy) - @Aniketsy
- [arbor](https://github.com/napari/docs/commits?author=arbormoss) - @arbormoss
- [Carol Willing](https://github.com/napari/docs/commits?author=willingc) - @willingc
- [Draga Doncila Pop](https://github.com/napari/docs/commits?author=DragaDoncila) - @DragaDoncila
- [girochat](https://github.com/napari/napari/commits?author=girochat) - @girochat +
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Jacopo Abramo](https://github.com/napari/napari/commits?author=jacopoabramo) - @jacopoabramo
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) ([docs](https://github.com/napari/docs/commits?author=jni))  - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Maxime Rey](https://github.com/napari/docs/commits?author=MaxJPRey) - @MaxJPRey
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Sara Czasak](https://github.com/napari/docs/commits?author=sara-czasak) - @sara-czasak +
- [Tim Monko](https://github.com/napari/docs/commits?author=TimMonko) - @TimMonko
