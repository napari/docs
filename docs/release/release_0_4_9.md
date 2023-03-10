# napari 0.4.9

We're happy to announce the release of napari 0.4.9!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).


For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari


## Highlights
This release adds a couple nice new features like additional shading modes for our
surface layer ({pr}`2972`) and the ability to copy a screenshot directly to the clipboard ({pr}`2721`).
It also contains a variety of bug fixes and improvements.


## New Features
- Add tooltip for labels ({pr}`2658`)
- Added copy-to-clipboard functionality ({pr}`2721`)
- Add `make watch` command for hot reload ({pr}`2763`)
- Expose alternative shading modes for surfaces ({pr}`2792`)

## Improvements
- Global plugin setting ({pr}`2565`)
- Provide interface for progress bars in @thread_workers ({pr}`2655`)
- Delay all imports in `napari.__init__` behind module level `napari.__getattr__` ({pr}`2662`)
- Add `block` to viewer.show ({pr}`2669`)
- New type stubs PR, and simpler `napari.view_layers` module ({pr}`2675`)
- Extend the action manager to work with layer. ({pr}`2677`)
- Add `MultiScaleData` wrapper to give multiscale data a consistent API ({pr}`2683`)
- Revert "add `MultiScaleData` wrapper to give multiscale data a consistent API (#2683)" ({pr}`2807`)
- Add repr-html to nbscreenshot ({pr}`2740`)
- Set default highlight thickness to 2 ({pr}`2746`)
- Save shortcuts in settings ({pr}`2754`)
- Enable correct loading of settings from environment variables ({pr}`2759`)
- Add tooltips to widgets in preferences ({pr}`2762`)
- Improve colormap error message, when using display names or wrong colormap names ({pr}`2769`)
- Add parent to console and dockwidgets in a separate private attribute. ({pr}`2773`)
- Improve error message when legacy Qt installed from conda over pip ({pr}`2776`)
- Add octree and async to preferences ({pr}`2783`)
- Change remove to uninstall in plugin dialog ({pr}`2787`)
- Update typing and checks with mypy for settings module ({pr}`2795`)
- Do not write settings loaded from environment values ({pr}`2797`)
- Update settings descriptions ({pr}`2812`)
- Extend the action manager to support multiple shortcuts ({pr}`2830`)
- Adds notes about multiscale only being 2D to docs ({pr}`2833`)
- Set upper limit of Vectors spinboxes to infinity ({pr}`2842`)
- Plugin dock widgets menu ({pr}`2843`)
- Update to openGL max texture size ({pr}`2845`)
- Followup to #2485 to add opengl context ({pr}`2846`)
- Do not store default values in preference files ({pr}`2848`)


## Bug Fixes
- Fix Labels and Points properties set ({pr}`2657`)
- Fixing `add_dock_widget` compatibility with `magicgui v0.2` ({pr}`2734`)
- Shortcuts: Render properly shortcuts with minus and space. ({pr}`2735`)
- Fix runtime error when running doc tests on napari site ({pr}`2738`)
- Fix play button with dask/zarr ({pr}`2741`)
- Ignore opening 1D image layers in the viewer model. ({pr}`2743`)
- Fix custom layer subclasses (don't require layer icon) ({pr}`2758`)
- Add temporal fix for handling enums in qt_json_form ({pr}`2761`)
- Use slicing rather than np.take in add_image ({pr}`2780`)
- Fix paint cursor size for layer with negative scale ({pr}`2788`)
- track_id dtype change. from uint16 to uint32 ({pr}`2789`)
- Ensure aborted workers don't emit returned signal ({pr}`2796`)
- Connect axes visual to dims range change ({pr}`2802`)
- Add fix for large labels in new slices ({pr}`2804`)
- Fix zoom for non square image ({pr}`2805`)
- Implement lazy module importing for all public submodules ({pr}`2816`)
- Coerce surface vertex data to float32 ({pr}`2820`)
- Vendor shading filter from vispy ({pr}`2821`)
- Small doc fixes ({pr}`2822`)
- Fix key bindings display dialog ({pr}`2824`)
- Work around numpy's string casting deprecation ({pr}`2825`)
- Update translation strings ({pr}`2827`)
- Fix keypress skipping layers in layerlist ({pr}`2837`)
- Fix octree imports ({pr}`2838`)
- Remove opacity from plugin sorter widget ({pr}`2840`)
- Fix Labels.fill for tensorstore data ({pr}`2856`)
- Be more robust for non-existant keybindings in settings ({pr}`2861`)
- trans NameError bugfix ({pr}`2865`)


## Tasks
- Add imports linting ({pr}`2659`)
- Pre-commit update ({pr}`2728`)
- Remove linenos option from code-blocks and line references ({pr}`2739`)
- Remove qt from _qt import linter rule ({pr}`2774`)
- Add PR labeler and update templates ({pr}`2775`)
- Add pytest-order and move threading tests to the top of the suite ({pr}`2779`)
- Auto assign PR to author ({pr}`2794`)
- Typo in PR template ({pr}`2831`)


## 12 authors added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Alister Burt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [Andy Sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Pam](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03


## 10 reviewers added to this release (alphabetical)

- [Andy Sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pam](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03

