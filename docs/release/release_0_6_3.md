# napari 0.6.3
⚠️ *Note: these release notes are still in draft while 0.6.3 is in release candidate testing.* ⚠️

*Tue, Jul 22, 2025*

We’re happy to announce the release of napari 0.6.3!

napari is a fast, interactive, multi-dimensional image viewer for Python. It’s designed for exploring, annotating, and analyzing multi-dimensional images. It’s built on Qt (for the GUI), VisPy (for performant GPU-based rendering), and the scientific Python stack (NumPy, SciPy, and friends).

For more information, examples, and documentation, please visit our website: https://napari.org/

## Highlights


- Qt controls for thick slicing ([#6146](https://github.com/napari/napari/pull/6146))
- Enable testing on recent PySide6  ([#7887](https://github.com/napari/napari/pull/7887))
- Add 'zoom-box' to the viewer ([#8004](https://github.com/napari/napari/pull/8004))
- Prevent Windows Access Violation with GPU resource cleanup on layer removal ([#8122](https://github.com/napari/napari/pull/8122))

## New Features

- Qt controls for thick slicing ([#6146](https://github.com/napari/napari/pull/6146))
- Add automatic area and perimeter measurement for shapes + action ([#7262](https://github.com/napari/napari/pull/7262))
- Tiling canvas overlays ([#7836](https://github.com/napari/napari/pull/7836))
- Use information about units when calculate scale of layers when render ([#7889](https://github.com/napari/napari/pull/7889))
- Add 'zoom-box' to the viewer ([#8004](https://github.com/napari/napari/pull/8004))
- Add hot-reload for the devs ([#8007](https://github.com/napari/napari/pull/8007))

## Improvements

- Allow use functions from PartSegCore-compiled-backend as numba alternative for data to texture mapping  ([#6617](https://github.com/napari/napari/pull/6617))
- Enable testing on recent PySide6  ([#7887](https://github.com/napari/napari/pull/7887))
- Implement pasting spatial information into higher dimensions ([#7973](https://github.com/napari/napari/pull/7973))
- Improve performance and memory usage of editing Shapes layer  ([#8006](https://github.com/napari/napari/pull/8006))
- [Update] Added `remove` and `remove_selected` in Shapes and Points ([#8031](https://github.com/napari/napari/pull/8031))
- Colorblind friendly image sample of kidney and lily ([#8090](https://github.com/napari/napari/pull/8090))
- Add Features using Features Table widget ([#8093](https://github.com/napari/napari/pull/8093))
- Added fixed seed and tested the value. ([#8097](https://github.com/napari/napari/pull/8097))
- Add keybinding (CtrlCmd-up/down) to select layer above/below ([#8119](https://github.com/napari/napari/pull/8119))

## Performance

- Allow use functions from PartSegCore-compiled-backend as numba alternative for data to texture mapping  ([#6617](https://github.com/napari/napari/pull/6617))

## Bug Fixes

- ensure sync when taking a screenshot ([#8064](https://github.com/napari/napari/pull/8064))
- Set the dimensions of the label equal to the maximum value of the layers world ([#8098](https://github.com/napari/napari/pull/8098))
- Updated code to use current symbol and border width for new points. ([#8102](https://github.com/napari/napari/pull/8102))
- Improve performance and memory usage of editing Shapes layer (#8006 again) ([#8109](https://github.com/napari/napari/pull/8109))
- Prevent Windows Access Violation with GPU resource cleanup on layer removal ([#8122](https://github.com/napari/napari/pull/8122))

## Documentation

- Update docs constraints and pyprojecttoml for npe2 ([#8075](https://github.com/napari/napari/pull/8075))
- Typo ismhow -> imshow ([#8084](https://github.com/napari/napari/pull/8084))
- Replace deprecated `view_*()` method from examples ([#8091](https://github.com/napari/napari/pull/8091))
- Comment the HEX codes of each color theme and where they're used ([#8099](https://github.com/napari/napari/pull/8099))
- New example for affine transformations in 3D using meshio and stl ([#8103](https://github.com/napari/napari/pull/8103))
- Added a try it out now section to README.md for using uv. ([#8107](https://github.com/napari/napari/pull/8107))
- Update README wording about scikit-image example ([#8125](https://github.com/napari/napari/pull/8125))
- Autogenerate images of parts of the viewer ([docs#621](https://github.com/napari/docs/pull/621))
- Update instruction how to update contraints files ([docs#672](https://github.com/napari/docs/pull/672))
- Updates to NAP-9: Multiple Views ([docs#730](https://github.com/napari/docs/pull/730))
- Update guides.md to add menu contribution guide ([docs#747](https://github.com/napari/docs/pull/747))
- Update building your first plugin guide ([docs#753](https://github.com/napari/docs/pull/753))
- Update version switcher for 0.6.2 ([docs#754](https://github.com/napari/docs/pull/754))
- Update Release Guide ([docs#755](https://github.com/napari/docs/pull/755))
- Fix information about `site-packages` directory ([docs#756](https://github.com/napari/docs/pull/756))
- Add empty release notes for 0.6.3 ([docs#757](https://github.com/napari/docs/pull/757))
- Add roadmap to sidebar links ([docs#760](https://github.com/napari/docs/pull/760))
- Refactor contributing guide landing page ([docs#761](https://github.com/napari/docs/pull/761))
- Reorganize homepage with grid columns ([docs#767](https://github.com/napari/docs/pull/767))
- Fix sidebar roadmap link ([docs#768](https://github.com/napari/docs/pull/768))
- Fix Image Annotation example ([docs#777](https://github.com/napari/docs/pull/777))
- Add website colors to community resources ([docs#779](https://github.com/napari/docs/pull/779))
- Update napari.org homepage to remove the `imshow` "button" ([docs#780](https://github.com/napari/docs/pull/780))
- Add instructions for headless docs build on Wayland ([docs#781](https://github.com/napari/docs/pull/781))
- Add module docstrings to scripts ([docs#787](https://github.com/napari/docs/pull/787))
- Update pre-commit config to add some python checkers ([docs#788](https://github.com/napari/docs/pull/788))

## Other Pull Requests

- Add codespell support (config, workflow to detect/not fix) and make it fix few typos ([#7619](https://github.com/napari/napari/pull/7619))
- Move export ROI and export figure implementations into `QtViewer` ([#7950](https://github.com/napari/napari/pull/7950))
- Clipping planes control widget ([#7993](https://github.com/napari/napari/pull/7993))
- [pre-commit.ci] pre-commit autoupdate ([#8062](https://github.com/napari/napari/pull/8062))
- Block the recent pytest-qt version on python 3.10 to keep PySide2 support in testing. ([#8067](https://github.com/napari/napari/pull/8067))
- Add configurable suffix for test artifacts ([#8069](https://github.com/napari/napari/pull/8069))
- [Update] Added `pop` for `Points` and `Shapes` ([#8072](https://github.com/napari/napari/pull/8072))
- Update `coverage`, `hypothesis`, `ipython`, `pillow`, `psygnal`, `pytest-qt`, `tensorstore`, `xarray` ([#8073](https://github.com/napari/napari/pull/8073))
- [pre-commit.ci] pre-commit autoupdate ([#8074](https://github.com/napari/napari/pull/8074))
- Move non-qt file actions from qactions module ([#8076](https://github.com/napari/napari/pull/8076))
- Move more view actions from qaction to actions ([#8077](https://github.com/napari/napari/pull/8077))
- Report benchmark on non skipped status ([#8086](https://github.com/napari/napari/pull/8086))
- Enable SIM117 ruff rule ([#8088](https://github.com/napari/napari/pull/8088))
- Remove dotenv from dev dependencies ([#8089](https://github.com/napari/napari/pull/8089))
- Add deprecation warning for view_<layer_type> functions ([#8092](https://github.com/napari/napari/pull/8092))
- Revert #8006 Improve performance and memory usage of editing Shapes layer ([#8104](https://github.com/napari/napari/pull/8104))
- Example from SciPy 2025 tutorial; image warping ([#8111](https://github.com/napari/napari/pull/8111))
- Improve stability of tests by ensuring cleaning of QtViewer instances ([#8113](https://github.com/napari/napari/pull/8113))
- Do not crash test with leaked graph if test failed ([#8123](https://github.com/napari/napari/pull/8123))
- [pre-commit.ci] pre-commit autoupdate ([#8124](https://github.com/napari/napari/pull/8124))
- Update triggered_target_build.yml regex to ensure we match on hyphen ([docs#764](https://github.com/napari/docs/pull/764))


## 12 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Andrew](https://github.com/napari/napari/commits?author=ahuang11) - @ahuang11 +
- [Carol Willing](https://github.com/napari/napari/commits?author=willingc) ([docs](https://github.com/napari/docs/commits?author=willingc))  - @willingc
- [Filippo Balzaretti](https://github.com/napari/napari/commits?author=FilBalza) ([docs](https://github.com/napari/docs/commits?author=FilBalza))  - @FilBalza +
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Ian Coccimiglio](https://github.com/napari/docs/commits?author=ian-coccimiglio) - @ian-coccimiglio +
- [Kanai Potts](https://github.com/napari/napari/commits?author=8bitbiscuit) - @8bitbiscuit +
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) ([docs](https://github.com/napari/docs/commits?author=brisvag))  - @brisvag
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) ([docs](https://github.com/napari/docs/commits?author=psobolewskiPhD))  - @psobolewskiPhD
- [Rahul Kumar](https://github.com/napari/napari/commits?author=rahul713rk) - @rahul713rk
- [rwkozar](https://github.com/napari/napari/commits?author=rwkozar) - @rwkozar
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko


## 18 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Carol Willing](https://github.com/napari/napari/commits?author=willingc) ([docs](https://github.com/napari/docs/commits?author=willingc))  - @willingc
- [Constantin Aronssohn](https://github.com/napari/docs/commits?author=cnstt) - @cnstt
- [Daniel Althviz Moré](https://github.com/napari/docs/commits?author=dalthviz) - @dalthviz
- [Davis Bennett](https://github.com/napari/docs/commits?author=d-v-b) - @d-v-b
- [Draga Doncila Pop](https://github.com/napari/docs/commits?author=DragaDoncila) - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) ([docs](https://github.com/napari/docs/commits?author=Czaki))  - @Czaki
- [Jacopo Abramo](https://github.com/napari/docs/commits?author=jacopoabramo) - @jacopoabramo
- [jaime rodraguez-guerra](https://github.com/napari/docs/commits?author=jaimergp) - @jaimergp
- [Juan Nunez-Iglesias](https://github.com/napari/docs/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) ([docs](https://github.com/napari/docs/commits?author=brisvag))  - @brisvag
- [Lukasz Migas](https://github.com/napari/docs/commits?author=lukasz-migas) - @lukasz-migas
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) ([docs](https://github.com/napari/docs/commits?author=psobolewskiPhD))  - @psobolewskiPhD
- [Rahul Kumar](https://github.com/napari/napari/commits?author=rahul713rk) - @rahul713rk
- [rwkozar](https://github.com/napari/napari/commits?author=rwkozar) - @rwkozar
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko
- [Wouter-Michiel Vierdag](https://github.com/napari/docs/commits?author=melonora) - @melonora
- [Yaroslav Halchenko](https://github.com/napari/docs/commits?author=yarikoptic) - @yarikoptic

