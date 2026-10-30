This is primarily a bug-fix release, including fixes for a couple of nasty
regressions in 0.5.0 ([#7184](https://github.com/napari/napari/pull/7184)) and
0.5.2 ([#7201](https://github.com/napari/napari/pull/7201)). However, we also
have a couple of *excellent* user-facing improvements:

- In [#7090](https://github.com/napari/napari/pull/7090), new contributor [Bean
  Li](https://github.com/beanli161514) fixed a *very* long-standing issue in
  napari: 3D picking didn't work when using a perspective projection (rather
  than the default orthogonal projection. The result is glorious:

  ![animated gif showing picking of points in 3D filaments using a perspective projection camera](https://github.com/user-attachments/assets/58036c3c-5776-4f13-bb49-562334b53834)

  There's still a lot of work to be done in perspective projection (dragging
  planes, for example, still doesn't work), but this is an exciting first step,
  and we are thrilled that it came from a new community member! Thanks
  [@beanli161514](https://github.com/beanli161514)!

- In [#7146](https://github.com/napari/napari/pull/7146), napari team member
  [Grzegorz Bokota](https://github.com/Czaki) fixed a long-standing issue in
  napari: Layer.get_status used to be computed on the main thread, which meant
  that layers for which this involved heavy computation (such as large Labels
  layers, or Shapes layers or 3D surface layers with lots of polygons) would
  slow down the viewer refresh rate. Grzegorz's changes move the computation to
  a separate thread, which will dramatically improve performance in many
  situations. 🚀🚀🚀

Thanks as always to all our contributors, and read on for the full list of
changes!
