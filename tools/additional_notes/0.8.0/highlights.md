### Dropping Python 3.10 and PyQt5

napari 0.8.0 drops support for Python 3.10
([#9104](https://github.com/napari/napari/pull/9104)) and deprecates PyQt5
support ([#9079](https://github.com/napari/napari/pull/9079)).

These changes are being made to help maintenance of napari. Python 3.10 will
reach end-of-life support in October 2026, while PyQt5 has already reached
end-of-life, and is becoming increasingly difficult to maintain as a
dependency. PyQt6, in contrast, has been the daily driver for the napari core
team for many months. As we recognise that PyQt5 has extensive usage in the
community, we have decided to deprecate it in this release and drop support
in Q4 2026. If your project still depends on Qt5, consider migrating to PySide6
or PyQt6. As always, feel free to get in touch
[on our Zulip](https://napari.zulipchat.com) if you encounter any issues!

### Histogram for Image layer

It's been a heckuva long time coming, but napari Image layers *finally* gain a
[built-in histogram (#8391)](https://github.com/napari/napari/pull/8391)!
Wonder no more about why your image looks black or totally washed out — you can
now see the distribution of your pixels' brightness right there in the layer
controls, or within the larger contrast limits widget (which, as a reminder,
you can access by right clicking on the contrast limits slider).

You can access the brightness of the current slice (default), or the full
layer, *and* it will sample progressively from remote chunks if you are looking
at large remote data. Try it out!

```{raw} html
<figure>
  <video width="100%" controls autoplay loop muted playsinline>
    <source src="../_static/images/histogram.webm" type="video/webm" />
    <source src="../_static/images/histogram.mp4" type="video/mp4" />
    <img src="../_static/images/histogram.jpg"
      title="Your browser does not support the video tag"
      alt="Video showing a napari viewer with a 2D canvas showing a slice of a large 3D image. The layer controls include a histogram of image intensities that updates as you pan around the canvas, and also, when selecting the full image, as pixels are drawn from remote data."
    >
  </video>
</figure>
```

### Synced cameras between 2D and 3D views

Ever switched between 2D and 3D views to check out your data, only to be
frustrated that the zoom and center has been reset? Now, by default, the
cameras are
[synced between views (#9151)](https://github.com/napari/napari/pull/9151)!
The synced camera's zoom and center persists when switching between 2D and 3D,
with the depth (Z) component synced through the dimension slider to complete
the round-trip.

To unlock the cameras from each other for completely separate views, you can
toggle `viewer.camera.synced = False` from the Camera popup (right-click 2D/3D
button) or **Toggle Synced Camera** (Ctrl/Cmd+U) in the **View** menu. Set your
preferred default in **Preferences** -> **Application** -> **Synced Camera**.

```{raw} html
<figure>
  <video width="100%" controls autoplay loop muted playsinline>
    <source src="../_static/images/synced-cameras.webm" type="video/webm" />
    <source src="../_static/images/synced-cameras.mp4" type="video/mp4" />
    <img src="../_static/images/synced-cameras.jpg"
      title="Your browser does not support the video tag"
      alt="Video showing zoom and position staying in sync between 2D and 3D views of the same data."
    >
  </video>
</figure>
```

### Auto-fill label contours when painting

Annotating blobs in 2D just got a lot faster! In paint mode, right-click to
start a *self-filling* area annotation. Then draw your shape, and when you come
back around to the start point, the shape will automatically fill with your
selected label! ([#9075](https://github.com/napari/napari/pull/9075))
See it in action below:

```{raw} html
<figure>
  <video width="100%" controls autoplay loop muted playsinline>
    <source src="../_static/images/auto-fill-labels.webm" type="video/webm" />
    <source src="../_static/images/auto-fill-labels.mp4" type="video/mp4" />
    <img src="../_static/images/auto-fill-labels.jpg"
      title="Your browser does not support the video tag"
      alt="Video showing an annotation around a coin, with the coin filling with the annotated label at the end."
    >
  </video>
</figure>
```

We intend to keep refining this functionality, so if you like it but it doesn't
*quite* fit in your workflow, please {ref}`get in touch <community>`!

### Paint into more arrays faster!

Labels painting is now much faster for zarr arrays, and you can now paint into
other array types such as dask and tensorstore! Painting with very large brush
sizes (e.g. 1,000) is now possible where it used to be extremely choppy. Give
it a whirl! ([#8636](https://github.com/napari/napari/pull/8636))

### Floating axes overlay

Ever feel disoriented looking at your data? You're not alone. Until
[#8262](https://github.com/napari/napari/pull/8262), the axes overlay would
live in the same space as your data, and would be out of view if you didn't
have the top left corner of your data on the canvas. Now you can have a little
2- or 3-axis compass always on in a corner of the canvas. Find it in the View
menu!

### Improving the napari theme

Like many things in community-run open source, napari's theme grew organically
as we added features and UI elements.
[#8927](https://github.com/napari/napari/pull/8927) unified the look of many of
those elements, while [#9078](https://github.com/napari/napari/pull/9078)
improved the default light and dark themes by increasing contrast to meet
[Web Content Accessibility Guidelines][WCAG]. Want to build your own
WCAG-compliant theme? Try out the new WCAG table in
[`examples/theme_sample.py`][theme-sample]
([#9175](https://github.com/napari/napari/pull/9175))!

![sample showing the theme sample widget along with a WCAG compliance table](https://github.com/user-attachments/assets/44510228-1163-4532-9945-aea5f7657ff0)

[WCAG]: https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines
[theme-sample]: https://github.com/napari/napari/blob/700a36f148dc073d281b5a9e42bb28cd18ed6a32/examples/theme_sample.py
