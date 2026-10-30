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
  You can install it automatically by pip installing `"napari[optional,pyqt]"`
  (or a GUI backend of your choice among pyqt, pyqt6, pyside, pyside6) or
  `"napari[all]"`.
- *and*, in the napari advanced settings, tick the "Use C++ code to speed up
  creation and updates of Shapes layers" box.

Please give it a try and let us know if you encounter any issues! This is the
beginning of a new era of performance improvements in napari, to help it live
up to its promise of a *fast* viewer for n-dimensional data in Python!

### New path drawing tool

Drawing paths is easier and smoother with the open-line equilavent of the
lasso tool. If you want to draw a curve through your data, whether with a
mouse or a tablet+stylus, it is now much easier to freehand rather than
clicking on individual points. Try it out!
([#7099](https://github.com/napari/napari/pull/7099))

```{raw} html
<figure>
  <video width="100%" controls autoplay loop muted playsinline>
    <source src="https://github.com/user-attachments/assets/978584f7-f707-4085-840f-a2f8fee12e21" type="video/mp4" />
    <img src="https://github.com/user-attachments/assets/20892add-2382-490b-8ad8-6efc023395a7"
      title="Your browser does not support the video tag"
      alt="video of new path-drawing tool used to delineate a blood vessel"
    >
  </video>
</figure>
```

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

Read on for the full list of changes since 0.5.5.
