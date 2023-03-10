# napari 0.2.6

We're happy to announce the release of napari 0.2.6! napari is a fast,
interactive, multi-dimensional image viewer for Python. It's designed for
browsing, annotating, and analyzing large multi-dimensional images. It's built
on top of Qt (for the GUI), vispy (for performant GPU-based rendering), and the
scientific Python stack (numpy, scipy).

For more information, examples, and documentation, please visit our website:
https://github.com/napari/napari

## New Features

- label axes with strings ({pr}`644`)
- interactive scripting with `viewer .update`({pr}`650`)
- add dock widget support ({pr}`695`)
- dockable console ({pr}`714`)

## Improvements

- improve release guide ({pr}`668`)
- add logo to repo ({pr}`674`)
- improve labels painting speed ({pr}`684`)
- add example showing mouse drag callbacks ({pr}`690`)
- add main window option to screenshots ({pr}`722`)

## Bug Fixes

- allow all animation thread tests to be +/- 1 frame ({pr}`670`)
- document qt not qt5 ({pr}`677`)
- fix init of `_position` ({pr}`680`)
- fix 3d display surface ({pr}`682`)
- set arcballCamera fov default ({pr}`683`)
- cleaning for interactive scripting ({pr}`688`)
- change no. of pixels calculation from 32 to 64-bit ({pr}`692`)
- support multichannel dask array ({pr}`701`)
- Don't calc_data_range on uint8 data ({pr}`705`)
- allows Path in io.magic_imread ({pr}`709`)
- handles empty chosen files and folder ({pr}`715`)
- relax `play_api` ({pr}`717`)
- raise main window when showing ({pr}`721`)
- fix vertical scrollbars ({pr}`728`)
- revert "change no. of pixels calculation from 32 to 64-bit" ({pr}`738`)
- remove vispy backport with 0.6.3, fix segfault in #576 ({pr}`739`)
- improve pyramid guessing ({pr}`740`)

## 7 authors added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Guillaume Gay](https://github.com/napari/napari/commits?author=glyg) - @glyg
- [Hagai Har-Gil](https://github.com/napari/napari/commits?author=HagaiHargil) - @HagaiHargil
- [Heath Patterson](https://github.com/napari/napari/commits?author=NHPatterson) - @NHPatterson
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03

## 5 reviewers added to this release (alphabetical)

- [Ahmet Can Solak](https://github.com/napari/napari/commits?author=AhmetCanSolak) - @AhmetCanSolak
- [Hagai Har-Gil](https://github.com/napari/napari/commits?author=HagaiHargil) - @HagaiHargil
- [Juan Nunez-Iglesias](https://github.com/napari/napari/commits?author=jni) - @jni
- [Nicholas Sofroniew](https://github.com/napari/napari/commits?author=sofroniewn) - @sofroniewn
- [Talley Lambert](https://github.com/napari/napari/commits?author=tlambert03) - @tlambert03
