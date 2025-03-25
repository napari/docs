# napari 0.6.0
⚠️ *Note: these release notes are still in draft while 0.6.0 is in release candidate testing.* ⚠️

Friday, Mar 14, 2025 (0.6.0a1)


🚧 *These notes are under construction while in pre-release* 🚧

We’re happy to announce the release of napari 0.6.0! The right-handed release! This release features major changes so read on to see how they might affect you!

napari is a fast, interactive, multi-dimensional image viewer for Python. It’s designed for exploring, annotating, and analyzing multi-dimensional images. It’s built on Qt (for the GUI), VisPy (for performant GPU-based rendering), and the scientific Python stack (NumPy, SciPy, and friends).

For more information, examples, and documentation, please visit our website: https://napari.org/

## Highlights


### Updated viewer handedness ✋

So. Funny story. 😅

For (checks notes) 5 years or so, napari has had a 3D view, and for those 5
years, for almost all datasets, that view has been a *mirror image* of the 3D
object they were trying to represent. Any biologists among you might have
noticed that loading 3D molecular coordinates of DNA would result in a
left-handed helix, while anatomists among you might have been surprised by how
many of your samples suffered from [situs inversus
totalis](https://en.wikipedia.org/wiki/Situs_inversus)!

By and large, many things that people care about work exactly the same in the
mirror world — volume measurements, forces, tracking, speed, ... — so this bug
has gone mostly unnoticed, or noticed and shrugged off and unfixed for all this
time. But it's important for some things!  Your heart is on the left side of
your body, but the right side of your mirror image's. This can be critical, for
example, when using software to plan surgery! Thankfully, we are not aware of
any cases of napari being used in this way. 😅

napari uses zyx coordinates instead of xyz because it is the most natural way
to work with NumPy arrays and the rest of the scientific Python imaging
ecosystem. Flipping the axes in this way also changes the *handedness* of the
space, *unless* you also flip the direction of one of the dimensions. The
simplest way to illustrate this is [this 3D model of a right
shoe](https://grabcad.com/library/anatomic-shoe-sole-euro-right-41-1), which looks
like this in previous versions of napari:

![right shoe rendered as a left shoe in napari](https://github.com/user-attachments/assets/c9190e2c-f35a-44d1-95d5-f9877dd4c843)

and in 0.5.6+, thanks to [#7488](https://github.com/napari/napari/pull/7488):

![right shoe correctly rendered as a right shoe in napari](https://github.com/user-attachments/assets/e187f5e7-8e4a-4526-bae9-80a9bec6fea3)

Most users won't notice. But if you were among the users that noticed and you
implemented workarounds in your code (such as setting the z-scale to a negative
number), now is a good time to undo the workarounds for newer versions of
napari! If you run into any issues please get in touch [on GitHub
issues](https://github.com/napari/napari) or on our [Zulip chat room](https://napari.zulipchat.com)!

- Implement command palette widget ([#5483](https://github.com/napari/napari/pull/5483))
- Fix issues displaying polygons with holes in Shapes ([#6654](https://github.com/napari/napari/pull/6654))
- Flip z axis on 3D camera to default to right-handed frame (#7488 redux) ([#7554](https://github.com/napari/napari/pull/7554))
- Add right-click indicator to 3D, Roll, Grid, and Square push buttons ([#7556](https://github.com/napari/napari/pull/7556))
- Implement polygon with holes in compiled triangulation ([#7566](https://github.com/napari/napari/pull/7566))
- Remove pydantic v1 compatibility layer, depend on pydantic>=2.2 ([#7589](https://github.com/napari/napari/pull/7589))
- Add Grid Mode Spacing to change distance between layers  ([#7597](https://github.com/napari/napari/pull/7597))
- Enable creation of custom linear colormaps in layer controls ([#7600](https://github.com/napari/napari/pull/7600))
- Update configuration to drop python 3.9 and add python 3.13 ([#7603](https://github.com/napari/napari/pull/7603))
- Change ndisplay button to toggle-like to increase discoverability ([#7608](https://github.com/napari/napari/pull/7608))
- Expose additional Camera parameters in GUI with 3D popup widget ([#7626](https://github.com/napari/napari/pull/7626))
- Turn on npe2 adaptor by default and add warning ([#7627](https://github.com/napari/napari/pull/7627))
- Add API to Camera model to flip axes ([#7663](https://github.com/napari/napari/pull/7663))
- Show layer status for all visible layers ([#7673](https://github.com/napari/napari/pull/7673))

## New Features

- Implement command palette widget ([#5483](https://github.com/napari/napari/pull/5483))
- Add a custom log handler and GUI viewer with filters ([#6900](https://github.com/napari/napari/pull/6900))
- Add Grid Mode Spacing to change distance between layers  ([#7597](https://github.com/napari/napari/pull/7597))
- Enable creation of custom linear colormaps in layer controls ([#7600](https://github.com/napari/napari/pull/7600))
- Add API to Camera model to flip axes ([#7663](https://github.com/napari/napari/pull/7663))
- Show layer status for all visible layers ([#7673](https://github.com/napari/napari/pull/7673))
- Expose new camera orientation API in GUI in ndisplay popup widget ([#7686](https://github.com/napari/napari/pull/7686))

## Improvements

- Add a custom log handler and GUI viewer with filters ([#6900](https://github.com/napari/napari/pull/6900))
- Add numba warmup step when creating empty Shapes Layer ([#7541](https://github.com/napari/napari/pull/7541))
- Add Image Border / Bounding Box Gallery Examples for both 2D and 3D ([#7546](https://github.com/napari/napari/pull/7546))
- Add right-click indicator to 3D, Roll, Grid, and Square push buttons ([#7556](https://github.com/napari/napari/pull/7556))
- Change naming of 'pan/zoom' mode to 'Move camera' to clarify functionality differences in 2D and 3D ([#7569](https://github.com/napari/napari/pull/7569))
- ENH: adjust layer coordinates in status by _translate_grid ([#7584](https://github.com/napari/napari/pull/7584))
- Add right click indicator to playback icons ([#7590](https://github.com/napari/napari/pull/7590))
- Change ndisplay button to toggle-like to increase discoverability ([#7608](https://github.com/napari/napari/pull/7608))
- [UI] Add Command Palette to the welcome screen ([#7613](https://github.com/napari/napari/pull/7613))
- Fix layout issue in image/surface controls ([#7618](https://github.com/napari/napari/pull/7618))
- Expose additional Camera parameters in GUI with 3D popup widget ([#7626](https://github.com/napari/napari/pull/7626))
- Add 'Extend with Plugins' and 'Contribute to napari' links to the Help menu. ([#7645](https://github.com/napari/napari/pull/7645))
- Restyle visibility icon to clarify different interactions compared to clicking layer ([#7657](https://github.com/napari/napari/pull/7657))

## Performance

- Add numba warmup step when creating empty Shapes Layer ([#7541](https://github.com/napari/napari/pull/7541))

## Bug Fixes

- Fix issues displaying polygons with holes in Shapes ([#6654](https://github.com/napari/napari/pull/6654))
- Fix points data selection for 4D ([#6819](https://github.com/napari/napari/pull/6819))
- Update point add to handle multiple coordinates in data_indices ([#7536](https://github.com/napari/napari/pull/7536))
- Use data.dtype for creating slicer ([#7540](https://github.com/napari/napari/pull/7540))
- Fix bounding_box extent for case of 3D multiscale layer ([#7545](https://github.com/napari/napari/pull/7545))
- Flip z axis on 3D camera to default to right-handed frame (#7488 redux) ([#7554](https://github.com/napari/napari/pull/7554))
- Protect few possible access to window that may be triggered by callback ([#7565](https://github.com/napari/napari/pull/7565))
- Implement polygon with holes in compiled triangulation ([#7566](https://github.com/napari/napari/pull/7566))
- Fix / update path (shape layer) icon ([#7582](https://github.com/napari/napari/pull/7582))
- Fix double-click-to-zoom for case of only 2D layer in 3D display ([#7586](https://github.com/napari/napari/pull/7586))
- Set dtype for out of bounds slice when slicing image ([#7606](https://github.com/napari/napari/pull/7606))
- Refactor setting face meshes in Shapes to support other planar axes ([#7622](https://github.com/napari/napari/pull/7622))
- Fix add_shapes.py example: remove duplicate vertex that can cause seg faults ([#7636](https://github.com/napari/napari/pull/7636))
- Move focus to main window before close `NapariQtNotification` ([#7656](https://github.com/napari/napari/pull/7656))
- Update layerlist.py docstring to stop doc build warnings ([#7660](https://github.com/napari/napari/pull/7660))
- Use faster edge triangulation if numba is available ([#7674](https://github.com/napari/napari/pull/7674))
- enforce not restart status checker thread on window close ([#7682](https://github.com/napari/napari/pull/7682))
- Fix `is_convex` to properly handle shapes with self intersection ([#7688](https://github.com/napari/napari/pull/7688))

## Documentation

- Add example linking the cameras of two viewers ([#6881](https://github.com/napari/napari/pull/6881))
- Add example to LayerList and docstrings for link_layers/unlink_layers ([#7410](https://github.com/napari/napari/pull/7410))
- Add example for using the glasbey colormap with napari ([#7468](https://github.com/napari/napari/pull/7468))
- Ensure that fps overlay is visible on gallery screenshot in overlay example ([#7558](https://github.com/napari/napari/pull/7558))
- Update NotebookScreenshot docstring ([#7583](https://github.com/napari/napari/pull/7583))
- Cleanup multiple viewer example ([#7593](https://github.com/napari/napari/pull/7593))
- Update README.md to use python 3.10 like napari.org install docs ([#7599](https://github.com/napari/napari/pull/7599))
- Add link to napari weather report dashboard in README.md ([#7609](https://github.com/napari/napari/pull/7609))
- Update README.md to bump the recommended python to 3.11 ([#7610](https://github.com/napari/napari/pull/7610))
- Update layerlist.py docstring to stop doc build warnings ([#7660](https://github.com/napari/napari/pull/7660))
- Skip `multiple_viewers` example from docs Examples gallery ([#7676](https://github.com/napari/napari/pull/7676))
- Update finding and installing plugin docs ([docs#541](https://github.com/napari/docs/pull/541))
- Rename Gallery to Examples ([docs#560](https://github.com/napari/docs/pull/560))
- Update BlueSky link to our actual account (not masto bridge) ([docs#564](https://github.com/napari/docs/pull/564))
- Update installation instructions to mention the `optional` dependency group ([docs#571](https://github.com/napari/docs/pull/571))
- Update conf.py to bump the recommended python version to 3.11 ([docs#572](https://github.com/napari/docs/pull/572))
- Update viewer.md to include spacing for grid mode ([docs#573](https://github.com/napari/docs/pull/573))
- Update shapes path icon ([docs#574](https://github.com/napari/docs/pull/574))
- Update viewer.md to include tip about the chevron for right-click ([docs#576](https://github.com/napari/docs/pull/576))
- Add an explicit list of Steering Council members to Team page ([docs#579](https://github.com/napari/docs/pull/579))
- Edit plugin landing page to add links and update information ([docs#581](https://github.com/napari/docs/pull/581))
- Edit user plugin installation page to simplify instructions ([docs#586](https://github.com/napari/docs/pull/586))
- Untab the plugin users and plugin developers grids ([docs#593](https://github.com/napari/docs/pull/593))
- Add guidance document for adapted npe1 plugins ([docs#597](https://github.com/napari/docs/pull/597))
- Re-add empty cli image for installation tutorial ([docs#598](https://github.com/napari/docs/pull/598))
- Updates to the makefile, contribution guide, and README for the napari[docs] installation ([docs#602](https://github.com/napari/docs/pull/602))
- Add cards to the Advanced Topics landing page for plugins ([docs#603](https://github.com/napari/docs/pull/603))
- Reorganize plugin landing page and remove redundant index file ([docs#609](https://github.com/napari/docs/pull/609))
- Add release notes and community chat links to homepage sidebar ([docs#610](https://github.com/napari/docs/pull/610))
- Suppress detached head warning in prep_docs script ([docs#612](https://github.com/napari/docs/pull/612))
- Move user-facing information to top of preferences and fix autogenerated UI images ([docs#613](https://github.com/napari/docs/pull/613))
- Add sections to Contributing landing page and edit lightly ([docs#614](https://github.com/napari/docs/pull/614))
- Move links out of navbar and into sidebar / other docs. ([docs#620](https://github.com/napari/docs/pull/620))
- Add 0.6.0 alpha release note ([docs#622](https://github.com/napari/docs/pull/622))
- Add info about adapted plugins to troubleshooting guide ([docs#623](https://github.com/napari/docs/pull/623))

## Other Pull Requests

- Layer controls widgets refactor ([#7355](https://github.com/napari/napari/pull/7355))
- Add optional dependency sections for gallery and docs ([#7487](https://github.com/napari/napari/pull/7487))
- Small improvement of code readability for Shape painting ([#7544](https://github.com/napari/napari/pull/7544))
- Remove some py38 leftovers ([#7549](https://github.com/napari/napari/pull/7549))
- Update `hypothesis`, `pydantic`, `scikit-image` ([#7557](https://github.com/napari/napari/pull/7557))
- Fix rendering of Fourier example screenshot  ([#7560](https://github.com/napari/napari/pull/7560))
- [pre-commit.ci] pre-commit autoupdate ([#7561](https://github.com/napari/napari/pull/7561))
- Update scale bar tests to actually test white/magenta ([#7563](https://github.com/napari/napari/pull/7563))
- ci(dependabot): update cff-validator and codecov upload ([#7572](https://github.com/napari/napari/pull/7572))
- Update `babel`, `certifi`, `coverage`, `fsspec`, `hypothesis`, `ipython`, `lxml`, `psygnal`, `pyqt6`, `qtpy`, `virtualenv`, `xarray` ([#7575](https://github.com/napari/napari/pull/7575))
- [pre-commit.ci] pre-commit autoupdate ([#7578](https://github.com/napari/napari/pull/7578))
- Update grid / layer button icons (and separate from stop playback icon) ([#7580](https://github.com/napari/napari/pull/7580))
- [pre-commit.ci] pre-commit autoupdate ([#7592](https://github.com/napari/napari/pull/7592))
- Remove andy-sweet from CODEOWNERS ([#7594](https://github.com/napari/napari/pull/7594))
- Block problematic pydantic pre-release ([#7596](https://github.com/napari/napari/pull/7596))
- stop using ubuntu 20.04 runners in actions ([#7598](https://github.com/napari/napari/pull/7598))
- Update `dask`, `hypothesis`, `psutil` ([#7605](https://github.com/napari/napari/pull/7605))
- Update `scipy` ([#7616](https://github.com/napari/napari/pull/7616))
- Fix test_export_rois to work on HiDPI screens ([#7625](https://github.com/napari/napari/pull/7625))
- Add tox to dev dependencies ([#7629](https://github.com/napari/napari/pull/7629))
- Add benchmarks for triangulation ([#7632](https://github.com/napari/napari/pull/7632))
- Update `hypothesis`, `npe2`, `scikit-image`, `tensorstore`, `tifffile` ([#7635](https://github.com/napari/napari/pull/7635))
- Update pyproject.toml to add missing docs reqs to [docs] ([#7637](https://github.com/napari/napari/pull/7637))
- Update CIrcleCI config.yml to use docs dependency group and pyqt5 (match napari/docs) ([#7638](https://github.com/napari/napari/pull/7638))
- Update build_docs.yml to match napari/docs ([#7640](https://github.com/napari/napari/pull/7640))
- Update `hypothesis` ([#7641](https://github.com/napari/napari/pull/7641))
- Simplify constraints configuration ([#7642](https://github.com/napari/napari/pull/7642))
- [pre-commit.ci] pre-commit autoupdate ([#7647](https://github.com/napari/napari/pull/7647))
- Conditionally call IPython 9+ with a theme_name instead of color_scheme ([#7650](https://github.com/napari/napari/pull/7650))
- Add version info to welcome screen ([#7659](https://github.com/napari/napari/pull/7659))
- Update `hypothesis`, `ipython`, `matplotlib`, `pytest` ([#7664](https://github.com/napari/napari/pull/7664))
- [pre-commit.ci] pre-commit autoupdate ([#7666](https://github.com/napari/napari/pull/7666))
- Cleanup warnings in shapes benchmark, use `_` prefix for unused variables ([#7667](https://github.com/napari/napari/pull/7667))
- Skip 3D sporadically-failing 3D screenshot test in all macOS CI ([#7672](https://github.com/napari/napari/pull/7672))
- Show viewer before trigger screenshot in the camera tests ([#7678](https://github.com/napari/napari/pull/7678))
- Update `fsspec`, `hypothesis`, `ipython`, `virtualenv` ([#7684](https://github.com/napari/napari/pull/7684))
- Block ipykernel==7.0.0a1 ([#7685](https://github.com/napari/napari/pull/7685))
- [pre-commit.ci] pre-commit autoupdate ([#7687](https://github.com/napari/napari/pull/7687))
- Show version for PyQt6 and PySide6 ([#7691](https://github.com/napari/napari/pull/7691))
- Add CI status badge and remove Cirrus CI badge from README ([#7693](https://github.com/napari/napari/pull/7693))
- Bump python versions in CircleCI to match docs repo ([#7694](https://github.com/napari/napari/pull/7694))
- Skip vispy bounding box test on windows ([#7697](https://github.com/napari/napari/pull/7697))
- Add codespell support (config, workflow to detect/not fix) and make it fix few typos ([docs#587](https://github.com/napari/docs/pull/587))
- Update CircleCI config.yml to use napari docs and gallery dependency groups ([docs#590](https://github.com/napari/docs/pull/590))
- Update build_and_deploy.yml to use napari docs dependency group ([docs#591](https://github.com/napari/docs/pull/591))
- Replace two manual screenshots of the viewer (launch_cli_empty and launch_cli_image) with nbscreenshots ([docs#606](https://github.com/napari/docs/pull/606))
- Update conf.py to address pygment -> pygments deprecation ([docs#607](https://github.com/napari/docs/pull/607))
- Update CircleCI config to python orb and image ([docs#611](https://github.com/napari/docs/pull/611))


## 14 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Andrew Sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Carol Willing](https://github.com/napari/napari/commits?author=willingc) ([docs](https://github.com/napari/docs/commits?author=willingc))  - @willingc
- [Daniel Althviz Moré](https://github.com/napari/napari/commits?author=dalthviz) - @dalthviz
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) ([docs](https://github.com/napari/docs/commits?author=DragaDoncila))  - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Hanjin Liu](https://github.com/napari/napari/commits?author=hanjinliu) - @hanjinliu +
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) ([docs](https://github.com/napari/docs/commits?author=jni))  - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Melissa Weber Mendonça](https://github.com/napari/napari/commits?author=melissawm) ([docs](https://github.com/napari/docs/commits?author=melissawm))  - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) ([docs](https://github.com/napari/docs/commits?author=psobolewskiPhD))  - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko
- [Yaroslav Halchenko](https://github.com/napari/docs/commits?author=yarikoptic) - @yarikoptic +


## 15 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Andrew Sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Carol Willing](https://github.com/napari/napari/commits?author=willingc) ([docs](https://github.com/napari/docs/commits?author=willingc))  - @willingc
- [Daniel Althviz Moré](https://github.com/napari/napari/commits?author=dalthviz) - @dalthviz
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) ([docs](https://github.com/napari/docs/commits?author=DragaDoncila))  - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Hanjin Liu](https://github.com/napari/napari/commits?author=hanjinliu) - @hanjinliu +
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) ([docs](https://github.com/napari/docs/commits?author=jni))  - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Lucy Liu](https://github.com/napari/docs/commits?author=lucyleeow) - @lucyleeow
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [Melissa Weber Mendonça](https://github.com/napari/napari/commits?author=melissawm) ([docs](https://github.com/napari/docs/commits?author=melissawm))  - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) ([docs](https://github.com/napari/docs/commits?author=psobolewskiPhD))  - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko
- [Wouter-Michiel Vierdag](https://github.com/napari/docs/commits?author=melonora) - @melonora
- [Yaroslav Halchenko](https://github.com/napari/docs/commits?author=yarikoptic) - @yarikoptic +

