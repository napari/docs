# Troubleshooting

This page collects a few known issues and solutions for common problems that users might encounter when using napari.
If you are facing an error that is not covered by this page, please
[open an issue](https://github.com/napari/napari/issues/new) in the napari repository.

## Known issues

### Resetting preferences and settings

Changing napari versions—or conda envs with different napari versions—can cause issues with settings. These issues can
be solved by resetting the settings back to default using the terminal command:

```python
napari --reset
```

### torch + rosetta + napari crashes Python

In some cases, when using napari on Mac M1 using Rosetta you may experience crashing when adding layers or using a script.
If you observe this, you can try to run napari using the native arm64 Python interpreter (see [napari#7259](https://github.com/napari/napari/issues/7259).

### "module napari has no attribute Viewer"

This may happen when doing an editable install on top of a normal one, or when you have a local file called `napari.py`.

To fix this, either rename the file or remove all previous napari versions in your environment before installing the editable version.

### My image renders as all black/all white

This can happen when the contrast limits are not set correctly. You can reset the contrast limits by right-clicking "contras limits", then clicking the "Reset" button in the dialog shown.

### napari + numba combination doesn't work on admin installs of Windows

If you have trouble using napari together with numba on Windows, try setting `NUMBA_CACHE_DIR` to an user-accessible location.

See [napari#7288](https://github.com/napari/napari/issues/7288).

## FAQ

### How do I use napari in a remote Jupyter env?

napari is a native Qt app so it's not possible to do this directly within a Jupyter notebook or JupyterLab tab. However, we are working on documenting options for this workflow.
