# Troubleshooting

This page collects a few known issues and solutions for common problems that users might encounter when using napari.
If you are facing an error that is not covered by this page, please check existing issues on the
[napari repository](https://github.com/napari/napari/issues). If you can't find what you are looking for, 
please open a new issue.

## Known issues

### Resetting preferences and settings

Changing napari versions—updating or downgrading—within an environment can cause issues with settings.  These issues can
manifest as napari failing to start. 

Likewise, issues with napari on multiple monitors or with window sizes are also due to settings. These issues can
frequently be solved by resetting the settings back to default using the terminal command:

```python
napari --reset
```

### torch + rosetta + napari crashes Python

In some cases, when using napari on Mac M1 using Rosetta you may experience crashing when adding layers or using a script.
If you observe this, you should run napari using the native arm64 Python interpreter (see [napari#7259](https://github.com/napari/napari/issues/7259).

### "module napari has no attribute Viewer"

This may happen when doing an editable install on top of a normal one, or when you have a local file called `napari.py`.

To fix this, either rename the file or remove all previous napari versions in your environment before installing the editable version.

### My image renders as all black/all white

This can happen when the contrast limits are not set correctly. You can reset the contrast limits by right-clicking
"contrast limits", then clicking the "Reset" button in the dialog shown.

The contrast limits are the minimum and maximum values displayed by the layer. Any value under the smaller contrast
limit will appear as black, while any value above the larger limit will appear as white. Additionally, when all the
values are near the bottom of the range, the image can still appear black even if there are some very dark but not quite
black pixels there.

You can reset the contrast limits by clicking the Auto-Contrast: "Once" button, or, if that fails, right clicking on the
contrast limits to do manual adjustment, including directly editing the numbers shown. When in doubt, you can hover over
the canvas with your image layer selected, and check the status message as you move the mouse around. That will give you
an idea of the range and variability of the data in your layer, helping you set meaningful contrast limits.

### PermissionError when trying to launch napari on Windows

If you have a PermissionError when trying to launch napari on Windows, it could be due to how numba deals with
permissions. Try setting `NUMBA_CACHE_DIR` to an user-accessible location.

See [napari#7288](https://github.com/napari/napari/issues/7288).

