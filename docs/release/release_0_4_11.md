# napari 0.4.11

We're happy to announce the release of napari 0.4.11!
napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based
rendering), and the scientific Python stack (numpy, scipy).


For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## Highlights

This release introduces ways to interact with data in 3D ({pr}`3037`). Features like
label picking ({pr}`3074`) and label painting/erasing ({pr}`3108`) now work in 3D, but
these are just the beginning! We're excited to see new ways of annotating 3D
data appear in napari! For more details, please see the documentation at
[https://napari.org/stable/guides/3D_interactivity.html](https://napari.org/stable/guides/3D_interactivity.html).
Many thanks to Alister Burt and Kevin Yamauchi for their foundational work
setting up the infrastructure for these features.

Our volume rendering functionality has been significantly improved and now
includes the ability to render arbitrary planes through volumes ({pr}`3023`) and add
clipping planes to restrict rendering to a region of interest ({pr}`3140`). For now,
these features are marked as `experimental` and the API around their use is
likely to change in future versions of napari. We've also greatly improved how
depth is handled across our visuals to fix some artifacts, see {pr}`3181` and
{pr}`3265`. Thanks to Alister Burt, Lorenzo Gaifas, and Kevin Yamauchi for this
work.

Last but not least, some common operations are now much more accessible from
the GUI thanks to a new context menu on the layer list ({pr}`2556` and {pr}`3028`) and
buttons for controlling image contrast limit scaling ({pr}`3022`). Thanks to Talley
Lambert for these features!

Read on below for the full list of new features, improvements, bug fixes, and
more! Thanks to our incredible user and contributor community.


## New Features

- Add context menu on layer list, introduce `QtActionContextMenu`. ({pr}`2556`)
- Add activity dialog and style progress bars ({pr}`2656`)
- Add playback options to settings ({pr}`2933`)
- Refactor settings manager to allow setting all preferences with env vars and context managers ({pr}`2932`)
- Add autoscale modes to image layer model, and buttons to GUI ({pr}`3022`)
- Arbitrary plane rendering prototype ({pr}`3023`)
- Add projections to layer context menu, allow grouping and nesting of menu items ({pr}`3028`)
- Add napari_experimental_provide_theme hook specification ({pr}`3034`)
- Add view ray and labels selection in 3D ({pr}`3037`)
- Add `add_<shape_type>` method for each shape type ({pr}`3076`)
- Grid mode popup ({pr}`3084`)
- Fix stubgen and package stubs in wheel/sdists ({pr}`3105`)
- Add 3D fill, "mill", and "print" on top of #3074 ({pr}`3108`)
- Add positive tail length to tracks layer ({pr}`3138`)
- Arbitrary clipping planes for volumes in the image layer ({pr}`3140`)
- Mask image from points layer ({pr}`3151`)
- Add .npy reader to builtin reader ({pr}`3271`)


## Improvements

- Add `assign_[plugin]_to_extension` methods on plugin_manager.  ({pr}`2695`)
- Use QDoubleRangeSlider from superqt package ({pr}`2752`)
- Use labeled sliders from superqt ({pr}`2753`)
- Shortcuts UI ({pr}`2864`)
- Convert TextManager to an EventedModel ({pr}`2885`)
- Make maximum brush size flexible ({pr}`2901`)
- Allow layer to register action on double clicks. ({pr}`2907`)
- Reduce numpy array traceback print ({pr}`2910`)
- Provide manual deepcopy implementation for translations strings. ({pr}`2913`)
- Make Points construction with properties consistent with setting properties ({pr}`2916`)
- Add search field to plugin dialog  ({pr}`2923`)
- Add initital support to install from conda/mamba ({pr}`2943`)
- Shape Mouse refactor ({pr}`2950`)
- Make handling properties more consistent across some layer types ({pr}`2957`)
- Labels paintbrush now takes anisotropy into account ({pr}`2962`)
- Remove mode guards for selection interactions in points ({pr}`2982`)
- Emit data event when moving, adding or removing shapes or points ({pr}`2992`)
- Add TypedMutableMapping and EventedDict ({pr}`2994`)
- Add isosurface rendering to Labels ({pr}`3006`)
- Remove mentions of _mode_history (2987) ({pr}`3008`)
- Change opacity slider to float slider ({pr}`3016`)
- Refactor the Point, Label and Shape Layer Mode logic. ({pr}`3050`)
- Make flash effect feel more instant ({pr}`3060`)
- Use enum values internally for settings. ({pr}`3063`)
- Update vendored volume visual from vispy ({pr}`3064`)
- Allow for multiple installs and update buttons to reflect state ({pr}`3067`)
- Unify plugin wording and installer dialog to display only package/plugins ({pr}`3071`)
- 3D label picking and label ID in status bar ({pr}`3074`)
- Store unmaximized size if napari closes maximized ({pr}`3075`)
- Change shapes default edge color to middle gray ({pr}`3113`)
- Change default text overlay color to mid grey ({pr}`3114`)
- Add 3D get_value to Shapes ({pr}`3117`)
- Replace custom signals to accept/reject ({pr}`3120`)
- Remove old utils/settings/constants file ({pr}`3122`)
- NAPARI_CATCH_ERRORS disable notification manager ({pr}`3126`)
- Save files after launch from ipython ({pr}`3130`)
- Don't try to read unknown formats in builtin reader plugin ({pr}`3145`)
- Make current viewer accessible from the napari module ({pr}`3149`)
- Rename `Layer.plane` to `Layer.slicing_plane` ({pr}`3150`)
- Update new label action to work with tensorstore arrays ({pr}`3153`)
- Always raise PluginErrors ({pr}`3157`)
- Establish better YAML encoding for settings (fix enum encoding issue). ({pr}`3163`)
- Move `get_color` call to after `all_vals` have been cleared ({pr}`3173`)
- Prevent highlight widget from emitting constant signals ({pr}`3175`)
- Refactor preferences dialog to take advantage of evented settings methods ({pr}`3178`)
- Set gl_FragDepth in volume visual isosurface rendering ({pr}`3181`)
- Use QElidingLabel from superqt ({pr}`3188`)
- Move dock widgets in menu ({pr}`3190`)
- Use `QLargeIntSpinBox` from superqt, remove internal one ({pr}`3191`)
- Catch and prune connections to stale Qt callbacks in events.py ({pr}`3193`)
- Add checkbox to handle global plugin enable/disabled state ({pr}`3194`)
- Print warning if error formatting in the console fails instead of ignoring errors. ({pr}`3201`)
- Ensure we save a copy of existing value for undo ({pr}`3203`)
- Pull main window menu creation off of Window ({pr}`3204`)
- Remove extra box on plugin dialog ({pr}`3235`)
- Add instant hover tooltips ({pr}`3242`)
- Clipping planes, generalized ({pr}`3252`)
- Improve behavior when holding "shift" while editing shapes ({pr}`3259`)
- Mesh depth ({pr}`3265`)
- Make notification text selectable ({pr}`3310`)


## Bug Fixes

- Fix notification manager threading test ({pr}`2892`)
- Pycharm blocking fix ({pr}`2905`)
- Fix windows 37 test ({pr}`2909`)
- Fix docstring, and type annotate. ({pr}`2912`)
- Don't raise exception when failing to save qt resources. ({pr}`2919`)
- Dix invalid yaml for docs workflow ({pr}`2920`)
- Fix use of `default_factory` in settings ({pr}`2930`)
- Close Qt progress bars when viewer is closed ({pr}`2931`)
- Degrade gracefully to default when colormap is not recognized ({pr}`2936`)
- Fix magicgui registration and circular imports ({pr}`2949`)
- Fix error in `Viewer.reset_view()` with vispy 0.7 ({pr}`2958`)
- Addressing case where argument to get_default_shape_type is empty list, addresses issue #2960 ({pr}`2961`)
- Fix nD anisotropic painting when scale is negative ({pr}`2966`)
- Ensure new height of expanded notification is larger than current height ({pr}`2981`)
- Gracefully handle properties with `object` dtype ({pr}`2986`)
- Fix scale decomp with composite ({pr}`2990`)
- Fix behavior of return/escape on preferences dialog to accept/cancel ({pr}`2998`)
- Fix EventedDict ({pr}`3011`)
- Use compression=('zlib', 1) for new tifffile ({pr}`3040`)
- Fix saving preferences ({pr}`3041`)
- Use non-deprecated colormap in viewer cmap test ({pr}`3043`)
- Fix Labels layer controls checkbox labels ({pr}`3046`)
- Fix Layer.affine assignment and broadcasting ({pr}`3056`)
- Fix problem with assigning affine with negative entries to  pyramids ({pr}`3088`)
- Fix stubgen and package stubs in wheel/sdists ({pr}`3105`)
- Fix opacity slider on shapes ({pr}`3109`)
- Fix empty points layer with color cycle ({pr}`3110`)
- Fix point deletion bug ({pr}`3119`)
- Fix for get_value() with mixed dims ({pr}`3121`)
- Fix settings reset breaking connections (creating a new instance of nested sub-models) ({pr}`3123`)
- Fix plane serialisation ({pr}`3143`)
- Bugfix in labels erasing ({pr}`3146`)
- Bug fix for undo history in 3D painting ({pr}`3154`)
- Don't clear blocked plugins when closing preferences dialog ({pr}`3164`)
- Revert `Points` `remove_selected` always overwriting `self._value` to `None` ({pr}`3165`)
- Fix window geometry loading bug, and make `ApplicationSettings` types more accurate ({pr}`3182`)
- Fix missing import in napari.__init__.pyi ({pr}`3183`)
- Fix incorrect window position storage ({pr}`3196`)
- Fix incorrect use of dims_order when 3D painting ({pr}`3202`)
- Fix plugin settings restore and schema_version validation error in preferences dialog ({pr}`3215`)
- Fix memory leak in napari ({pr}`3217`)
- Disable space bar on layer list ({pr}`3234`)
- Close napari window on Ctrl+C without geting window focus ({pr}`3239`)
- Skip labeled sliders for <5.14 ({pr}`3243`)
- Don't pass interpolation when creating a new projection layer ({pr}`3247`)
- Prevent greedy dask array calculation when creating an Image layer ({pr}`3248`)
- Fix plane normal inconsistency ({pr}`3264`)
- Remove accidental print statement ({pr}`3269`)
- Only change `labels` color mode in `color` setter if new `colors` are not default ({pr}`3275`)
- Fix updating of plugins ({pr}`3288`)
- Fix theme color setting on startup ({pr}`3293`)
- Fix incorrect theme registration ({pr}`3299`)
- Fix issubclass error in update_docs ({pr}`3305`)
- Fix some divide-by-zeros ({pr}`3320`)
- Fix connect_setattr to handle single arguments better ({pr}`3324`)
- Fix objectName being an empty string ({pr}`3326`)
- Fix napari.run aborting due to IPython being imported during script ({pr}`3328`)
- Fix _old_size attribute error in main window ({pr}`3329`)

## API Changes

- Remove brush shape ({pr}`3047`)
- Enforce layer.metadata as dict ({pr}`3020`)
- Use enum objects in EventedModel ({pr}`3112`)


## UI Changes

- Remove keybindings dialog from help menu ({pr}`3048`)
- Remove plugin sorter from plugin install dialog ({pr}`3069`)
- Update Labels layer keybindings to be more ergonomic ({pr}`3072`)


## Build Tools, Tests, Documentation, and other Tasks

- Add imagecodecs to the bundle to open additional tiffs ({pr}`2895`)
- Make ordering of releases manual ({pr}`2921`)
- Add alister burt to team page ({pr}`2937`)
- Use briefcase 0.3.1 on all platforms ({pr}`2980`)
- Move to Python 3.9 in the bundled application ({pr}`2991`)
- Speedup one of the slowest test. ({pr}`2997`)
- Update plugin guide with references and instructions for napari-hub ({pr}`3055`)
- Skip progress indicator test when viewer is not shown ({pr}`3065`)
- Add missing libraries in docker file and entrypoint ({pr}`3081`)
- Update documentation regarding the hub ({pr}`3091`)
- Block showing dialog in nongui test ({pr}`3127`)
- Update about page ({pr}`3134`)
- Adding new design issues template ({pr}`3142`)
- Fix emoji for design template ({pr}`3161`)
- Update design_related.md ({pr}`3162`)
- Try to fix CI, change perfmon test strategy ({pr}`3167`)
- Fix comprehensive tests ({pr}`3168`)
- Fix `make_docs` action ({pr}`3169`)
- Remove convert_app ({pr}`3171`)
- Update team.md ({pr}`3176`)
- Misc Doc format fixing ({pr}`3179`)
- Add public meeting calendar to the docs ({pr}`3192`)
- Don't start gui qt event loop when building docs ({pr}`3207`)
- Add note detailing current octree support ({pr}`3208`)
- Add napari_write_tracks to hook spec reference ({pr}`3209`)
- Add 3d interactivity docs ({pr}`3210`)
- Fix docs build again ({pr}`3211`)
- Fix CI typing tests ({pr}`3212`)
- Fix typo, add proper note markdown ({pr}`3216`)
- Pooch bugfix ({pr}`3218`)
- Update team.md ({pr}`3237`)
- Add binder to repository and badge on README ({pr}`3244`)
- Add extras_require for bundle deps ({pr}`3255`)
- Pin support pkg revision macos ({pr}`3266`)
- Exclude vispy 0.8.0 ({pr}`3276`)
- Revert sys.exit(0) debugging ({pr}`3277`)
- Bundle: export ARCH on Linux ({pr}`3280`)
- DOC: misc edits/fixes in the developer guide ({pr}`3296`)
- Update napari console dependency ({pr}`3297`)
- Bundle: use python 3.8 on Windows ({pr}`3300`)
- Bundle: add arch suffix to zip name ({pr}`3302`)
- Fix headless test failure ({pr}`3311`)
- Pin furo version ({pr}`3315`)
- Update the affine parameter description in several classes ({pr}`3319`)


## 21 authors added to this release (alphabetical)

- [Abigail McGovern](https://github.com/napari/napari/commits?author=AbigailMcGovern) - @AbigailMcGovern
- [Alister Burt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [Andy Sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Jaime Rodríguez-Guerra](https://github.com/napari/napari/commits?author=jaimergp) - @jaimergp
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Lia Prins](https://github.com/napari/napari/commits?author=liaprins-czi) - @liaprins-czi
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [Marlene Elisa Da Vitoria Lobo](https://github.com/napari/napari/commits?author=marlene09) - @marlene09
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nathan Clack](https://github.com/napari/napari/commits?author=nclack) - @nclack
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pam](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Thanushi Peiris](https://github.com/napari/napari/commits?author=thanushipeiris) - @thanushipeiris
- [Volker Hilsenstein](https://github.com/napari/napari/commits?author=VolkerH) - @VolkerH
- [Ziyang Liu](https://github.com/napari/napari/commits?author=ziyangczi) - @ziyangczi


## 19 reviewers added to this release (alphabetical)

- [Alister Burt](https://github.com/napari/napari/commits?author=alisterburt) - @alisterburt
- [Andy Sweet](https://github.com/napari/napari/commits?author=andy-sweet) - @andy-sweet
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Gonzalo Peña-Castellanos](https://github.com/napari/napari/commits?author=goanpeca) - @goanpeca
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Lia Prins](https://github.com/napari/napari/commits?author=liaprins-czi) - @liaprins-czi
- [Lorenzo Gaifas](https://github.com/napari/napari/commits?author=brisvag) - @brisvag
- [Lucy Obus](https://github.com/napari/napari/commits?author=LCObus) - @LCObus
- [Lukasz Migas](https://github.com/napari/napari/commits?author=lukasz-migas) - @lukasz-migas
- [Matthias Bussonnier](https://github.com/napari/napari/commits?author=Carreau) - @Carreau
- [Nathan Clack](https://github.com/napari/napari/commits?author=nclack) - @nclack
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Pam](https://github.com/napari/napari/commits?author=ppwadhwa) - @ppwadhwa
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Ziyang Liu](https://github.com/napari/napari/commits?author=ziyangczi) - @ziyangczi

