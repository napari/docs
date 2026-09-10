This release continues the 0.5 tradition of churning out the bug fixes and
enhancements, with 24 pull requests total in that category. If you are a user
of oblique plane rendering, you'll appreciate
[#7422](https://github.com/napari/napari/pull/7422), which fixes the plane
calculation when data is anisotropic.

And, did you have a hole in your heart where high-quality 3D labels rendering
should have been? Check out
[#7431](https://github.com/napari/napari/pull/7431), in which [Ashley
Anderson](https://github.com/aganders3) has (again) improved the quality of 3D
labels by filling the (apparent, but fictional) holes in labels at the borders
of a volume. Before/after gif:

![movie showing before and after of labels rendering at the borders of a
volume](https://github.com/user-attachments/assets/728505be-d212-417b-a29e-7228761ffed3)

Additionally, [Grzegorz Bokota](https://github.com/Czaki) has again sped up
launch time for Shapes layers by porting all the edge triangulation code to
numba ([#7268](https://github.com/napari/napari/pull/7268)). As part of that
work he also created a fantastic developer example explaining how the edge
triangulation works, which you can find at
[examples/dev/triangle_edge.py](https://github.com/napari/napari/blob/b2edccd6e40e04467ccfeec0257c2160783f7187/examples/dev/triangle_edge.py).
Give it a read and a play if you want to peek under the hood of the Shapes
layer!

```{raw} html
<figure>
  <video width="100%" controls autoplay loop muted playsinline>
    <source src="../_static/images/triangle-edge.webm" type="video/webm" />
    <source src="../_static/images/triangle-edge.mp4" type="video/mp4" />
    <img src="../_static/images/triangle-edge.png"
      title="Your browser does not support the video tag"
      alt="napari viewer showing a shapes layer and associated layers depicting the triangulation of the elements of the Shapes layer."
    >
  </video>
</figure>
```

Did you miss a napari error or warning while reading these notes? We don't
blame you! Those missed notifications will be a thing of the past with
[#7220](https://github.com/napari/napari/pull/7220), which will keep
notifications open if the napari window is not in focus. Whew!

Finally, for the zarrventurous among you, napari 0.5.5 is ready for zarr v3,
coming soon to a PyPI near you!
([#7215](https://github.com/napari/napari/pull/7215)) If you are using or
testing the zarr 3.0.0 betas, try them with napari! We hope you'll be
pleasantly surprised. 😊

As always, we thank all the contributors to this napari release and all the
previous ones! We welcome [Carol Willing](https://github.com/willingc) and
[Tim Monko](https://github.com/TimMonko) to the list of contributors. Read on
for all the changes in this version!

Read on for all the changes in this version!
