This a small bugfix release, following up the changes in 0.6.5.

### Zooming in the dark?
In the previous release we accidentally made the [zoom tool added in v0.6.3](https://napari.org/stable/release/release_0_6_3.html#a-zoom-with-a-view) invisible. Whoops! No worries, it's back 🔍.

### "Open with napari"

When using the [napari bundle](https://napari.org/stable/tutorials/fundamentals/installation_bundle_conda.html#how-to-install-the-napari-app), it will now detect when a file can be opened with napari based on the extension. This allows you to use the `open with >` menu from your operative system to open files with napari!

![image showing a context menu with the the `open with > napari` option available](https://github.com/user-attachments/assets/f13d58e5-ce2d-460a-b92e-2f23ecc8d438)

PS: Since we did quite a few changes behind the scenes on this new version of the bundle, you might experience some issues. Don't hesitate to open an issue or contact us on zulip if you do!
