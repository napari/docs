The napari 0.7.1 release includes many new features and improvements. Here are some of the highlights:

### Signed Windows bundle

Starting with the napari 0.7.1 release, our bundle on Windows is now [signed](https://github.com/napari/packaging/pull/387) with a NumFOCUS certificate, like our macOS bundle has been. This means that you should be able to run napari without any warnings about the application being from an unknown publisher. This is an important step forward for our Windows users, as it enhances security and trust in our application, especially in managed IT environments where unsigned applications may be blocked by default.

The certificate is issued for the NumFOCUS foundation, which supports napari and a large number of other open source projects.

If you encounter any issues related to this change, please let us know!


### Selection of the rendered level for multiscale layers

Prior to napari 0.7.1, when rendering a multiscale layer:

- in 3D display, napari would always render the lowest resolution level of the pyramid
- in 2D display, the pyramid level would be automatically selected based on the viewport

Thanks to [#8917](https://github.com/napari/napari/pull/8917), users can now [select a multiscale level to render](https://napari.org/dev/howtos/layers/image.html#locking-the-multiscale-level) ([check out the awesome new example!](https://napari.org/stable/gallery/add_multiscale_volume.html)). Importantly, this allows choosing a higher resolution rendering than before in 3D, as long as the selected level can fit within GPU texture limits. Meanwhile, for 2D display, you can fix the resolution level, which can be useful for annotation or previewing data prior to an analysis or export step. You can set this resolution using the resolution widget in the layer controls:

![The resolution dropdown in the layer controls allows the user to select different levels of a multiscale image.](https://github.com/user-attachments/assets/862e7512-0309-429c-b155-a9c03acf2db6)


### Colorbars for points layer

The points allows coloring points based of their feature values; in napari 0.7.1 we added support for colorbars ([#8624](https://github.com/napari/napari/pull/8624)), so you can now easily see the mapping between feature values and colors, just like the colorbars for image colormapping. This is especially useful when you have a large number of points and want to quickly understand the distribution of feature values.

![Example of colorbar for points layer](https://github.com/user-attachments/assets/1522aa7c-3520-4e41-85e6-99e9a91c47ee)

### Scalebar with units

In previous versions of napari, if you added a scale bar using **View > Scale Bar > Scale Bar visible**, it was shown with no units. In napari 0.7.1 we now
set default unit to `pixel` in [#8900](https://github.com/napari/napari/pull/8900) and also add calculation of units for scale bar based on currently added layers in [#8907](https://github.com/napari/napari/pull/8907) and [#9007](https://github.com/napari/napari/pull/9007), if they have units set and are logically consistent across layers.
We've also [added a guide about unit and scale aware rendering](https://napari.org/stable/guides/units.html)  ([#1032](https://github.com/napari/docs/pull/1032)).


![Scale bar with units](https://github.com/user-attachments/assets/b25a1a53-b9a0-46f1-b88c-c2625e4287a8)

### Lock layer to prevent accidental deletions

In [#8736](https://github.com/napari/napari/pull/8736) we added the initial implementation for a [lock mechanism for layers](https://napari.org/stable/getting_started/layers.html#layer-locking). Now, when a layer is locked, it cannot be accidentally deleted or destructively modified. This is especially useful when you have a complex project with many layers and want to prevent accidental changes to important layers. Note: the layer controls are not affected by the lock at this time.
In the future we plan to expand this feature to prevent not only deletion but also other modifications.

![Lock layer on layer list](https://github.com/user-attachments/assets/1df17b1e-cb52-4b2f-88b3-495f1e5301a0)
