# napari 0.7.1
⚠️ *Note: these release notes are still in draft while 0.7.1b1 is in prerelease testing.* ⚠️

*Thu, May 21, 2026*

We're happy to announce the release of napari 0.7.1!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website,
https://napari.org.

napari follows [EffVer (Intended Effort Versioning)](https://effver.org/); this is a **Meso** release containing awesome new features, but some effort may be needed when updating previous projects to use this version.

## Highlights


The napari 0.7.1 release is mainly a bug fix release, but it also includes some new features and improvements. Here are some of the highlights:

## Signed windows bundle

Since napari 0.7.1 our bundle on Windows is now [signed](https://github.com/napari/packaging/pull/387). It means that you should be able to run napari without any warnings about the application being from an unknown publisher. This is a great step forward for our Windows users, as it enhances security and trust in our application, especially on managed environments where unsigned applications may be blocked by default.

The certificate is issued for NumFOCUS foundation that provide legal representation for napari, and many other open source projects.
 
If you encounter any issues related to this change, please let us know!


## Selection of the rendered level for multiscale layers

Till napari 0.7.1 when render a multiscale layer in 3d, napari would always render the lowest resolution level of the pyramid. 
Thanks to [#8917](https://github.com/napari/napari/pull/8917) user can now select the level of the pyramid to render in 3d. 
This allows to have better resolution that previously and keep data enough small to fit in GPU memory.

![](https://github.com/user-attachments/assets/862e7512-0309-429c-b155-a9c03acf2db6)


## Colorbars for points layer

The points layer allow to color points based of their feature values. In napari 0.7.1 we added support for colorbars for points layer ([#8624](https://github.com/napari/napari/pull/8624)), so you can now easily see the mapping between feature values and colors. This is especially useful when you have a large number of points and want to quickly understand the distribution of feature values.



## New Features

- Add points layer face and border colorbar ([#8624](https://github.com/napari/napari/pull/8624))

## Improvements

- Add handler for show message when napari fails to import ([#8609](https://github.com/napari/napari/pull/8609))
- Add example driving computation from gui ([#8658](https://github.com/napari/napari/pull/8658))
- Example: Enhance theme sample widget with theme colors, widgets ([#8662](https://github.com/napari/napari/pull/8662))
- Do not connect to children events of EventedDict items if there is no callback ([#8673](https://github.com/napari/napari/pull/8673))
- ENH: For multiscale 2d: store materialized thumbnail_level ([#8715](https://github.com/napari/napari/pull/8715))
- Canvas based font size ([#8770](https://github.com/napari/napari/pull/8770))
- Enh, minor, builtins: use urllib (and defer) instead of requests if reading a remote script path ([#8785](https://github.com/napari/napari/pull/8785))
- Perf: Defer importing scipy.spatial ([#8789](https://github.com/napari/napari/pull/8789))
- Revert the switch from Welcome widget to Welcome overlay from #8117 ([#8793](https://github.com/napari/napari/pull/8793))
- Add handler for show message when napari fails to import v2 ([#8803](https://github.com/napari/napari/pull/8803))
- Update text in mac installer to improve UX ([#8806](https://github.com/napari/napari/pull/8806))
- Fix: Use Python's tokenize script decoding for builtin reader ([#8838](https://github.com/napari/napari/pull/8838))
- Add note for user how to reset the reader preference ([#8848](https://github.com/napari/napari/pull/8848))
- Ensure all napari and plugin commands use . instead of : ([#8883](https://github.com/napari/napari/pull/8883))
- Improve dask check to support more dask-backed array types ([#8896](https://github.com/napari/napari/pull/8896))
- Fix floating widgets and use custom title bar in all cases ([#8898](https://github.com/napari/napari/pull/8898))
- Set pixel as default scalebar unit ([#8900](https://github.com/napari/napari/pull/8900))
- Turn off contrast/color controls when surface has `vertex_colors` ([#8909](https://github.com/napari/napari/pull/8909))
- Actually use theme type from npe contrib ([#8915](https://github.com/napari/napari/pull/8915))
- Add multiscale level lock for scalar field layers ([#8917](https://github.com/napari/napari/pull/8917))
- Do not add a new colormap if one already exists in napari ([#8924](https://github.com/napari/napari/pull/8924))
- Improve sizing of dims ordering popup ([#8952](https://github.com/napari/napari/pull/8952))

## Performance

- ENH: For multiscale 2d: store materialized thumbnail_level ([#8715](https://github.com/napari/napari/pull/8715))
- Enh, minor, builtins: use urllib (and defer) instead of requests if reading a remote script path ([#8785](https://github.com/napari/napari/pull/8785))
- Perf: Defer importing scipy.spatial ([#8789](https://github.com/napari/napari/pull/8789))
- Revert the switch from Welcome widget to Welcome overlay from #8117 ([#8793](https://github.com/napari/napari/pull/8793))
- Improve dask check to support more dask-backed array types ([#8896](https://github.com/napari/napari/pull/8896))
- Use pep562 to defer AVAILABLE_LABELS_COLORMAPS which imports skimage.color -> scipy.linalg ([#8903](https://github.com/napari/napari/pull/8903))

## Bug Fixes

- fix: clims for non-numpy arrays with out-of-view translate ([#8756](https://github.com/napari/napari/pull/8756))
- Fix TypeError with anisotropic data in 3D ray intersections ([#8812](https://github.com/napari/napari/pull/8812))
- Reuse QMarginSlidersPopup between rightclicks ([#8819](https://github.com/napari/napari/pull/8819))
- Fix: Use Python's tokenize script decoding for builtin reader ([#8838](https://github.com/napari/napari/pull/8838))
- Fix: Blocks dims slider widget creation feedback to dims model ([#8840](https://github.com/napari/napari/pull/8840))
- Fix: play button loop mode duplication ([#8841](https://github.com/napari/napari/pull/8841))
- Improve dask check to support more dask-backed array types ([#8896](https://github.com/napari/napari/pull/8896))
- Fix floating widgets and use custom title bar in all cases ([#8898](https://github.com/napari/napari/pull/8898))
- Wrap Labels multiscale data in MultiScaleData object in setter ([#8922](https://github.com/napari/napari/pull/8922))
- Fix Labels show_selected_label being silently dropped after color shuffle ([#8947](https://github.com/napari/napari/pull/8947))
- Fix Volume visual crash when adding invisible scalar field in 3D ([#8968](https://github.com/napari/napari/pull/8968))

## Documentation

- Fix typo in 0.7.0 release notes ([docs#967](https://github.com/napari/docs/pull/967))
- Remove draft note from 0.7.0 release notes. ([docs#968](https://github.com/napari/docs/pull/968))
- Reorganize cards in homepage ([docs#970](https://github.com/napari/docs/pull/970))
- Rename "latest" version switch to "dev" ([docs#971](https://github.com/napari/docs/pull/971))
- Use stable version for dev docs bundle links ([docs#973](https://github.com/napari/docs/pull/973))
- Remove mention of unmaintained plugin in quick start ([docs#976](https://github.com/napari/docs/pull/976))
- Rename navbar entries (API and Contribute) ([docs#978](https://github.com/napari/docs/pull/978))
- Update team page ([docs#980](https://github.com/napari/docs/pull/980))
- Add "Edit on Github" to secondary sidebar ([docs#982](https://github.com/napari/docs/pull/982))
- Add deprecation warning section in contributing guide ([docs#984](https://github.com/napari/docs/pull/984))
- Enable search as you type and remove sidebar search ([docs#989](https://github.com/napari/docs/pull/989))
- Use flexible search field for navbar ([docs#991](https://github.com/napari/docs/pull/991))
- Add more info about example tags and _.py ([docs#994](https://github.com/napari/docs/pull/994))
- Remove napari-hub from navbar and add to sidebar ([docs#995](https://github.com/napari/docs/pull/995))
- Update deprecation warning guidance to use `FutureWarning` ([docs#997](https://github.com/napari/docs/pull/997))
- Update Jupyter notebook example screenshot ([docs#1003](https://github.com/napari/docs/pull/1003))
- Update multiscale documentation to describe new level selection ([docs#1004](https://github.com/napari/docs/pull/1004))
- Add release notes for 0.7.1a1 ([docs#1009](https://github.com/napari/docs/pull/1009))
- Minimal all-contributors setup ([docs#1011](https://github.com/napari/docs/pull/1011))
- Add Carlos to Core Team page ([docs#1012](https://github.com/napari/docs/pull/1012))
- Update release notes for 0.7.1 ([docs#1019](https://github.com/napari/docs/pull/1019))
- Example: Enhance theme sample widget with theme colors, widgets ([#8662](https://github.com/napari/napari/pull/8662))
- Add note to Camera.angles docstring about quaternion normalisation ([#8864](https://github.com/napari/napari/pull/8864))
- Docs: Bump lower version of napari-sphinx-theme ([#8886](https://github.com/napari/napari/pull/8886))
- Replace v (shorter) with viewer in the examples ([#8940](https://github.com/napari/napari/pull/8940))
- Add Carlos Rodríguez-Reza to core team section of citation file ([#8971](https://github.com/napari/napari/pull/8971))

## Other Pull Requests

- ci(dependabot): bump the github-actions group with 3 updates ([docs#975](https://github.com/napari/docs/pull/975))
- Fix minor typos ([docs#1005](https://github.com/napari/docs/pull/1005))
- ci(dependabot): bump the github-actions group with 3 updates ([docs#1006](https://github.com/napari/docs/pull/1006))
- Remove "auto author assign" workflow ([docs#1008](https://github.com/napari/docs/pull/1008))
- Update workflows to python 3.14 ([#8666](https://github.com/napari/napari/pull/8666))
- Improve typing in qt_dims_slider and clean local functions ([#8683](https://github.com/napari/napari/pull/8683))
- Drop triangle from 3.14 docs dependencies ([#8703](https://github.com/napari/napari/pull/8703))
- Use viewer-based caching for font manager ([#8761](https://github.com/napari/napari/pull/8761))
- Enable `TC003` - typing-only-standard-library-import rule in ruff config ([#8791](https://github.com/napari/napari/pull/8791))
- Solve "Could not resolve type hint for required parameter 'qt_viewer'." ([#8792](https://github.com/napari/napari/pull/8792))
- Add app-model to mypy task dependencies and fix errors ([#8794](https://github.com/napari/napari/pull/8794))
- Update `coverage`, `dask`, `fsspec`, `hypothesis`, `ipython`, `numpy`, `pint`, `pygments`, `pyside6`, `qtconsole`, `superqt` ([#8796](https://github.com/napari/napari/pull/8796))
- Move from `appdirs` to `platformdirs` ([#8797](https://github.com/napari/napari/pull/8797))
- [pre-commit.ci] pre-commit autoupdate ([#8800](https://github.com/napari/napari/pull/8800))
- Enable TC002 ruff rule ([#8804](https://github.com/napari/napari/pull/8804))
- Fix layerlist_context by move Calable from TYPE_CHECKING block ([#8805](https://github.com/napari/napari/pull/8805))
- Add zizmor security CI check ([#8811](https://github.com/napari/napari/pull/8811))
- Ban expensive import in ruff ([#8815](https://github.com/napari/napari/pull/8815))
- Remove `triangle` from `napari[all]` ([#8824](https://github.com/napari/napari/pull/8824))
- Add a Linux aarch64 test run (py313, pyqt6) to --pre, PR, and comprehensive tests  ([#8825](https://github.com/napari/napari/pull/8825))
- [maint] Use ubuntu-slim 1 vCPU runners for simple jobs ([#8826](https://github.com/napari/napari/pull/8826))
- [maint] Add `bermuda` to testing dependencies ([#8827](https://github.com/napari/napari/pull/8827))
- [pre-commit.ci] pre-commit autoupdate ([#8831](https://github.com/napari/napari/pull/8831))
- Add more debug information on fail to import Qt ([#8834](https://github.com/napari/napari/pull/8834))
- maint: replace `StringEnum` base class with with `StrEnum` ([#8835](https://github.com/napari/napari/pull/8835))
- Do not import builtins from core (and forbid doing so) ([#8842](https://github.com/napari/napari/pull/8842))
- ci(dependabot): bump the actions group with 8 updates ([#8844](https://github.com/napari/napari/pull/8844))
- Remove sentinel leftover from `napari.utils.misc` ([#8846](https://github.com/napari/napari/pull/8846))
- Fix checking autogenerated type stubs ([#8847](https://github.com/napari/napari/pull/8847))
- Deprecate str_to_rgb which is unused ([#8849](https://github.com/napari/napari/pull/8849))
- Revert Citation validator from ubuntu-slim to use ubuntu-latest ([#8851](https://github.com/napari/napari/pull/8851))
- Deprecate make_default_color_array ([#8852](https://github.com/napari/napari/pull/8852))
- Dependabot cooldown ([#8853](https://github.com/napari/napari/pull/8853))
- Test against conda packages using pixi ([#8855](https://github.com/napari/napari/pull/8855))
- Use bash script instead of docker image for checking PR labels ([#8856](https://github.com/napari/napari/pull/8856))
- Check untyped defs in labels ([#8861](https://github.com/napari/napari/pull/8861))
- add jasper-tms to citation ([#8862](https://github.com/napari/napari/pull/8862))
- Rename tox test step names to include 'qt_backend' ([#8866](https://github.com/napari/napari/pull/8866))
- Update `hypothesis`, `npe2`, `pandas`, `pillow`, `pydantic-extra-types`, `pyqt6` ([#8868](https://github.com/napari/napari/pull/8868))
- [pre-commit.ci] pre-commit autoupdate ([#8869](https://github.com/napari/napari/pull/8869))
- Deprecate color_dict_to_colormap with FutureWarning ([#8871](https://github.com/napari/napari/pull/8871))
- Update `hypothesis`, `lxml`, `magicgui`, `platformdirs`, `pytest`, `rich`, `virtualenv` ([#8876](https://github.com/napari/napari/pull/8876))
- Add session type to --info ([#8880](https://github.com/napari/napari/pull/8880))
- Improve make_release workflow's release steps ([#8882](https://github.com/napari/napari/pull/8882))
- [pre-commit.ci] pre-commit autoupdate ([#8884](https://github.com/napari/napari/pull/8884))
- ci(dependabot): bump the actions group with 4 updates ([#8889](https://github.com/napari/napari/pull/8889))
- Restore ability to push changes to napari-bot/napari repo ([#8891](https://github.com/napari/napari/pull/8891))
- Checkout only citation.cff in milestone checker ([#8892](https://github.com/napari/napari/pull/8892))
- Use hynek for build wheel ([#8893](https://github.com/napari/napari/pull/8893))
- Deprecate image_reader_to_layerdata_reader ([#8895](https://github.com/napari/napari/pull/8895))
- Finish typing bounding box and brush circle overlays ([#8902](https://github.com/napari/napari/pull/8902))
- Update `hypothesis`, `lxml`, `pydantic`, `pydantic-extra-types`, `virtualenv`, `xarray` ([#8906](https://github.com/napari/napari/pull/8906))
- [pre-commit.ci] pre-commit autoupdate ([#8908](https://github.com/napari/napari/pull/8908))
- Update `certifi`, `hypothesis`, `ipython`, `matplotlib`, `pydantic`, `pydantic-settings` ([#8920](https://github.com/napari/napari/pull/8920))
- [pre-commit.ci] pre-commit autoupdate ([#8923](https://github.com/napari/napari/pull/8923))
- Scalar base data setter ([#8925](https://github.com/napari/napari/pull/8925))
- Instead of checking if milestone is added, add the milestone on merge ([#8926](https://github.com/napari/napari/pull/8926))
- Adapt tests that use zarr to work on zarr < 3 and zarr > 3.2.0 ([#8943](https://github.com/napari/napari/pull/8943))
- Don't use random floats for image layer data in screenshot tests ([#8945](https://github.com/napari/napari/pull/8945))
- Update `coverage`, `fsspec`, `hypothesis`, `pydantic`, `pydantic-settings`, `tensorstore`, `tifffile`, `virtualenv` ([#8949](https://github.com/napari/napari/pull/8949))
- [pre-commit.ci] pre-commit autoupdate ([#8951](https://github.com/napari/napari/pull/8951))
- Fix auto milestone workflow ([#8954](https://github.com/napari/napari/pull/8954))
- Explicitly pass the repository name in command setting milestone ([#8955](https://github.com/napari/napari/pull/8955))
- Update python version used to generate title and body of update constraints PR ([#8957](https://github.com/napari/napari/pull/8957))
- Use `gh release create` instead of `softprops/action-gh-release` ([#8958](https://github.com/napari/napari/pull/8958))
- Remove CODEOWNERS ([#8959](https://github.com/napari/napari/pull/8959))
- Restore testing on windows-latest (Revert  5d6ab46) ([#8960](https://github.com/napari/napari/pull/8960))
- ci(dependabot): bump the actions group across 1 directory with 8 updates ([#8963](https://github.com/napari/napari/pull/8963))
- Pass token to make `gh` working in create release workflow ([#8964](https://github.com/napari/napari/pull/8964))
- Next fix of release workflow by pass directly `dist/*` ([#8966](https://github.com/napari/napari/pull/8966))
- Try to fix passing prerelease to `gh release create` ([#8969](https://github.com/napari/napari/pull/8969))
- Explicitly set repository in make release workflow ([#8970](https://github.com/napari/napari/pull/8970))
- Update `hypothesis`, `pandas`, `pyside6`, `pytest-rerunfailures`, `virtualenv` ([#8981](https://github.com/napari/napari/pull/8981))


## 18 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Aniket](https://github.com/napari/napari/commits?author=Aniketsy) ([docs](https://github.com/napari/docs/commits?author=Aniketsy))  - @Aniketsy +
- [Carol Willing](https://github.com/napari/napari/commits?author=willingc) - @willingc
- [Caroline Malin-Mayor](https://github.com/napari/napari/commits?author=cmalinmayor) ([docs](https://github.com/napari/docs/commits?author=cmalinmayor))  - @cmalinmayor +
- [Constantin Aronssohn](https://github.com/napari/docs/commits?author=cnstt) - @cnstt
- [David Stansby](https://github.com/napari/napari/commits?author=dstansby) - @dstansby
- [Draga Doncila Pop](https://github.com/napari/docs/commits?author=DragaDoncila) - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Jacopo Abramo](https://github.com/napari/napari/commits?author=jacopoabramo) - @jacopoabramo
- [Kabilar Gunalan](https://github.com/napari/docs/commits?author=kabilar) - @kabilar
- [LiudengZhang](https://github.com/napari/napari/commits?author=LiudengZhang) - @LiudengZhang
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Lucien Hinderling](https://github.com/napari/napari/commits?author=hinderling) - @hinderling +
- [Margot Chazotte](https://github.com/napari/napari/commits?author=MargotCh) - @MargotCh
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Newstein](https://github.com/napari/napari/commits?author=pnewstein) - @pnewstein +
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko
- [Wulin Teo](https://github.com/napari/napari/commits?author=wulinteousa2-hash) - @wulinteousa2-hash +

## 20 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Aniket](https://github.com/napari/napari/commits?author=Aniketsy) ([docs](https://github.com/napari/docs/commits?author=Aniketsy))  - @Aniketsy +
- [Anniek Stokkermans](https://github.com/napari/docs/commits?author=AnniekStok) - @AnniekStok
- [Carlos Mario Rodriguez Reza](https://github.com/napari/docs/commits?author=carlosmariorr) - @carlosmariorr
- [Carol Willing](https://github.com/napari/napari/commits?author=willingc) - @willingc
- [Caroline Malin-Mayor](https://github.com/napari/napari/commits?author=cmalinmayor) ([docs](https://github.com/napari/docs/commits?author=cmalinmayor))  - @cmalinmayor +
- [Constantin Aronssohn](https://github.com/napari/docs/commits?author=cnstt) - @cnstt
- [David Stansby](https://github.com/napari/napari/commits?author=dstansby) - @dstansby
- [Davin Potts](https://github.com/napari/docs/commits?author=applio) - @applio
- [Draga Doncila Pop](https://github.com/napari/docs/commits?author=DragaDoncila) - @DragaDoncila
- [github-advanced-security[bot]](https://github.com/napari/docs/commits?author=github-advanced-security[bot]) - @github-advanced-security[bot]
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Jacopo Abramo](https://github.com/napari/napari/commits?author=jacopoabramo) - @jacopoabramo
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Lucien Hinderling](https://github.com/napari/napari/commits?author=hinderling) - @hinderling +
- [Margot Chazotte](https://github.com/napari/napari/commits?author=MargotCh) - @MargotCh
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko
- [Wulin Teo](https://github.com/napari/napari/commits?author=wulinteousa2-hash) - @wulinteousa2-hash +
