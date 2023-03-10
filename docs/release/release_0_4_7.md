# napari 0.4.7

We're happy to announce the release of napari 0.4.7!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).


For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## Highlights

After nearly a year of planning, thanks to help from the fine folks at
[Quansight](https://labs.quansight.org/), napari now has a preferences dialog!
({pr}`2211`). It's a little sparse at the moment but we look forward to meeting all
your customization needs!

Thanks to Matthias Bussonnier and Talley Lambert, we've also improved our
notification handling and can now show tracebacks in our error notifcations in
the GUI!

You can now use PyData/Sparse arrays as labels layers, thanks to work by Draga
Doncila Pop (across both napari and sparse itself) and Juan Nunez-Iglesias.
This is useful when painting labels across large volumes/time series. As a
side-benefit of this work, undo when painting labels now works across the full
volume rather than only in the currently-visible plane. ({pr}`2339`, {pr}`2396`,
pydata/sparse#435 and related PRs)

We've also continued to make improvements to our experimental octree support,
which now supports single scale tiled loading ({pr}`2372`, {pr}`2391`). It is still
2D-only but continues to improve!

Last but not least, this is the first release since we launched our new website
at https://napari.org, powered by Jupyter Book! Check it out! Huge thanks to
Kira Evans, Talley Lambert, Lia Prins, Genevieve Buckley, and others who
contributed (and continue to contribute) to our efforts to improve our
documentation.

See below for the full list of changes.

## New Features
- Notification Manager  ({pr}`2205`)
- Add preference dialog ({pr}`2211`)
- Make napari strings localizable ({pr}`2429`)

## Documentation
- Add profiling documentation ({pr}`1998`)
- Add release note about pydantic viewermodel ({pr}`2334`)
- Broken link fixed for Handling Code of Conduct Reports ({pr}`2342`)
- Update nbscreenshot docstring ({pr}`2395`)
- Clarify benchmark docs ({pr}`2431`)
- Make structural doc changes to better align with sitemap ({pr}`2404`)

## Improvements
- ColorManager take 2 (w/ pydantic) ({pr}`2204`)
- Add basic selection model ({pr}`2293`)
- Tooltips2 ({pr}`2310`)
- Add a font size preview slider widget ({pr}`2318`)
- Read multiple page from pypi ({pr}`2335`)
- Use fancy indexing rather than full slices for label editing undo ({pr}`2339`)
- Consolidate polygon base object ({pr}`2344`)
- Use not mutable fields on Viewer where appropriate ({pr}`2346`)
- Generic Button to toggle state. ({pr}`2359`)
- Make `add_plugin_dock_widget` public, add CLI option ({pr}`2360`)
- Add spiral indexing to bring in tiles at center of FOV first ({pr}`2363`)
- Improve octree coverage process ({pr}`2366`)
- Single scale tiled rendering ({pr}`2372`)
- Add notification settings, add back console notifications ({pr}`2377`)
- ipython embed example ({pr}`2378`)
- Add contrast limits estimate for large plane ({pr}`2381`)
- Discover dock widgets during get info ({pr}`2385`)
- Add example of 2D, single-scale tiled rendering ({pr}`2391`)
- Preference screen size ({pr}`2399`)
- Add support for octree labels ({pr}`2403`)
- Auto-enable gui qt when in IPython ({pr}`2406`)
- Allow no vertex values to be passed to surface layer ({pr}`2408`)
- Add base shape outline for single scale tiled ({pr}`2414`)
- Change raw_to_displayed to only compute colours for all labels when required ({pr}`2415`)
- Highlight widget ({pr}`2424`)
- Remove brush shape from label UI ({pr}`2426`)
- Remember Preferences dialog size. ({pr}`2434`)
- `Selectable` mixin and `SelectableEventedList` ({pr}`2439`)
- Unify evented/nestedEvented list APIs ({pr}`2440`)
- Pretty-settings ({pr}`2448`)
- Add a button to Qt Error Notification to show tracebacks ({pr}`2452`)
- Update preferences dialog style to match designs ({pr}`2456`)

## Bug Fixes
- Fix initialization of an empty Points layer ({pr}`2341`)
- Fix octree clim ({pr}`2349`)
- Fix json encoder inheritance on nested submodels for pydantic>=1.8.0 ({pr}`2357`)
- Fix shortcut to toggle grid. ({pr}`2358`)
- Fix rgb for octree ({pr}`2362`)
- Fix deleting points data in viewer ({pr}`2383`)
- Close floating docks on close event ({pr}`2397`)
- Handle None settings on load ({pr}`2398`)
- Fix preference cancel ({pr}`2410`)
- Fix shapes data setter ({pr}`2411`)
- Fix nd text on shapes layer ({pr}`2412`)
- Fix overly sensitive Points layer dragging ({pr}`2413`)
- Fix points delete ({pr}`2419`)
- Fix empty layer text ({pr}`2420`)
- Fix env-dependent test errors, remove warnings ({pr}`2421`)
- Fix Labels `save_history` benchmark ({pr}`2430`)
- Fix packaging ({pr}`2436`)
- Fix numpy warnings ({pr}`2438`)
- Fix some translation formatting ({pr}`2453`)
- Remove extra remove window action from window menu and use file menu
  instead ({pr}`2454`)
- Fix translation II ({pr}`2455`)
- Fix for constant warning when using label brush ({pr}`2460`)
- Restore QtNDisplayButton ({pr}`2464`)

## API Changes

- Using `layer.get_status()` without an argument was deprecated in version
  0.4.4 and is removed in this version. Instead, use
  `layer.get_status(viewer.cursor.position, world=True)` ({pr}`2443`).
- `layer.status` was deprecated in version 0.4.4 and is removed in this
  version. Instead, use `layer.get_status(viewer.cursor.position, world=True)`
  ({pr}`2443`).
- Label-layers must be of integer type, float `Labels` layers are no longer allowed (see {pr}`2491`)

## Deprecations

We are moving to a model in which layers don't know about the cursor or current
view, resulting in the following two deprecations:

- `layer.displayed_coordinates` is deprecated ({pr}`2327`). Instead, use
  `[layer.coordinates[d] for d in viewer.dims.displayed]`
- `layer.position` and `layer.coordinates` are deprecated ({pr}`2443`). Instead, use
  `viewer.cursor.position` for the position in world coordinates, and
  `layer.world_to_data(viewer.cursor.position)` for the position in data
  coordinates.

We have also deprecated the `napari.qt.QtNDisplayButton`. Instead a more general
`napari.qt.QtStateButton` is provided.

## Build Tools and Support
- Add environment flag for sparse library ({pr}`2396`)
- re-add plausible ({pr}`2433`)


## 14 authors added to this release (alphabetical)

- [alisterburt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [DenisSch](https://github.com/napari/napari/commits?author=DenisSch) - @DenisSch
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pam](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [ziyangczi](https://github.com/napari/napari/commits?author=ziyangczi) - @ziyangczi


## 12 reviewers added to this release (alphabetical)

- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pam](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Thomas A Caswell](https://github.com/napari/napari/commits?author=tacaswell) - @tacaswell
- [ziyangczi](https://github.com/napari/napari/commits?author=ziyangczi) - @ziyangczi

