# napari 0.4.5

We're happy to announce the release of napari 0.4.5!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).


For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## Highlights
This release is our first release using Jupyter Book to build our documentation ({pr}`2187`)
which can be seen at https://napari.org/docs/dev/, or
https://napari.org/docs/0.4.5/ . We'll be continuing to reorganize the
napari.org website to create a more integrate feel with documentation and tutorials living
together. You can read more about our website reorganization in ({pr}`764`).

We've also added exprimental support for the ability to link attribute in layers which could
be useful for synchronizing attribute values across layers, for example to
set matching contrast limits for multiple channels ({pr}`2226`).


## New Features
- Add experimental link_layers ({pr}`2226`)


## Improvements
- Replace evented dataclasses with pydantic evented model on viewer ({pr}`2042`)
- Add pydantic evented model ({pr}`2127`)
- UI: Add keybindings to the Paint and Pick tooltips ({pr}`2184`)
- Add update in-place to evented model ({pr}`2197`)
- Allow reader_function to return empty layer list ({pr}`2206`)
- Handle closing the main window via the close button and handle_exit for this case. ({pr}`2215`)
- More main window cleanup ({pr}`2218`)
- Support equality checking for arrays (or other unusual types) in EventedModel. ({pr}`2232`)
- Make get_stylesheet public ({pr}`2241`)


## Bug Fixes
- Fix show/ hide plugin widgets ({pr}`2173`)
- Fix bug with modification of `AVAILABLE_COLORMAPS` when iterating over it  ({pr}`2193`)
- Prevent monitor information refering to one of first issues ({pr}`2214`)
- Fix close procedure ({pr}`2220`)
- Update `napari.run`, prevent double-blocking ({pr}`2225`)


## Documentation
- Convert docs to use Jupyter Book ({pr}`2187`)


## API Changes
- Removed github searching for plugin discovery, instead the `Framework :: napari` classifer should be used ({pr}`2228`)
- Removed evented_dataclass, instead the `EventedModel` should be used ({pr}`2236`)
- The deprecated ``Viewer.interactive`` parameter has been removed, instead you should use ``Viewer.camera.interactive`` ({pr}`2198`)
- The deprecated ``Viewer.palette`` attribute has been removed. To access the palette you can get it using ``napari.utils.theme.register_theme`` dictionary using the ``viewer.theme`` as the key ({pr}`2198`)
- The deprecated approach of annotating a magicgui function with a return type of ``napari.layers.Layer`` has been removed. To indicate that your function returns a layer data tuple, please use a return annotation of ``napari.types.LayerDataTuple`` or ``List[napari.types.LayerDataTuple]``({pr}`2198`)


## Deprecations
 - The `asdict` method has been renamed `dict` and is now deprecated on `Axes`, `Camera`, `Cursor`, `Dims, `GridCanvas`, `ScaleBar` ({pr}`2197`)


## Build Tools and Support
- Use napari-console package ({pr}`2118`)
- Fix typo in hookspecs docs ({pr}`2180`)
- DOC: autoreformat all the docstrings ({pr}`2186`)
- Refactor a qt dims test to not use the viewer ({pr}`2194`)
- Move `--show-viewer` option to testsupport, add test ({pr}`2208`)
- Include a line on adding screenshots/animations to PRs ({pr}`2219`)
- Skip perfmon test on windows pyside2 CI ({pr}`2223`)
- Generate api file for top-level napari package ({pr}`2237`)
- Better plugin errors surfacing in CLI with `--plugin-info` ({pr}`2244`)
- Add pluginmanager fixture ({pr}`2247`)
- Fix API Reference link in docs ({pr}`2248`)
- Add missing release notes ({pr}`2250`)
- Update napari_plugin_tester docstring ({pr}`2251`)
- Remove pluginmanager fixture in favor of devtools repo ({pr}`2252`)


## 9 authors added to this release (alphabetical)

- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Ian Hunt-Isaak](https://github.com/napari/napari/commits?author=ianhi) - @ianhi
- [Jonas Windhager](https://github.com/napari/napari/commits?author=jwindhager) - @jwindhager
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Ziyang Liu](https://github.com/napari/napari/commits?author=ziyangczi) - @ziyangczi


## 10 reviewers added to this release (alphabetical)

- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Jonas Windhager](https://github.com/napari/napari/commits?author=jwindhager) - @jwindhager
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Justine Larsen](https://github.com/napari/napari/commits?author=justinelarsen) - @justinelarsen
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Lia Prins](https://github.com/napari/napari/commits?author=liaprins-czi) - @liaprins-czi
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03

