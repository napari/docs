# napari 0.3.0

We're happy to announce the release of napari 0.3.0!

napari is a fast, interactive, multi-dimensional image viewer for Python.
It's designed for browsing, annotating, and analyzing large multi-dimensional
images. It's built on top of Qt (for the GUI), vispy (for performant
GPU-based rendering), and the scientific Python stack (numpy, scipy).

This is the first "major" release since 0.2.0 and is the culmination of 6
months of work by our developer community. We have made a small number of
breaking changes to the API, and added several new capabilities to napari, so
we encourage you to read on for more details.

For more information, examples, and documentation, please visit our website:
https://napari.org

## Highlights

### Community and governance

After the 0.2.5 release, which was our first publicly-announced release, we
worked to rapidly turn napari into a mature library in the scientific Python
ecosystem. We added a [code of
conduct](https://napari.org/stable/community/code_of_conduct.html), a [mission
and values
document](https://napari.org/stable/community/mission_and_values.html), and
adopted a [community governance
model](https://napari.org/stable/community/governance.html) (based on
scikit-image's, and since adopted with modifications by zarr). These are
accessible from our [developer resources
page](https://napari.org/developers/index.html), together with a [public
roadmap](https://napari.org/roadmaps/0_3.html) explaining where
the core team will devote effort in the coming months.

We are still humbled by the enthusiasm of the community response to napari and
we hope that the above documents will continue to encourage potential users to
join our community. We welcome contributions of all kinds and encourage you to
get in touch with us if you don't see your most wanted feature in our roadmap,
or as an issue in our [issue tracker](https://github.com/napari/napari/issues).

### Getting in touch

We joined the [image.sc forum](https://forum.image.sc) and actively monitor it
([under the "napari" tag](https://forum.image.sc/tag/napari)) to help users
with any issues they might have using napari and have discussions about
exciting ways to use napari. If you're new to napari and getting started this
is the first place you should go for help.

If you've found a napari bug or have a specific feature request, please let us
know in our [GitHub issues](https://github.com/napari/napari/issues).

### IO plugins

Contributors can now easily extend napari to open and save in a variety of file
formats, both local and remote, through our plugin architecture. The same file
formats as before are available to read (TIFF, most image file formats
supported by imageio, and zarr).  However, we can now *write* to all these
formats, and read and write point and shape annotations in .csv format.
Additionally, we have made it possible for anyone to create packages for napari
to read and write in any other formats through plugins. You can read about our
plugin architecture [here](https://napari.org/plugins/index.html).

Want to drag and drop your favorite file format into napari and have it load
automatically? See [this
guide](https://github.com/napari/napari/blob/v0.3.0/docs/source/plugins/for_plugin_developers.rst) to
understand how to write your own plugin, see Jackson Brown's
[napari-aicsimageio](https://github.com/AllenCellModeling/napari-aicsimageio)
for an exemplar plugin, and get started with Talley's [cookiecutter napari
plugin](https://github.com/napari/cookiecutter-napari-plugin)!

Many thanks to Talley Lambert for driving this effort!

### Dockable widgets and magicgui

Another brainchild of Talley is our dockable widget architecture, which allows
you to pop out the napari UI elements from the main window, enabling, for
example, those on multi-monitor setups to have the toolbars on one monitor and
the main window in full-screen on another.

Even better, we have released a side package called
[magicgui](https://github.com/napari/magicgui) to allow you to create your own
dockable widgets with which to interact with napari without writing GUI code.
We are still working on standard models of interaction here (see our
[roadmap](https://napari.org/roadmaps/0_3.html)), but you should
be able to get started creating useful user interfaces right now. [This
image.sc
post](https://forum.image.sc/t/integration-of-napari-module-subclass-plugin/36018/2)
by Talley provides a good overview of how to create interaction with napari
right now, and [this GitHub
answer](https://github.com/napari/napari/issues/1165#issuecomment-618013894)
explains how to embed a matplotlib plot within napari.

### Multiscale image handling

napari is now much better at handling large datasets. Viewing a large dataset
will no longer trigger automatic — but very slow, and often unnecessary —
generation of an image pyramid. Instead, we direct users to our [tutorial on
how to generate your own
pyramid](https://scikit-image.org/docs/dev/auto_examples/transform/plot_pyramid.html)
from `scikit-image`. For large arrays, users may want to look at the
[`dask.array.coarsen`
documentation](https://docs.dask.org/en/stable/generated/dask.array.coarsen.html)

If you submit an image pyramid, napari will automatically detect it as such. To
turn off automatic detection, you can now pass the `multiscale=True/False`
parameter to `add_image`. This replaces the `is_pyramid` parameter which has
now been removed. In the future, we aim to add multiscale capabilities to all
our layers.

We have also fixed the bug where too small a tile was shown to fill the entire
canvas.

### Points with properties

Points are no longer generic coordinates floating in space! Each point can have
its own personality and character :-). Specifically, each point can have an
arbitrary number of properties, and attributes such as size, face color, and
edge color can be determined by those properties. This makes it easier to
annotate multiple types of points in an image, such as different cell types. To
assign properties to points you can pass a dictionary as the `properties`
parameter to `add_points`.

### API changes and improvements

We are taking the opportunity of this major release to update a few APIs. We
hope that the number of users impacted by these changes will be small. In each
case, we provide an equivalent API for the same functionality.

- `viewer.add_path` has been renamed `viewer.open` and gained the ability to
  read to any layer type.
- `add_image(path=...)` and `add_labels(path=...)` have been removed. Users
  should use `viewer.open(...)` instead with the `layer_type` parameter to
  force the added data to be a particular layer type, e.g.
  `layer_type='image'` or `layer_type='labels'`.
- Image pyramids are no longer automatically generated when a dataset is large.
  This should not affect API compatibility but might affect performance. For
  most users, this should result in faster startup for large images.
- `add_image(..., is_pyramid=False)` is now `add_image(..., multiscale=False)`.
  This will allow us to use a consistent keyword argument when we add
  multiscale support for other layer types.
- `layer.to_svg()` has been removed. This functionality is now implemented with
  `viewer.save('path/to/layer.svg', layer, plugin='svg')` through our plugin
  architecture.

### And one more thing...

Thanks to the ever-creative Kira Evans, napari will now populate layer names
based on the name of the variables being visualized:

```python
import napari
from skimage import data

camera = data.camera()
with napari.gui_qt():
    viewer = napari.view_image(camera)
    print(viewer.layers[0].name)  # prints "camera"!
```

In Python 3.8, the name will even be visible if you are using the assignment
expression a.k.a. the walrus operator:

```python
import napari
from skimage import data

with napari.gui_qt():
    viewer = napari.view_image(camera := data.camera())
    print(viewer.layers[0].name)  # prints "camera"!
```

## New Features
- Hook up reader plugins ({pr}`937`)
- Support for magicgui ({pr}`981`)
- Writer plugins ({pr}`1104`)


## Improvements
- Generalize keybindings ({pr}`791`)
- Points view data refactor ({pr}`951`)
- Add magic name guessing ({pr}`1008`)
- Refactor labels layer mouse bindings ({pr}`1010`)
- Reduce code duplication for `_on_scale_change` & `_on_translate_change` ({pr}`1015`)
- Style refactor ({pr}`1017`)
- Add ScaleTranslate transform ({pr}`1018`)
- Add docstrings for all the Qt classees ({pr}`1022`)
- Sorting and disabling of hook implementations ({pr}`1023`)
- Plugin exception storage and developer notification GUI ({pr}`1024`)
- Refactor points layer mouse bindings ({pr}`1033`)
- Add chains of transforms ({pr}`1042`)
- Shapes layer internal renaming ({pr}`1046`)
- Internal utils / keybindings / layer accessories renaming ({pr}`1047`)
- Shapes layer mouse bindings refactor ({pr}`1051`)
- Make console loading lazy ({pr}`1055`)
- Remove scikit-image dependency ({pr}`1061`)
- All args to add_image() accept sequences when channel_axis != None ({pr}`1092`)
- Added documentation for label painting ({pr}`1094`)
- Finish layer mouse bindings refactor ({pr}`1121`)
- Enable volume rendering interpolation control ({pr}`1127`)
- Change image icon ({pr}`1128`)
- Refactor Vectors colors ({pr}`1130`)
- Reduce code duplication in Points ({pr}`1140`)
- Add keybinding to toggle selected layer visibility ({pr}`1147`)
- Only block in gui_qt or quit QApp when necessary ({pr}`1148`)
- Plugin `_HookCaller` and registration updates ({pr}`1153`)
- Reduce code duplication in points tests ({pr}`1154`)
- Color cycles properties return array ({pr}`1163`)
- Allow last added point to be deleted with backspace keybinding ({pr}`1164`)
- Extract plugin code to napari-plugin-engine ({pr}`1169`)
- Turn caching on and fusion off when adding a dask array ({pr}`1173`)
- Save all/selected layers Qt dialogs ({pr}`1185`)
- Magic layer name guessing is always on ({pr}`1186`)
- Warn when nothing saved ({pr}`1188`)
- Add builtin shapes writer and reader ({pr}`1193`)
- Bump svg-dep, add builtin write_labels ({pr}`1200`)
- Change screenshot hotkey and open menubar names ({pr}`1201`)

## Bug Fixes
- Refactor cleanup, prevent leaked widgets, add viewer.close method ({pr}`1014`)
- Allow StringEnum to accept instances of self as argument ({pr}`1027`)
- Close the canvas used to retrieve maximum texture size. ({pr}`1028`)
- Fix points color cycle refresh ({pr}`1034`)
- Fix styles for Qt < 5.12.  Fix styles in manifest for pip install ({pr}`1037`)
- Fix label styles in contrast limit popup  ({pr}`1039`)
- Fix pyramid clipping ({pr}`1053`)
- Fix resources/build_icons:build_resources_qrc ({pr}`1060`)
- Add error raise in `Viewer._add_layer_from_data` ({pr}`1063`)
- Fix empty points with properties ({pr}`1069`)
- Fix image format ({pr}`1076`)
- Lazy console fixes ({pr}`1081`)
- Fix function and signature to match with code ({pr}`1083`)
- Fix LayerList and ListModel type checking ({pr}`1088`)
- Fix changing translate order when changing data dims ({pr}`1102`)
- Fix add_points_with_properties example ({pr}`1126`)
- Use mode='constant' in numpy.pad usage ({pr}`1150`)
- Fix canvas none after layer deletion ({pr}`1158`)
- Prevent crash when viewing 3D pyramids ({pr}`1179`)
- Add ensure_colormap utility function to standardize colormap getting/setting ({pr}`1180`)
- Fix small plugin error report bug ({pr}`1181`)
- Fix multichannel implicit multiscale ({pr}`1192`)
- One more plugin error reporting fix ({pr}`1194`)
- Normalize paths handed to reader plugins ({pr}`1195`)
- Fix singleton dims display after toggle ({pr}`1196`)
- Fix resize axis labels on show ({pr}`1197`)
- Only assert that dask config returns to original value in test ({pr}`1202`)

## Breaking API Changes
- Allow add_path() to accept any layer-specific kwarg and rename to open() ({pr}`1111`)
- Remove path arg from add_image and add_labels ({pr}`1149`)
- Drop pyramid autogeneration ({pr}`1159`)
- Replace pyramid with multiscale ({pr}`1170`)
- Add napari-svg plugin support ({pr}`1171`)


## Support
- Publish developer resources ({pr}`967`)
- Fix recursive include in manifest.in ({pr}`1003`)
- Fix pip install with older versions of pip ({pr}`1011`)
- Plugin docs (for plugin developers) ({pr}`1030`)
- Add github links to contributor list ({pr}`1043`)
- Check if PyQt5 is installed and then not install PySide2 ({pr}`1059`)
- Use pip instead of invoking setup.py ({pr}`1072`)
- pyenv with PyQt5 in other environment workaround ({pr}`1080`)
- Roadmap for 0.3 releases ({pr}`1095`)
- Add installed plugins to sys_info() ({pr}`1096`)
- Avoid pillow 7.1.0 ({pr}`1099`)
- Pin pillow at <= 7.0.0 ({pr}`1108`)
- Fix a number of sphinxdocs errors ({pr}`1113`)
- Fix miniconda download in CI ({pr}`1119`)
- Convert old release notes to md ({pr}`1135`)
- Automate release process ({pr}`1138`)
- Open up Pillow again after 7.1.* ({pr}`1146`)
- Fix black consistency ({pr}`1152`)
- Fix sphinx ({pr}`1155`)
- Change release notes source file to use .md ext ({pr}`1156`)
- Rename requirements test ({pr}`1160`)
- Update Pillow dependency pin ({pr}`1172`)
- Update napari-svg to 0.1.1 ({pr}`1182`)
- Update manifest.in for plugin code removal ({pr}`1187`)
- Fix pip-missing-reqs step ({pr}`1189`)


## 13 authors added to this release (alphabetical)

- [Bhavya Chopra](https://github.com/napari/napari/commits?author=BhavyaC16) - @BhavyaC16
- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Hector](https://github.com/napari/napari/commits?author=hectormz) - @hectormz
- [Hugo van Kemenade](https://github.com/napari/napari/commits?author=hugovk) - @hugovk
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Luigi Petrucco](https://github.com/napari/napari/commits?author=vigji) - @vigji
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Peter Boone](https://github.com/napari/napari/commits?author=boonepeter) - @boonepeter
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Tony Tung](https://github.com/napari/napari/commits?author=ttung) - @ttung


## 13 reviewers added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Genevieve Buckley](https://github.com/napari/napari/commits?author=GenevieveBuckley) - @GenevieveBuckley
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Hector](https://github.com/napari/napari/commits?author=hectormz) - @hectormz
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Justine Larsen](https://github.com/napari/napari/commits?author=justinelarsen) - @justinelarsen
- [Kevin Yamauchi](https://github.com/napari/napari/commits?author=kevinyamauchi) - @kevinyamauchi
- [Kira Evans](https://github.com/napari/napari/commits?author=kne42) - @kne42
- [Luigi Petrucco](https://github.com/napari/napari/commits?author=vigji) - @vigji
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Shannon Axelrod](https://github.com/napari/napari/commits?author=shanaxel42) - @shanaxel42
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
- [Tony Tung](https://github.com/napari/napari/commits?author=ttung) - @ttung
