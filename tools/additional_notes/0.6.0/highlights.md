### Summary

- Updated viewer handedness ✋
- Command palette 🎨
- Display polygons with holes ⛳️
- Transition to npe2 plugin engine by default 🔌
- Many other GUI improvements 🖥️

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

and in 0.6.0, thanks to [#7554](https://github.com/napari/napari/pull/7554):

![right shoe correctly rendered as a right shoe in napari](https://github.com/user-attachments/assets/e187f5e7-8e4a-4526-bae9-80a9bec6fea3)

Most users won't notice. But if you were among the users that noticed and you
implemented workarounds in your code (such as setting the z-scale to a negative
number), now is a good time to undo the workarounds for newer versions of
napari! If you run into any issues please get in touch [on GitHub
issues](https://github.com/napari/napari) or on our [Zulip chat room](https://napari.zulipchat.com)!

On the user space, we now offer several options to orient the axes any way you
like:

1. **Through the camera API:** the `Viewer.camera` instance gains two new
  attributes: `orientation`, and `orientation2d`, which is just the last two
  dimensions of `orientation`. You can set the direction that the *depth*,
  *vertical*, and *horizontal* axes point to, respectively in that order, as
  follows ([#7663](https://github.com/napari/napari/pull/7663)):

  ```python
  # 2D
  viewer.camera.orientation2d = ('up', 'right')
  # 3D
  viewer.camera.orientation = ('away', 'up', 'right')
  ```

  See an example of this in action in
  {ref}`sphx_glr_gallery_xarray-latlon-timeseries.py`.

2. **Through the UI:** By right clicking on the dimension toggle in the viewer,
  and setting the axis orientations using the drop-down menus
  ([#7686](https://github.com/napari/napari/pull/7686)), which in 3D will
  further indicate whether the resulting coordinate frame is [right-handed or
  left-handed](https://en.wikipedia.org/wiki/Right-hand_rule)
  ([#7770](https://github.com/napari/napari/pull/7770)):

  ![axis orientation dialog](https://github.com/user-attachments/assets/f73898ec-9156-4f73-ab7f-ee2a7cc17fe1)

3. **Through the startup settings:** If you want to use a specific axis
  orientation consistently, you can set the default orientation on startup by
  changing the relevant settings
  ([#7787](https://github.com/napari/napari/pull/7787):

  ![napari settings panel with axis orientation options highlighted](https://github.com/user-attachments/assets/f5032320-8b03-4ff7-9cb7-8b182ab232af)

  To restore the orientation from napari 0.5.6 and earlier, change the Depth
  axis setting to "away" (i.e. depth axis points away from you).

### Command palette 🎨

Tired of mousing around? Thanks to
[#5483](https://github.com/napari/napari/pull/5483), napari gains a command
palette! Press {kbd}`Ctrl/Command+Shift+P` and start typing the name of the
action you want to use, and press {kbd}`Enter` when you've highlighted it. It
even works with plugins! This is the culmination of many months of work porting
napari's actions to Talley Lambert's
[app-model](https://github.com/pyapp-kit/app-model). 🥳

![command palette example](https://github.com/user-attachments/assets/a412c3d1-8d29-43a2-87a4-391f2ccec57e)

There's still lots of work to be done here, but in the meantime, give it a try!
We on the team have found it very hard to go back to using napari without the
palette!

### Feature improvements to Shapes layers ⛳️

⚠️  *When using numba for triangulation, some shapes will still not be drawn
correctly, due to a bug in VisPy. We recommend installing `bermuda`, our new
fast triangulation package, for the best performance.* ⚠️

Finally, napari Shapes layers can now display polygons with holes in them,
which starts to open it up for use with mapping data, among other things!
([#7566](https://github.com/napari/napari/pull/7566),
[#6654](https://github.com/napari/napari/pull/6654)]) Implementing this feature
also eliminated a lot of bugs in our polygon drawing code, which could cause
crashes. If you've had issues with Shapes layers before, now might be a good
time to give them another try!

As part of this work, napari gained the ability to select between different
backends for triangulation, which means breaking up polygons into collections
of triangles, which is what GPUs are good at drawing.
([#7747](https://github.com/napari/napari/pull/7747)) To use the new backends,
install the relevant package (for example, `bermuda`,
`partsegcore-compiled-backend`, or `numba`), then go to Settings > Experimental
\> triangulation backend. (If you use `napari[all]`, you will have bermuda
installed and it will be used automatically, as the default option is "fastest
available".)

### Transition to npe2 plugin engine 🔌

npe2 was introduced over four years ago, with napari 0.4.12. npe2 has paved the
way for new plugin functionality, such as [adding menu
items](nap-6-contributable-menus) and the command palette. We are now beginning
the process of deprecating npe1 (napari-plugin-engine) plugins, which we need
to do to continue to improve npe2 functionality, for example in file readers,
which is currently very entangled with npe1 code.

To aid this migration, npe1 plugins will now be automatically converted to npe2
by default. This may break some features if the plugins relied on import-time
behavior. ([#7627](https://github.com/napari/napari/pull/7627))

During the 0.6.x series, if some plugin functionality is broken by the
automatic conversion, you can turn off this conversion in the plugin
preferences. However, the option to not convert npe1 plugins will be
removed in 0.7.0, and npe1 plugins will *only* work through automatic
conversion. We anticipate 0.7.0 will be released in the second half of 2025.

If you encounter conversion issues in a plugin you rely on, please contact the
plugin authors to encourage them to migrate their plugin to the npe2 system.

For more details on this change and how it affects plugins, see the [detailed
guide](adapted-plugin-guide). If you are a plugin author and your plugin is not
yet npe2-compatible, please see our [npe2 migration
guide](npe2-migration-guide), and, if you encounter any issues, get in touch in
our [Plugins Zulip chat
channel](https://napari.zulipchat.com/#narrow/channel/309872-plugins) or by
coming to one of our [community meetings](meeting-schedule).

### GUI improvements 🖥️

You'll notice the main napari GUI is subtly (or not so subtly) different in
0.6.0. Here are some of the improvements:

- Buttons now have an indicator to show whether they contain an extra menu when
  right-clicking. ([#7556](https://github.com/napari/napari/pull/7556))
- The button to change between 2D and 3D views much more clearly shows
  what it does. ([#7608](https://github.com/napari/napari/pull/7608))
- … And it has an extra menu with lots of options to control the camera!
  ([#7626](https://github.com/napari/napari/pull/7626))
- You can now add a bit of spacing between layers in grid mode (and control it
  in the grid mode right-click menu!)
  ([#7597](https://github.com/napari/napari/pull/7597))
- The colormap indicator in image layers is now a button, allowing you to
  create a linear colormap with any color!
  ([#7600](https://github.com/napari/napari/pull/7600))
- If you select multiple layers in the layer list, you can now see the status
  display of all the selected layers in the status bar
  ([#7673](https://github.com/napari/napari/pull/7673))
- If you switch from 2D to 3D view and back again, your 3D viewing angle will
  be preserved ([#7765](https://github.com/napari/napari/pull/7765))
- Notice some weird behavior? Our new log handler and viewer might help! Access
  it with Help > Show logs. ([#6900](https://github.com/napari/napari/pull/6900))

### Other stuff

For developers: napari now depends on Python 3.10+
([#7603](https://github.com/napari/napari/pull/7603) and Pydantic v2.2
([#7589](https://github.com/napari/napari/pull/7589)).

We've supported both pydantic 1 and 2 since 0.4.19, but we're now ready to take
advantage of performance and API improvements in Pydantic 2. If your library
depends on Pydantic 1.x, now would be a good time to upgrade, or it will not be
compatible with napari going forward.


If you were dreading 0.6.0 because you were relying on `_qt_viewer` features,
worry not: we have again postponed that deprecation while we add the required
APIs. 😅 ([#7730](https://github.com/napari/napari/pull/7730))

Also, if you've been wanting to contribute that doc fix but found the process
daunting, it's now easier than ever, because our default documentation preview
build is now much faster! You can propose changes from the GitHub UI and see
the rendered results in only two minutes!
([napari/docs#669](https://github.com/napari/docs/pull/669))
