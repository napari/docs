# napari 0.4.8

We're happy to announce the release of napari 0.4.8!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).

This release comes with a **big** change with how you use napari: you should no
longer wrap viewer calls in the `with napari.gui_qt():` context. Instead, when
you want to block and call the viewer, use `napari.run()`. A minimal example:

```python
import napari
from skimage import data

camera = data.camera()
viewer = napari.view_image(camera)
napari.run()
```

In interactive workspaces such as IPython and Jupyter Notebook, you should no
longer need to use `%gui qt`, either: napari will enable it for you.

For more information, examples, and documentation, please visit our website:
https://napari.org

## Highlights

This release adds a new plugin type (i.e. a hook specification) for plugins to
provide sample data ({pr}`2483`). No more demos with `np.random`! 🎉 We've added a
built-in sample data plugin for this using the scikit-image data module.
Use it with `viewer.open_sample(plugin_name, sample_name)`, for example,
`viewer.open_sample('scikit-image', 'camera')`. Or you can use the File
menu at File -> Open Sample. For more on how to provide your own sample
datasets to napari, see [how to write a
plugin](https://github.com/napari/napari/blob/v0.4.8/docs/plugins/for_plugin_developers.rst) and the
[sample data
specification](https://github.com/napari/napari/blob/v0.4.8/napari/plugins/hook_specifications.py#L57).

The scale bar now has rudimentary support for physical units 📏 ({pr}`2617`). To use
it, set your scale numerically as before, then use `viewer.scale_bar.unit =
'um'`, for example.

We have also added a text overlay, which you can use to display arbitrary text
over the viewer ({pr}`2595`). You can use this to display time series time stamps,
for example. Access it at `viewer.text_overlay`.

Editing segmentations with napari is easier than ever now with varying number
of dimensions during painting/filling with labels ({pr}`2609`). Previously, if you
wanted to edit segmentations in a time series, you had to choose between
painting 2D planes, or painting in 4D. Now you can edit individual volumes
without affecting the others.

If you launch a long running process from napari, you can now display a progress
bar on the viewer ({pr}`2580`). You can find usage examples in the repo
[here](https://github.com/napari/napari/blob/fa342dc399b636330afdb1b4cb58f919832651fd/examples/progress_bar_minimal.py)
and
[here](https://github.com/napari/napari/blob/fa342dc399b636330afdb1b4cb58f919832651fd/examples/progress_bar_segmentation.py).


## New Features

- Add highlight widget to preferences dialog ({pr}`2435`)
- Add interface language selection to preferences ({pr}`2466`)
- Add Hookspec for providing sample data ({pr}`2483`)
- Add ability to run file as plugin ({pr}`2503`)
- Add `layer.source` attribute to track layer provenance ({pr}`2518`)
- Add button to drop into debugger in the traceback viewer. ({pr}`2534`)
- Add initial welcome screen on canvas ({pr}`2542`)
- Text overlay visual ({pr}`2595`)
- Add global progress wrapper and ProgressBar widget ({pr}`2580`)
- Add FOV to camera model and slider popup ({pr}`2636`). Right click on the 2D/3D
  display toggle button to get a perspective projection view in 3D.

## Improvements

- Add stretch to vertical dock widgets ({pr}`2154`)
- Use new selection model on existing `LayerList` ({pr}`2441`)
- Add bbox annotator example ({pr}`2446`)
- Save last working directory ({pr}`2467`)
- add name to dock widget titlebar ({pr}`2471`)
- Add Qt`ListModel` and `ListView` for `EventedList` ({pr}`2486`)
- New new qt layerlist ({pr}`2493`)
- Move plugin sorter ({pr}`2501`)
- Add support for passing `shape_type` through `data` attribute for `Shapes` layers ({pr}`2507`)
- Add ColorManager to Vectors ({pr}`2512`)
- Enhance translation methods ({pr}`2517`)
- Cleanup plugins.__init__, better test isolation ({pr}`2535`)
- Add typing to schema_version ({pr}`2536`)
- Add initial restart implementation ({pr}`2540`)
- Add data setter for `surface` layers ({pr}`2544`)
- Extract shortcut into their own object. ({pr}`2554`)
- Add example tying slider change to point properties change ({pr}`2582`)
- Range of label spinbox is more dtype-aware ({pr}`2597`)
- Add generic name to unnamed dockwidgets ({pr}`2604`)
- Add option to save state separate from geometry ({pr}`2606`)
- QtLargeIntSpinbox for label controls ({pr}`2608`)
- Support varying number of dimensions during labels painting ({pr}`2609`)
- Add units to the ScaleBar visual ({pr}`2617`)
- Return widgets created by `add_plugin_dock_widget` ({pr}`2635`)
- Add _QtMainWindow.current ({pr}`2638`)
- Relax dask test ({pr}`2641`)
- Add table header style ({pr}`2645`)
- QLargeIntSpinbox with QAbstractSpinbox and python model ({pr}`2648`)
- Add Labels layer `get_dtype` utility to account for multiscale layers ({pr}`2679`)
- Display file format options when saving layers ({pr}`2650`)
- Add events to plugin manager ({pr}`2663`)
- Add napari module to console namespace ({pr}`2687`)
- Change deprecation warnings to future warnings ({pr}`2707`)
- Add strict_qt and block_plugin_discovery parameters to make_napari_viewer ({pr}`2715`)

## Bug Fixes

- Ensure Preferences dialog can only be opened once ({pr}`2457`)
- Restore QtNDisplayButton ({pr}`2464`)
- Fix label properties setter (issue #2477) ({pr}`2478`)
- Fix labels data setter ({pr}`2496`)
- Fix localization for colormaps ({pr}`2498`)
- Small brackets fix for Perfmon ({pr}`2499`)
- Add try except on safe load ({pr}`2505`)
- Be cautious when checking a module's __package__ attribute ({pr}`2516`)
- Trigger label colormap generation on seed change to fix shuffle bug, addresses #2523 ({pr}`2524`)
- Modified quaternion2euler function to cap the arcsin's argument by +-1 ({pr}`2530`)
- Single line change to track recoloring function ({pr}`2532`)
- Handle Escape on Preferences dialog ({pr}`2537`)
- Fix close window handling for non-modals ({pr}`2538`)
- Fix trans to use new API ({pr}`2539`)
- Fix set_call_order with missing plugin ({pr}`2543`)
- Update conditional to use new selection property ({pr}`2557`)
- Fix visibility toggle (and other key events) in new qt layerlist ({pr}`2561`)
- Delay importing plugins during settings registration ({pr}`2575`)
- Don't create a dask cache if it doesn't exist ({pr}`2590`)
- Update model and actions on menu ({pr}`2602`)
- Fix z-index of notifications (hidden by welcome window) ({pr}`2611`)
- Make sure Delete is a special key mapping ({pr}`2613`)
- Disconnect some events on Canvas destruction ({pr}`2615`)
- Add missing QSpinBox import in Labels layer controls ({pr}`2619`)
- Use dtype.type when passing to downstream NumPy functions ({pr}`2632`)
- Fix notifications when something other than napari or ipython creates QApp ({pr}`2633`)
- Update missing translations for 0.4.8 ({pr}`2664`)
- Catch dockwidget layout modification error ({pr}`2671`)
- Fix warnings in thread_worker, relay messages to gui ({pr}`2688`)
- Add missing setters for shape attributes ({pr}`2696`)
- Add get_default_shape_type utility introspecting current shape type ({pr}`2701`)
- Fix handling of exceptions and notifications of threading threads ({pr}`2703`)
- Fix vertical_stretch injection and kwargs passing on DockWidget ({pr}`2705`)
- Fix tracks icons, and visibility icons ({pr}`2708`)
- Patch horizontalAdvance for older Qt versions ({pr}`2711`)
- Fix segfaults in test ({pr}`2716`) 
- Fix napari_provide_sample_data documentation typo ({pr}`2718`)
- Fix mpl colormaps ({pr}`2719`)
- Fix active layer keybindings ({pr}`2722`)
- Fix labels with large maximum value ({pr}`2723`)
- Fix progressbar and notifications segfaults in test ({pr}`2726`)

## API Changes

- By default, napari used to create a dask cache. This has caused unforeseen
  bugs, though, so it will no longer be done automatically. ({pr}`2590`) If you
  notice a drop in performance for your dask+napari use case, you can restore
  the previous behaviour with
  `napari.utils.resize_dask_cache(memory_fraction=0.1)`. You can of course also
  experiment with other values!
- The default `area` for `add_dock_widget` is now `right`, and no longer `bottom`.
- To avoid oddly spaced sparse widgets, {pr}`2154` adds vertical stretch to the
  bottom of all dock widgets added (via plugins or manually) with an `area`
  of `left` or `right`, *unless:*

    1) the widget, or any widget in its primary layout, has a vertical
       [`QSizePolicy`](https://doc.qt.io/qt-5/qsizepolicy.html#Policy-enum)
       of `Expanding`, `MinimumExpanding`, or `Ignored`

    1) `add_vertical_stretch=False` is provided to `add_dock_widget`,
       or in the widget options provided with plugin dock widgets.


## Deprecations

- As noted at the top of these notes, `napari.gui_qt()` is deprecated ({pr}`2533`).
  Call `napari.run()` instead when you want to display the napari UI.

## UI changes

- Toggle theme has been removed from the menubar. ({pr}`2462`) Instead, change the
  theme in the preferences panel.
- The number of 2D interpolation options available from the drop down menu has
  been reduced. ({pr}`2552`)
- The ipy interactive setting has been removed from the preferences panel.
  ({pr}`2605`) You can still turn it off from the API with
  `napari.utils.settings.get_settings().ipy_interactive = False`, but this is not
  recommended.
- The `n-dimensional` tick box in the Labels layer controls has been removed.
  ({pr}`2609`) Use "n edit dims" instead.

## Documentation

- Extend release notes: Add breaking API changes in 0.4.7 ({pr}`2494`)
- Add about team page ({pr}`2508`)
- Update translations guide ({pr}`2510`)
- Misc Doc fixes. ({pr}`2515`)
- Correct lenght for title underline. ({pr}`2541`)
- Minor reformatting. ({pr}`2555`)
- Automate doc copy ({pr}`2562`)
- Pin docs dependencies ({pr}`2568`)
- Example of using magicgui with thread_worker ({pr}`2577`)
- Fix typo in docs CI ({pr}`2588`)
- Only copy the autosummary templates ({pr}`2600`)
- Documentation typos ({pr}`2614`)
- Update event loop documentation for gui_qt deprecation ({pr}`2639`)
- Example using matplotlib figure ({pr}`2668`)

## Build Tools and Support

- Add a simple property-based test using Hypothesis ({pr}`2469`)
- Add check for strings missing translations ({pr}`2521`)
- Check if opengl file exists ({pr}`2630`)
- Remove test warnings again, minimize output, hide more async stuff ({pr}`2642`)
- Remove `raw_stylesheet` ({pr}`2643`)
- Add link to top level project roadmap page ({pr}`2652`)
- Replace pypa/pep517 with pypa/build ({pr}`2684`)
- Add provide sample data hook to docs ({pr}`2689`)

## Other Pull Requests

- Update PULL_REQUEST_TEMPLATE.md ({pr}`2497`)
- Non-dynamic base layer classes ({pr}`2624`)


## 19 authors added to this release (alphabetical)

- [alisterburt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [Chris Barnes](https://github.com/napari/napari/commits?author=clbarnes) - @clbarnes
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Fifourche](https://github.com/napari/napari/commits?author=Fifourche) - @Fifourche
- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Pam Wadhwa](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Robert Haase](https://github.com/napari/napari/commits?author=haesleinhuepf) - @haesleinhuepf
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Volker Hilsenstein](https://github.com/napari/napari/commits?author=VolkerH) - @VolkerH
- [Wilson Adhikari](https://github.com/napari/napari/commits?author=wadhikar) - @wadhikar
- [Zac Hatfield-Dodds](https://github.com/napari/napari/commits?author=Zac-HD) - @Zac-HD


## 20 reviewers added to this release (alphabetical)

- [alisterburt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [Chris Barnes](https://github.com/napari/napari/commits?author=clbarnes) - @clbarnes
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Emil Melnikov](https://github.com/napari/napari/commits?author=emilmelnikov) - @emilmelnikov
- [Fifourche](https://github.com/napari/napari/commits?author=Fifourche) - @Fifourche
- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Jeremy Asuncion](https://github.com/napari/napari/commits?author=codemonkey800) - @codemonkey800
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Justine Larsen](https://github.com/napari/napari/commits?author=justinelarsen) - @justinelarsen
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pam](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Robert Haase](https://github.com/napari/napari/commits?author=haesleinhuepf) - @haesleinhuepf
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
