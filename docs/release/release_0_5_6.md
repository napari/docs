# napari 0.5.6

*Thu, Jan 16 2024*

🚧 *These notes are under construction while in pre-release* 🚧

We’re happy to announce the release of napari 0.5.6! The right-handed release! This release features a *big* change so read on to see how it might affect you!

napari is a fast, interactive, multi-dimensional image viewer for Python. It’s designed for exploring, annotating, and analyzing multi-dimensional images. It’s built on Qt (for the GUI), VisPy (for performant GPU-based rendering), and the scientific Python stack (NumPy, SciPy, and friends).

For more information, examples, and documentation, please visit our website: https://napari.org/

## Highlights

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

and in 0.5.6+, thanks to [#7488](https://github.com/napari/napari/pull/7488):

![right shoe correctly rendered as a right shoe in napari](https://github.com/user-attachments/assets/e187f5e7-8e4a-4526-bae9-80a9bec6fea3)

Most users won't notice. But if you were among the users that noticed and you
implemented workarounds in your code (such as setting the z-scale to a negative
number), now is a good time to undo the workarounds for newer versions of
napari! If you run into any issues please get in touch [on GitHub
issues](https://github.com/napari/napari) or on our [Zulip chat room](https://napari.zulipchat.com)!

### Faster shapes 🚀

For its whole history, napari has been a pure Python package. As we go deeper
into its performance bottlenecks, though, we're finding that we need some
compiled code. This is a big change to the napari installation story, though,
so we are rolling it out slowly. But if you've been waiting forever to load
your shapes data, this release has some enhancements for you (>2x speedup)!
([#7346](https://github.com/napari/napari/pull/7346))

To use this speedup, you'll need to:
- install napari core developer Grzegorz Bokota's collection of performant
  algorithms,
  [PartSegCore-compiled-backend](https://pypi.org/project/PartSegCore-compiled-backend/).
  (you can install it automatically by pip installing `"napari[optional]"`.)
- *and*, in the napari advanced settings, tick the "Use C++ code to speed up
  creation and updates of Shapes layers" box.

Please give it a try and let us know if you encounter any issues! This is the
beginning of a new era of performance improvements in napari, to help it live
up to its promise of a *fast* viewer for n-dimensional data in Python!

### Other improvements

Often, the important information in a layer name is at the *end* of the name
rather than the beginning. We've improved the eliding (…) of long names by
placing the ellipsis in the *middle* of the name rather than the end
([#7461](https://github.com/napari/napari/pull/7461)).

The default value of "flash" has been changed to `False` in
`viewer.screenshot`, so that taking many screenshots in a script will not
result in rapid flickering
([#7476](https://github.com/napari/napari/pull/7476)). This is part of a
broader accessibility initiative by recent contributor [Tim
Monko](https://github.com/TimMonko) to improve napari for light-sensitive
users ([#7433](https://github.com/napari/napari/issues/7433), and we are so
grateful! 🙏

## New Features

- Elide layer name in the middle instead of the end ([#7461](https://github.com/napari/napari/pull/7461))

## Improvements

- Perform triangulation using compiled backend ([#7346](https://github.com/napari/napari/pull/7346))
- stop/start notification timer on window focus change ([#7392](https://github.com/napari/napari/pull/7392))
- Extend reading with plugins to allow Layer objects ([#7443](https://github.com/napari/napari/pull/7443))
- Change default flash behavior for `viewer` screenshot-like methods ([#7476](https://github.com/napari/napari/pull/7476))

## Performance

- Perform triangulation using compiled backend ([#7346](https://github.com/napari/napari/pull/7346))

## Bug Fixes

- [Bugfix] Don't exit Preferences widget when using Return/Enter to confirm a shortcut ([#7420](https://github.com/napari/napari/pull/7420))
- Fix thread warning if not `napari.run()` is called ([#7450](https://github.com/napari/napari/pull/7450))
- Fix highlighting artifacts when selecting multiple shapes ([#7457](https://github.com/napari/napari/pull/7457))
- Fix selection of nD-sliced shapes ([#7459](https://github.com/napari/napari/pull/7459))
- TracksFilter head_length property bug ([#7474](https://github.com/napari/napari/pull/7474))
- Flip z axis on 3D camera to default to right-handed frame ([#7488](https://github.com/napari/napari/pull/7488))

## Documentation

- Add an image to the get_current_viewer example ([#7462](https://github.com/napari/napari/pull/7462))
- Update tutorials ([docs#514](https://github.com/napari/docs/pull/514))
- Add version warning banner for old versions of the docs ([docs#531](https://github.com/napari/docs/pull/531))
- Add troubleshooting page ([docs#533](https://github.com/napari/docs/pull/533))
- add info on how to cross-reference gallery examples  ([docs#534](https://github.com/napari/docs/pull/534))
- Add reference to napari architecture guide in the contributing guide ([docs#537](https://github.com/napari/docs/pull/537))
- Fix broken link in installation tutorial ([docs#539](https://github.com/napari/docs/pull/539))
- Update version_switcher.json for 0.5.5 ([docs#543](https://github.com/napari/docs/pull/543))
- Add resources page with logos ([docs#544](https://github.com/napari/docs/pull/544))
- Fix build-on-windows link in README.md ([docs#546](https://github.com/napari/docs/pull/546))

## Other Pull Requests

- Update `app-model`, `certifi`, `coverage`, `dask`, `hypothesis`, `imageio`, `ipython`, `matplotlib`, `napari-console`, `pydantic`, `pyqt6`, `pytest`, `scikit-image`, `superqt`, `tensorstore`, `tifffile`, `tqdm`, `virtualenv`, `xarray`, `zarr` ([#7406](https://github.com/napari/napari/pull/7406))
- [pre-commit.ci] pre-commit autoupdate ([#7451](https://github.com/napari/napari/pull/7451))
- Update `dask`, `fsspec`, `hypothesis`, `ipython`, `magicgui`, `napari-console`, `psutil`, `pydantic` ([#7464](https://github.com/napari/napari/pull/7464))
- [pre-commit.ci] pre-commit autoupdate ([#7465](https://github.com/napari/napari/pull/7465))
- changes Shapes data to float32 and reduce randomization in tests shapes test ([#7470](https://github.com/napari/napari/pull/7470))
- Fix typo observable in Preferences -> Appearance ([#7472](https://github.com/napari/napari/pull/7472))
- Set pytest configuration file for test run using pip ([#7473](https://github.com/napari/napari/pull/7473))
- Update `coverage`, `hypothesis` ([#7475](https://github.com/napari/napari/pull/7475))
- [py313] Fix test_qt_plugin_sorter on Python >= 3.13 ([#7479](https://github.com/napari/napari/pull/7479))
- [--pre] Update constraints to allow pyOpenGL 3.1.7, but block 3.1.9a1 ([#7480](https://github.com/napari/napari/pull/7480))
- [py313] Update test_prereleases.yml to add py313 ([#7481](https://github.com/napari/napari/pull/7481))
- [py313] Update plugins/test_utils.py to account for Windows py313 os.path.isabs change ([#7482](https://github.com/napari/napari/pull/7482))
- [Maint] Update version_denylist.txt to block zarr rc1 in --pre tests ([#7489](https://github.com/napari/napari/pull/7489))
- [pre-commit.ci] pre-commit autoupdate ([#7494](https://github.com/napari/napari/pull/7494))
- Specify dtype when using zarr.Group.create_array ([#7497](https://github.com/napari/napari/pull/7497))
- remove xfail from test_add_many_zarr_1d_array_is_ignored ([#7501](https://github.com/napari/napari/pull/7501))


## 8 authors added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Colin Watson](https://github.com/napari/napari/commits?author=cjwatson) - @cjwatson +
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Jordão Bragantini](https://github.com/napari/napari/commits?author=JoOkuma) - @JoOkuma
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko


## 8 reviewers added to this release (alphabetical)

(+) denotes first-time contributors 🥳

- [Daniel Althviz Moré](https://github.com/napari/docs/commits?author=dalthviz) - @dalthviz
- [Draga Doncila Pop](https://github.com/napari/napari/commits?author=DragaDoncila) - @DragaDoncila
- [Grzegorz Bokota](https://github.com/napari/napari/commits?author=Czaki) - @Czaki
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Lorenzo Gaifas](https://github.com/napari/docs/commits?author=brisvag) - @brisvag
- [Melissa Weber Mendonça](https://github.com/napari/docs/commits?author=melissawm) - @melissawm
- [Peter Sobolewski](https://github.com/napari/napari/commits?author=psobolewskiPhD) - @psobolewskiPhD
- [Tim Monko](https://github.com/napari/napari/commits?author=TimMonko) ([docs](https://github.com/napari/docs/commits?author=TimMonko))  - @TimMonko

