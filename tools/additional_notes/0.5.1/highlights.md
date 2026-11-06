napari 0.5.1 is a bugfix release hot on the heels of
[napari 0.5.0](release_0_5_0). It fixes a critical bug with creating viewers
multiple times within a single IPython/Jupyter session
([#7106](https://github.com/napari/napari/pull/7106)), as well as regressions
with viewing multiscale 3D time series
([#7103](https://github.com/napari/napari/pull/7103)) and with converting image
layers to labels layers ([#7095](https://github.com/napari/napari/pull/7095)).

It also fixes a bug with NumPy 2 support
([#7104](https://github.com/napari/napari/pull/7104) and our storing of layer
axis info when using the `channel_axis` keyword argument for images
([#7089](https://github.com/napari/napari/pull/7089)).

Read on for the full list of changes since the last version from just two weeks
ago!
