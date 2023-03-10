# napari 0.4.3

We're happy to announce the release of napari 0.4.3!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).


For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## Highlights
In this release we've added two new analysis and GUI focused [hook specifications](https://github.com/napari/napari/blob/87961d0554b2bb1574553e23bf2231a9a5117568/docs/source/plugins/hook_specifications.rst) for our plugin developers ({pr}`2080`).

The first one `napari_experimental_provide_function_widget` allows you to provide a function or list of functions that we
will turn into a GUI element using using [magicgui](https://napari.org/magicgui/). This hook spec leverages the newly added and the `viewer.window.add_function_widget` method ({pr}`1856`) and the newly recently released `0.2` series of magicgui which seperates out an abstract function and widget API from its Qt backend. These functions can take in and return napari layer, allowing you to
provide analysis functionality to napari without having to write GUI code.

The second one `napari_experimental_provide_dock_widget` allows you to provide a QWidget or list of QWidgets that we will instantiate with access to the napari viewer and add to the GUI. This hook spec leverages our `viewer.window.add_dock_widget` method, and allows you to provide highly customized GUI elements that could include additional plots or interactivity.

Both of these hook specs are marked as `experimental` as we're likely to evolve the API here in response to user needs, and we're excited to get early feedback from plugin developers on them.

In this release we also seperate out more of the Qt functionality from napari making it easier to run headless ({pr}`2039`, {pr}`2055`). We also added a `napari.run` method as an alternative to using the `napari.gui_qt` context manager ({pr}`2056`).

We've also made good progress on our `experimental` support for an octree system for rendering large 2D multiscale images. You can try this functionality setting `NAPARI_OCTREE=1` as an environment variable. See our [asynchronous rendering guide](https://napari.org/guides/rendering.html) for more details on how to use the octree and its current limitations.

Finally we've added our [0.4 series roadmap](https://napari.org/roadmaps/0_4.html) and a [retrospective on our 0.3 roadmap](https://napari.org/roadmaps/0_3_retrospective.html)!


## New Features
- Add support for function widgets ({pr}`1856`)
- Gui hookspecs ({pr}`2080`)


## Improvements
- Use evented dataclass for dims ({pr}`1917`)
- Add information about screen resolution ({pr}`1957`)
- Add asdict and update to evented dataclass ({pr}`1966`)
- async-30: ChunkLoader Stats ({pr}`1972`)
- async-31: Fix Monitor Feature Toggle ({pr}`1975`)
- octree: Fix float64 and check downscale ratio ({pr}`1976`)
- async-32: Faster Octree Rendering ({pr}`1977`)
- async-33: Cleanup QtPoll and Tiled Visuals ({pr}`1980`)
- async-34: Octree Performance ({pr}`1989`)
- async-35: OctreeDisplayOptions ({pr}`1991`)
- async-36: New OctreeChunkLoader ({pr}`1992`)
- async-37: Multilevel Rendering ({pr}`1995`)
- async-38: Better Multilevel Rendering ({pr}`1997`)
- async-39: Better Config and Remove Qt Code ({pr}`1999`)
- Improve label paint lag ({pr}`2000`)
- async-40: Shared Memory Resources ({pr}`2004`)
- async-41: Better Octree Performance ({pr}`2010`)
- Start magicgui apps too ({pr}`2016`)
- async-42: New LoaderPool and remove ChunkKey ({pr}`2025`)
- Two small path improvements ({pr}`2030`)
- Cleanup dockwidget removal ({pr}`2036`)
- Add a MousemapProvider ({pr}`2040`)
- Cleanup warnings in tests ({pr}`2041`)
- async-43: New LoaderPoolGroup ({pr}`2049`)
- Complete qt isolation ({pr}`2055`)
- Create QApplication on demand in viewer.Window, add napari.run function ({pr}`2056`)
- Remove global app logic from Window init ({pr}`2065`)
- async-45: Docs and Cleanup ({pr}`2067`)
- Better bound magicgui viewer ({pr}`2100`)
- reduce call of _extent_data in layer ({pr}`2106`)


## Bug Fixes
- Fix append and remove from layerlist ({pr}`1955`)
- Change label tooltip checkbox ({pr}`1978`)
- Fix cursor size ({pr}`1983`)
- Fix layer removing by disconnecting each event individually ({pr}`1984`)
- Compatibility with magicgui v0.2.0 ({pr}`1994`)
- Skip rounding of numbers when comparing data slice ({pr}`2017`)
- Fix InitVar problem ({pr}`2023`)
- Fix channel_axis for affine transforms in add_image ({pr}`2026`)
- Fix typos in theme event and vispy camera ({pr}`2034`)
- Fix magicgui test funcs ({pr}`2044`)
- Fix magicwidget.native detection of "empty" widgets ({pr}`2046`)
- async-44: Fix Pixel Shift Bug ({pr}`2052`)
- Fix missing console widget ({pr}`2063`)
- Save app reference in Window init ({pr}`2076`)
- Add deprecated parameters for updating theme ({pr}`2074`)
- Coerce name before layer is added to layerlist ({pr}`2087`)
- Fix stale data in magicgui `*Data` parameters ({pr}`2088`)
- Make dock widgets non-tabbed ({pr}`2096`)
- Fix overly strict magic kwargs ({pr}`2099`)
- Undo calling pyrcc with python sys.executable ({pr}`2102`)


## API Changes
- The ``axis`` parameter is no longer present on the ``current_step``, ``range``, or ``axis_labels`` events. Instead a single event is emitted whenever the tuple changes ({pr}`1917`)
- The deprecated public layer dims has been removed in 0.4.2 and the private ``layer._dims`` is now a NamedTuple ({pr}`1919`)
- The deprecated ``layer.shape`` arrtibute has been removed. Instead you should use the ``layer.extent.data`` and ``layer.extent.world attributes`` to get the extent of the data in data or world coordinates ({pr}`1990`, {pr}`2002`)
- Keymap handling has been moved off the ``Viewer`` and ``Viewer.keymap_providers`` has been removed. The ``Viewer`` itself
can still provide keymappings, but no longer handles keymappings from other objects like the layers. ({pr}`2003`)
- Drop scale background color and axes background color. These colors are now determined by defaults or the canvas background color. ({pr}`2037`)
- ``event.text`` was renamed ``event.value`` for the events emitted when changing ``Viewer.status``, ``Viewer.title``,
``Viewer.help``, and ``event.item`` was renamed ``event.value`` for the event emitted when changing ``Viewer.active_layer`` ({pr}`2038`)


## Deprecations
- The ``Viewer.interactive`` parameter has been deprecated, instead you should use ``Viewer.camera.interactive`` ({pr}`2008`)
- The ``Viewer.palette`` attribute has been deprecated. To access the palette you can get it using ``napari.utils.theme.register_theme`` dictionary using the ``viewer.theme`` as the key ({pr}`2031`)
- Annotating a magicgui function with a return type of ``napari.layers.Layer`` is deprecated. To indicate that your function returns a layer data tuple, please use a return annotation of ``napari.types.LayerDataTuple`` or ``List[napari.types.LayerDataTuple]``({pr}`2079`)


## Build Tools and Support
- 0.4 roadmap ({pr}`1906`)
- Rename artifact for nightly build releases ({pr}`1971`)
- Update latest tag alone with nightly build ({pr}`2001`)
- Only raise leaked widgets errors in tests if no other exception was raised ({pr}`2043`)
- Bump minimum numpy requirement to 1.16.5  ({pr}`2050`)
- Tox tests on github actions ({pr}`2051`)
- Move all requirements to extras ({pr}`2054`)
- Drop additional perfmon test pass ({pr}`2058`)
- Fix name in gha test ({pr}`2059`)
- Fix big sur on GHA and fix failed test template ({pr}`2061`)
- Update bundle.py ({pr}`2064`)
- Update pre-commit  and add pyupgrade ({pr}`2068`)
- Skip perfmon test on python 3.9 on CI ({pr}`2073`)
- async-46: Rendering Guide and Code Comments ({pr}`2078`)
- Update get-tag action ({pr}`2083`)
- Update magicgui examples ({pr}`2084`)
- Add examples tests ({pr}`2085`)
- Skip testing examples on CI ({pr}`2094`)
- Fix roadmap headings in docs ({pr}`2097`)
- Add PR 2106 to 0.4.3 release notes ({pr}`2107`)
- Fix `pytest --pyargs napari` test on pip install. Add CI test ({pr}`2109`)


## 9 authors added to this release (alphabetical)

- [Alister Burt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Heath Patterson](https://github.com/napari/napari/commits?author=NHPatterson) - @NHPatterson
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [kir0ul](https://github.com/napari/napari/commits?author=kir0ul) - @kir0ul
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Philip Winston](https://github.com/napari/napari/commits?author=pwinston) - @pwinston
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Ziyang Liu](https://github.com/napari/napari/commits?author=ziyangczi) - @ziyangczi


## 7 reviewers added to this release (alphabetical)

- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Philip Winston](https://github.com/napari/napari/commits?author=pwinston) - @pwinston
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Ziyang Liu](https://github.com/napari/napari/commits?author=ziyangczi) - @ziyangczi

