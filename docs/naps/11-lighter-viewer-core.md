(nap-11-lighter-viewer-core)=

# NAP-11 — A lighter viewer core

```{eval-rst}
:Author: Aniket Singh Yadav <singhyadavaniket43@gmail.com>
:Created: 2026-11-02
:Status: Draft
:Type: Standards Track
```

## Purpose

napari has grown around its viewer, and the viewer pays for it. A script that
shows one image loads about 1,360 modules and waits several seconds for the
first paint; `pip install napari` brings 106 packages. Most of that is not the
viewer.

napari-lite put a number on this. It is a copy of napari's viewer core, kept in
sync with napari's main, with the application around it removed and the clock
running. The copy showed the cost sits in three separable places:

- imports and once-per-run work that a script pays for and never uses;
- a model that imports vispy, app-model, npe2 and magicgui when it needs only a
  few names from each;
- a window fused with its canvas, so there is nowhere to put another renderer
  or a front end that is not Qt.

Leaving out the menus, plugins and console is what makes napari-lite a
different product. It saves about 0.15 s. It is not what makes it fast.

This NAP brings those findings back into napari one decision at a time. Each
item says what it costs now, what it saves, and what a user or plugin would
notice afterwards, so maintainers can take or leave each one on its own. Phases
1 and 2 change no behavior. Phase 3 is for discussion, not decided. napari-lite
stays the place where each change is tried first, against napari's own tests,
and the list of differences between the two codebases is the list of what is
left to do. The plan will change as items land.

## Definitions

This NAP uses the following terms.

*Model* - `ViewerModel`, the layers, dims, camera, cursor and their events.
The part of the viewer that holds state and knows nothing about drawing.

*Renderer* - The code that draws the model: today napari's `VispyCanvas`
with the vispy layer visuals, plus the wiring that `QtViewer` holds for
them.

*Front end* - Where the renderer's output is shown and where input comes
from: the Qt `Window` today; a notebook cell or no window at all in
napari-lite.

*Headless viewer* - A viewer with a renderer and no front end. It draws off
screen, so `screenshot()` and `export_figure()` work, and nothing else is
shown.

*Stand-in* - A small object that takes the place of a heavy library's
object until the library is needed, and is equal to it in every way the
surrounding code can observe. napari-lite uses two: a zero-column feature
table in place of a pandas DataFrame, and a `pixel` unit in place of
pint's.

*Extra* - An optional dependency group, installed as
`pip install napari[name]`.

*Rule* - One `[[rewrite]]` entry in napari-lite's `tools/vendor.toml`: a
text replacement applied to napari's code at every resync. Every
difference between napari-lite's copied code and napari is one rule, which
is what makes the differences countable.

## Motivation and Scope

### Where the time goes

A script that opens a napari window with one image waits about six seconds
on a slow laptop and about a second and a half on a CI runner. Step by
step, with napari-lite next to it, in seconds on one Windows laptop with
both packages installed into fresh environments (napari at `main`,
napari-lite at the matching commit; the ratios matter more than the
seconds):

| step | napari | napari-lite |
|---|---|---|
| load the viewer model (`napari.components`) | 2.65 | 0.88 |
| load the window code (Qt, vispy) | 1.07 | 0.91 |
| make the viewer | 0.78 | 0.66 |
| add the first image | 0.74 | 0.10 |
| everything else (numpy, Qt start, first paint) | 0.54 | 0.69 |
| **total** | **5.78** | **3.24** |

Two steps make the difference: loading the model and adding the first
image. The window costs about the same in both, because Qt, vispy and the
first OpenGL context are the same work in both, and napari's menus,
plugin discovery and console account for only about 0.15 s of it. Leaving
the application out is what makes napari-lite a different product; it is
not what makes it fast.

The absolute gaps shrink on CI runners with fast disks and warm caches:
on a Linux runner the first image takes 0.95 s in napari-lite against
1.05 s in napari, on a macOS runner 0.59 s against 1.99 s. The module
counts do not depend on the machine: the first image loads about 630
modules in napari-lite and about 1,360 in napari [^benchmarks].

### Where the install goes

| | napari | napari-lite |
|---|---|---|
| packages installed | 106 | 31 |
| installed size | 761 MB | 370 MB |
| direct dependencies | 37 | 14 |

330 MB of napari-lite is Qt, numpy, vispy and PyOpenGL, the floor of any
Qt viewer in Python. The rest of the difference is packages napari
requires for a handful of functions (scikit-image for four drawing
functions and two color conversions, scipy for rotations and a few
filters, toolz for two functions, wrapt for one base class), or imports
at startup for features that may never be used.

### Where the coupling is

In napari, `napari.components` imports vispy (for color names, key names
and two Shapes geometry helpers), app-model (for key names), npe2 and
magicgui. Anything that uses napari's layers loads all of these: a test of
the layer model, a notebook that only wants a screenshot, a server with no
display. The Qt window and the vispy canvas are created together in
`QtViewer`, so there is no supported way to draw the model somewhere else,
or to show it without Qt.

### Who it affects

- People who open napari from a script or a terminal many times a day, and
  wait at every start.
- People who embed the viewer in their own Qt application, run it in a
  notebook on a remote machine, or render figures on a server with no
  display. They need the viewer without the application.
- Plugin and downstream developers whose test-suites import
  `napari.components` and pay the full import on every run.
- Users on small or managed machines, where 760 MB and 106 packages are a
  cost in themselves.
- Anyone who wants a second renderer behind napari (NAP-10 [^nap-10] and
  issue #7373 [^issue-7373] discuss pygfx), who today has nowhere to put
  it.

### Goals

1. **A faster first image with nothing taken away.** Remove the imports and
   the once-per-run work that a script pays for without using them, and
   keep them from coming back with a test.
2. **A model that imports only what a model needs.** `napari.components`
   and `napari.layers` import without vispy, app-model, npe2 or magicgui.
   The application imports them when it starts.
3. **A smaller required install.** Packages napari uses for a few functions
   are replaced by tested code; packages that serve one feature become
   extras of that feature.
4. **A documented seam between model, renderer and front end.** One
   contract that a renderer fulfils and one that a front end fulfils, so
   that the Qt window stays as it is and other renderers and front ends
   can be added from separate packages.

### Non-goals

- Replacing vispy or Qt. The Qt window drawn by vispy stays the default
  and is unchanged by this NAP.
- Changing the plugin system, the menus, the console, the preferences or
  the layout of the window. napari-lite leaves those out; this NAP does
  not propose that napari does.
- Making a single slice or draw faster. Slice stepping and painting take
  the same time in both packages, as they should: the code is the same.
- Making napari-lite napari's core package (see Alternatives).
- Multiple views (NAP-9 [^nap-9]). The seam in goal 4 is what NAP-9 needs,
  but views are its subject, not this NAP's.

## Detailed Description

### Design principles

The items below were chosen by these rules, which also say how to judge a
pull request that implements one.

- **Same API, same pixels.** Every public name, signature and rendered
  pixel stays the same, except where an item says so. Where an item
  replaces library code, the replacement is compared with the library
  element by element in a test.
- **Remove the import, do not hide it.** An import that runs at startup
  is moved to the code path that needs it, or removed. Generic lazy
  loading would keep the dependency and move the error (see
  Alternatives).
- **Extras rather than removal.** A package that serves one feature
  becomes an extra of that feature, with an `ImportError` that names the
  extra at the point of use. Nothing is dropped.
- **Stand-ins must be equal.** A stand-in is equal to the object it
  replaces in every comparison and operation the surrounding code
  performs, converts to the real object on first real use, and is tested
  for both.
- **A protocol, not a base class.** The renderer and front-end contracts
  are `typing.Protocol`s. Existing classes fulfil them without inheriting
  from anything new, and a package can provide one without importing
  napari's Qt code.
- **Measured, not asserted.** Each item names the gain measured in
  napari-lite's benchmarks, in a fresh environment, and the pull request
  that implements it should repeat the measurement.

### Phase 1: small fixes, no behavior change

These are the imports and the work that a script pays for without using
them. Each is a contained pull request.

1. **Write the theme icons only when they change.** Loading
   `napari.utils.theme` writes 316 icon files to disk on every run, 0.17
   to 0.29 s, even in a script with no window. napari-lite writes them
   once behind a stamp file and checks the stamp afterwards.
2. **Shrink thumbnails with numpy, not `scipy.ndimage`.** The thumbnail
   uses `ndimage.zoom` with `order=0`, which is a nearest-neighbor
   lookup; the import costs 0.42 s and about 195 modules at the first
   image, and the zoom runs on every slice. Twenty lines of numpy return
   the same pixels. One visible difference, for the better: where
   floating-point error puts the last coordinate a hair past the last
   pixel, scipy's default mode blanks that row or column; the numpy
   version uses the edge pixel. A patch exists [^upstream].
3. **Build pint's registry from its cache.** The first layer's `pixel`
   unit makes pint parse its unit definitions from text, 0.20 s; with
   `cache_folder` set on the registry, pint loads them in 0.02 s.
4. **Read plugin theme contributions when plugins start, not at import.**
   `napari.utils.theme` reads every installed plugin's manifest while
   being imported, 0.15 s without a window; napari reads them again when
   it makes the viewer.
5. **Skip the xarray check until xarray is imported.** Every new layer
   runs `_check_xarray`, which imports xarray, and pandas with it,
   whenever xarray is installed: about 450 modules, a second on a slow
   disk. An xarray object can only exist once `xarray` is in
   `sys.modules`, so the check can be skipped until then. A patch exists.
6. **Import plain dask only where it is used.** `dask.array` already
   stays out of startup [^pr-8720]; the `dask` package itself still
   arrives with the model, 0.18 s on the laptop and about 0.05 s on CI.
7. **A first-image test and a first-image benchmark.** A test that opens
   a viewer with one image in a fresh interpreter and fails if a package
   from a short list (scipy, pandas, xarray, dask, scikit-image, pint's
   parser) arrives, so that items 1 to 6 do not come back. napari's ruff
   rule against top-level imports of scipy, pandas and `dask.array`
   [^pr-8815] catches module-level imports; it does not see an import
   inside a function that still runs at startup (item 3) or startup work
   that is not an import (items 1 and 4). napari-lite's
   `tests/test_startup_imports.py` and `bench/bench_imports.py` are the
   model; the benchmark belongs next to napari's `import napari`
   benchmark.
8. **Layer controls for layers that exist before the container.** The
   controls container makes widgets only for layers inserted after it
   exists, so a `ViewerModel` that already holds layers, handed to a
   `QtViewer` for embedding, shows no controls for them and raises
   `KeyError` at the first selection change. A patch with a test exists.
9. **Two cheaper repaints while painting.** The layer list renders the
   layer-type icon from SVG on every repaint (`SVGBufferIconEngine.paint`
   builds a `QSvgRenderer` each time), 0.4 ms per brush point; a pixmap
   cached per size removes it. The brush circle is two antialiased
   ellipse visuals, 1.5 ms a frame on an integrated GPU; a line or markers
   visual would be cheaper.
10. **Stop the dims playback thread when its widget closes.**
    `QtDims.closeEvent` schedules the widget's deletion without stopping
    its animation thread; Qt ends the process when a running `QThread` is
    deleted, and pytest-qt closes a test's widgets before fixtures run, so
    a failed playback test takes the whole run down. One line,
    `self.stop()`, before the deletion.
11. **Console notifications on legacy encodings.** On Windows with piped
    output, a message with a character outside cp1252 raised inside
    `print`, and the message was lost. Encoding with `errors='replace'`
    first shows it. A patch with a test exists.

Already in napari, and the reason the list is not longer: pandas is kept
out of startup [^pr-8733], `dask.array` too [^pr-8720], and the import of
scipy's `Rotation` in `canvas_to_world` moved to the 3D path [^pr-9746],
where napari-lite had carried it as a rule.

Items 1 to 6 were tried together on a copy of napari `main` (commit
`6b8d52f0`), on the laptop of the table above:

| | before | after |
|---|---|---|
| model plus first image | 3.2 s | 2.2 s |
| window with one image | 5.9 s | 4.8 s |
| modules loaded at the first image | 1,361 | 1,148 |

### Phase 2: a model that loads less

These keep the API and move imports to where they are used.

12. **app-model, npe2 and magicgui only when the application needs them.**
    The model imports app-model for key names, npe2 for the plugin
    manager and magicgui for the layer type registration. Scripts,
    notebooks and tests that use only the model pay about 0.5 s for them.
    napari-lite keeps copies of the two key-type files it needs and
    registers nothing until a window exists.
13. **vispy out of the model.** The model takes color names and parsing,
    key names, a rotation matrix and an exception helper from vispy, and
    the Shapes layer two geometry helpers. Own versions of the first four
    are small and are tested against vispy's; the geometry helpers can be
    imported when first used. With this, `napari.components` and
    `napari.layers` import without vispy, which napari-lite verifies in a
    subprocess with vispy blocked and in a CI job with vispy uninstalled.
14. **The few uses of toolz, wrapt and pydantic-extra-types.** Two
    functions from toolz, one proxy base class from wrapt (the part of
    `wrapt.ObjectProxy` napari uses; wrapt also imports asyncio, 46
    modules in a window), and the `Color` class from pydantic-extra-types,
    copied under its MIT license. Some of these packages still arrive
    through other dependencies; the point is that napari stops requiring
    them.

### Phase 3: changes that need a decision first

Each of these is a measured gain and a small visible difference. They are
listed with the difference stated, so the decision can be made on it.

#### 15. pandas only when a layer has features

Every Points, Shapes, Labels, Vectors and Surface layer builds a feature
table on creation, which imports pandas, about 530 modules and 0.5 s, for
layers that never get a feature. napari-lite serves a layer without
features from a zero-column stand-in until pandas is in the process; the
first read of `layer.features` or `feature_defaults`, the first feature,
or any import of pandas elsewhere turns it into a real DataFrame.
`layer.features` gives a DataFrame whenever it is read, as the API says.

The difference: with pandas as an extra, the first feature on a layer in
an environment without pandas raises an `ImportError` naming the extra,
and Tracks (which always has a `track_id` feature) needs the extra. With
pandas kept as a required dependency there is no visible difference, only
the gain.

#### 16. A pixel unit without pint

Every layer's default unit is pint's `pixel`, so pint loads with the first
layer: about 0.4 s and 340 modules, half of the first image in a fresh
environment, with item 3 taking care of the registry on top. napari-lite's
default is a `str` subclass equal to pint's pixel unit in both directions,
with the pint unit built on demand for arithmetic and formatting; pint
loads only when a layer gets a real unit.

The difference: `layer.units` holds that stand-in rather than a `pint.Unit`
until a real unit is set, which code that checks `isinstance(unit,
pint.Unit)` would notice. This item should be measured again after item 3
has landed; if the cache leaves little to gain, it can be dropped.

#### 17. Library functions replaced with tested numpy code; heavy packages as extras

scikit-image and scipy leave the required dependencies; pandas, dask, scipy and
tifffile become extras. napari uses four drawing functions and two color
conversions from scikit-image, and rotations, QR and RQ decompositions, a
geometric mean, two morphology filters and the Tracks nearest-vertex lookup
from scipy. napari-lite has numpy versions of each, compared with the originals
element by element in tests; spline-interpolated shapes keep scipy as an extra.
This halves the install.

The difference: users who expect those packages to come with napari
install an extra; and one known trade, the Tracks layer finds the vertices
nearest to the cursor by distance over all vertices instead of a KD-tree,
a few milliseconds per status update for a million vertices.

#### 18. A documented seam between the model, the renderer and the front end

napari-lite's viewer is three parts meeting at two contracts, both Python
protocols [^backends]:

```python
class CanvasBackend(Protocol):
    """What a front end uses from a renderer; it follows the model by itself."""

    native: Any  # the widget to place, or None

    def screenshot(
        self,
        *,
        size=None,
        scale=1.0,
        fit_to_data_extent=False,
        device_pixel_ratio=None,
    ) -> np.ndarray: ...
    def key_event(self, event, *, release=False) -> None: ...
    def close(self) -> None: ...


class Window(Protocol):
    """What a Viewer uses from its window."""

    def show(self, *, block=False) -> None: ...
    def close(self) -> None: ...
    def activate(self) -> None: ...
    def resize(self, width, height) -> None: ...
    def set_geometry(self, left, top, width, height) -> None: ...
    def geometry(self) -> tuple[int, int, int, int]: ...
    def screenshot(
        self,
        path=None,
        size=None,
        scale=None,
        flash=False,
        canvas_only=False,
    ) -> np.ndarray: ...
    def export_figure(self, path=None, *, scale=1, flash=False) -> np.ndarray: ...
    def clipboard(self, flash=False, canvas_only=False) -> None: ...
    def add_dock_widget(self, widget, *, name='', area=None, **kwargs) -> Any: ...
    def remove_dock_widget(self, widget, menu=None) -> None: ...
    def register_task_status(
        self,
        provider,
        task_status,
        description='',
        cancel_callback=None,
    ) -> uuid.UUID: ...
    def update_task_status(self, task_status_id, status, description='') -> bool: ...
```

A renderer is made as `Renderer(viewer, *, gui=None, parent=None)` and
keeps itself in step with the model; the vispy one is napari's
`VispyCanvas` plus the wiring that `QtViewer` holds today, with the Qt
parts behind a flag. A front end is made as
`Window(viewer, *, show=True, renderer=None)` and asks the renderer for
its `native` widget, or draws without one. With that:

```python
import napari

napari.Viewer()  # the Qt window, drawn by vispy: as today
napari.Viewer(gui=None)  # no window: screenshot() and export_figure() work
napari.Viewer(gui='jupyter')  # the viewer as widgets in a notebook cell
napari.Viewer(renderer='pygfx')  # another renderer, registered by entry point
QtViewer(viewer, renderer=MyRenderer)
```

`gui=None` draws off screen; on Linux with EGL, with no Qt in the process
at all. `gui='jupyter'` streams the frames of that off-screen canvas
through a `jupyter_rfb` widget [^jupyter-rfb], with napari's mouse and key
handling on the browser's events, dims sliders, a layer list and
`add_dock_widget` for ipywidgets around it. Other packages register
renderers and front ends under two entry-point groups, and an environment
variable selects a default. Nothing changes for `napari.Viewer()`.

This is also the shape NAP-9 needs: a view is a renderer with a model,
placed by a front end. And it is where NAP-10's "backend integration"
phase puts the translation between backend events and napari's own.

## Related Work

### Inside napari

- Issue #5940, "napari-lite" [^issue-5940], asked for a pared-down viewer
  with instant launch and fewer dependencies. napari-lite is one answer to
  it, and this NAP is the part of that answer that can live in napari.
- Issue #7373, "Disentangling events for multiple rendering backends"
  [^issue-7373], found the vispy coupling an obstacle to a second
  renderer. Items 13 and 18 remove the model's part of that coupling.
- NAP-4, asynchronous slicing [^nap-4]: the headless and notebook front
  ends reuse its slicer unchanged. The off-screen renderer applies slicing
  results on the canvas's thread, queued until the next screenshot when
  no event loop runs.
- NAP-9, multiple views [^nap-9], separates view state from the viewer
  window and needs the same seam between model, renderer and window as
  item 18. Its design considerations mention napari-lite as a possible
  lightweight view.
- NAP-10, migration of the event system [^nap-10], asks that
  backend-specific communication stay inside integration layers. The
  renderer contract of item 18 is such a layer.
- The startup work already done in napari: pandas out of startup
  [^pr-8733], `dask.array` out of startup [^pr-8720], the 3D-only scipy
  import moved [^pr-9746], and the ruff rule against top-level heavy
  imports [^pr-8815]. This NAP continues that work and adds the test that
  the ruff rule cannot be.

### Elsewhere

- vispy's own `jupyter_rfb` backend needs a GL context from glfw or a
  hidden Qt canvas. napari-lite's notebook front end draws with the same
  off-screen canvas as its headless viewer instead, so it works on a
  server with no display and no Qt.
- ndv [^ndv], the n-dimensional viewer from pyapp-kit, is built as a model
  with interchangeable canvas backends (vispy, pygfx) and front ends (Qt,
  Jupyter, wx). Item 18 gives napari the same shape without changing what
  `napari.Viewer()` does.
- PEP 562 module `__getattr__` [^pep-562], which `napari.utils` already
  uses for lazy attributes, and which napari-lite asks superqt to adopt
  (see Implementation).
- pygfx [^pygfx] as a second renderer: napari-lite's view-only canvas
  draws the same model with vispy and with pygfx and matches them pixel
  for pixel, a dress rehearsal for a second renderer behind the contract
  of item 18.

## Implementation

The phases are independent of each other; each item within a phase is one
pull request, in the order given, smallest first. The pull requests will
be linked from here as they open.

### Phase 1: items 1 to 11

No API or behavior change beyond the thumbnail edge pixel of item 2,
which the pull request should state. Items 2, 5, 8 and 11 start from the
patches in napari-lite's `docs/upstream/`. Item 7 adds the test that keeps
the rest honest and should land before or with item 1, so that each later
item extends its allowed list by removing a package from it. Item 3 is a
two-line change in the unit registry helper. Items 9 and 10 are
independent of the rest and of each other. Item 6 may be omitted if the
measurement on napari `main` shows less than 0.05 s on CI.

### Phase 2: items 12 to 14

Lazy imports and own copies; the public API does not move. Item 13 needs
four small modules (color names and parsing, key names, the rotation
matrix, the exception helper) with their comparison tests, which
napari-lite has under `napari_lite/utils/`; the Shapes geometry helpers
are imported on first use. Item 12 needs the decision in the open
questions on where the key types live when app-model is not imported.
Item 14 can land in any order and may be split per package. The phase is
complete when the startup-import test of item 7 asserts that `import
napari.components` loads neither vispy nor app-model, npe2 nor magicgui.

### Phase 3: items 15 to 18

Each needs its own discussion; this NAP lists them so the discussion can
start from measured gains and stated differences. Items 15 and 16 are
small changes once decided (a stand-in module and a rule each in
napari-lite). Item 17 is one pull request per replaced package, each with
its comparison test, and a final one that moves the packages to extras.
Item 18 is the largest and the one with the most reuse value; napari-lite's
`docs/backends.md` and `napari_lite/backends/__init__.py` are the written
contract, and its `_vispy/backend.py`, `backends/headless.py` and
`backends/jupyter.py` the three implementations. It can be done in steps:
first the renderer contract with the vispy renderer fulfilling it and
`QtViewer` taking a `renderer=`, then the headless front end, then the
notebook one.

### Asks to dependencies

Three asks go to dependencies rather than napari, and are written up ready
to file in napari-lite's `docs/upstream.md` [^upstream]:

- superqt: lazy attributes in `superqt/__init__.py` (PEP 562) and pygments
  as an optional dependency of its syntax highlighter. A viewer that needs
  two sliders and the thread workers loads 35 superqt modules and
  pygments, 0.16 s of a window's first frame.
- pint: import `dask.base` lazily. `pint/compat.py` imports it at import
  time whenever dask is installed, and dask brings PyYAML, toolz, psutil
  and cloudpickle: about 70 modules and 0.25 s for every program that
  imports pint in an environment with dask.
- vispy: load its fonts on first use rather than at package import, 0.3 s
  and 50 modules before any canvas exists, paid by `import vispy.color`
  alone.

PyOpenGL's `OpenGL.GL` import (0.3 s, about 190 modules, through vispy's
`gl+` backend that napari's markers need) is a question to both projects
rather than an ask.

### Success criteria

- **Phase 1.** A first-image test runs in napari's CI with a short list of
  packages that may load, and the modules loaded at the first image fall
  from about 1,360 to about 1,150 with no change to any test's expected
  output but the thumbnail edge pixel.
- **Phase 2.** `import napari.components` and `import napari.layers`
  succeed in an environment with vispy uninstalled, and load neither
  app-model, npe2 nor magicgui; a layer-model test-suite runs without a
  display.
- **Phase 3.** `napari.Viewer(gui=None).screenshot()` returns an image on
  a Linux machine with no display and no Qt installed; a renderer
  registered by another package draws in the unchanged Qt window; the
  required install of `napari[pyqt6]` is measurably smaller, with each
  moved package reachable through a named extra.

### Open questions

- this section is incomplete, so i guess no-one can see lets say this is the
  place where we will discuss the equation of `Theory of Everything`😿

## Backward Compatibility

Phase 1 and Phase 2 keep every public name, signature and behavior, with
one exception already named: a thumbnail's last row or column, which scipy
sometimes blanked, now shows the edge pixel. The first-image test of item
7 constrains future contributions: an import that runs at the first image
has to be added to its list on purpose.

Phase 3 has visible differences, each stated in its item. pandas and some
other packages become extras that users of those features install, which
changes what `pip install napari` brings; `napari[all]` can keep the
previous set. `layer.units` holds a pixel stand-in rather than a
`pint.Unit` until a real unit is set. `Viewer` gains `gui=` and
`renderer=` with defaults that give exactly today's window.

Plugins that reach into `viewer.window._qt_window` or
`viewer.window._qt_viewer` keep working with the Qt front end, which stays
the default. With a notebook front end or no window those attributes are
absent, as they are in napari-lite, where `viewer.window` raises
`AttributeError` for a headless viewer so that `hasattr` says so.

## Future Work

- A pygfx renderer behind the contract of item 18, after the one that
  napari-lite's view-only canvas already has.
- Multiple views (NAP-9) on the same seam: a view as a renderer with its
  own dims and camera, placed by the front end.

## Discussion

- Earth 🌏 (i'll be updating more precise location)

## References and Footnotes

[^napari-lite]: napari-lite, <https://github.com/Aniketsy/napari-lite>

[^issue-14]: "[Roadmap]: What napari can take from napari-lite",
    <https://github.com/Aniketsy/napari-lite/issues/14>

[^issue-7373]: "Disentangling events for multiple rendering backends",
    <https://github.com/napari/napari/issues/7373>

[^nap-4]: NAP-4 — Asynchronous slicing,
    <https://napari.org/dev/naps/4-async-slicing.html>

[^nap-9]: NAP-9 — Multiple Views,
    <https://napari.org/dev/naps/9-multiple-canvases.html>

[^nap-10]: NAP-10 — Migration of the event system,
    <https://napari.org/dev/naps/10-migration-event-system.html>

[^pr-8720]: `dask.array` kept out of startup,
    <https://github.com/napari/napari/pull/8720>

[^pr-8733]: pandas kept out of startup,
    <https://github.com/napari/napari/pull/8733>

[^pr-9746]: scipy's `Rotation` imported in `canvas_to_world` on the 3D
    path only, <https://github.com/napari/napari/pull/9746>

[^pr-8815]: ruff rule against top-level imports of scipy, pandas and
    `dask.array`, <https://github.com/napari/napari/pull/8815>

[^benchmarks]: napari-lite, `docs/benchmarks.md`: what is measured, how,
    and the numbers on three operating systems,
    <https://github.com/Aniketsy/napari-lite/blob/main/docs/benchmarks.md>

[^upstream]: napari-lite, `docs/upstream.md` and `docs/upstream/`: the
    patches for napari and the asks for its dependencies,
    <https://github.com/Aniketsy/napari-lite/blob/main/docs/upstream.md>

[^backends]: napari-lite, `docs/backends.md`: the renderer and front-end
    contracts,
    <https://github.com/Aniketsy/napari-lite/blob/main/docs/backends.md>

[^architecture]: napari-lite, `docs/architecture.md`: what is copied, what
    is own code, and how the copy is kept in sync,
    <https://github.com/Aniketsy/napari-lite/blob/main/docs/architecture.md>

[^jupyter-rfb]: jupyter_rfb, remote frame buffer widgets for Jupyter,
    <https://github.com/vispy/jupyter_rfb>

[^ndv]: ndv, <https://github.com/pyapp-kit/ndv>

[^pep-562]: PEP 562 — Module `__getattr__` and `__dir__`,
    <https://peps.python.org/pep-0562/>

[^pygfx]: pygfx, <https://github.com/pygfx/pygfx>

All NAPs should be declared as dedicated to the public domain with the CC0
license [^id3], as in `Copyright`, below, with attribution encouraged with
CC0+BY [^id4].

[^id3]: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication,
    <https://creativecommons.org/publicdomain/zero/1.0/>

[^id4]: <https://dancohen.org/2013/11/26/cc0-by/>

## Copyright

This document is dedicated to the public domain with the Creative Commons CC0
license [^id3]. Attribution to this source is encouraged where appropriate, as
per CC0+BY [^id4].
