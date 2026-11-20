Another release with a lot of bug fixes, but also some (more!) improvements to
Shapes layer performance ([#7144](https://github.com/napari/napari/pull/7144),
[#7256](https://github.com/napari/napari/pull/7256)), and a few nice
usability/quality of life features!

- you can now follow the value under the cursor around in images in 3D view as
  well as 2D ([#7126](https://github.com/napari/napari/pull/7126))
- Use standard keyboard shortcuts to zoom in and out ({kbd}`Command/Ctrl+=`,
  {kbd}`Command/Ctrl+-`) and to zoom-to-fit ({kbd}`Command/Ctrl+0`)
  ([#7200](https://github.com/napari/napari/pull/7200))
- you can now save tiff files larger than 4GB
  ([#7242](https://github.com/napari/napari/pull/7242))

Finally, we're starting some work on tweaking the UI to make it more
self-consistent, with the ultimate goal of adding functionality such as showing
common controls when multiple layers are selected, so that, for example, you
can select multiple layers and adjust all their opacity settings together. As
the first step for this, the *layer blending* controls have been moved directly
under the opacity control, so that all per-layer controls are next to each
other in the UI ([#7202](https://github.com/napari/napari/pull/7202))

Read on for all the changes in this version!
