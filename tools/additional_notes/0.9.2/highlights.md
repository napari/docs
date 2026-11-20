### Vispy update

In [#9499](https://github.com/napari/napari/pull/9499) we improved and updated [Vispy](https://vispy.org/) (napari's rendering engine), which brings us a few fixes and new features. Some important ones:

- perspective rendering of points and text is no longer broken (Shift+right-click-drag to change FOV in 3D!)
- RGB data can now be viewed in 3D. This might still have some kinks to smooth out, so if you see issues, make sure to report them on the issue tracker.

### Type checking changes and guide

In [#9395](https://github.com/napari/napari/pull/9395) we have switched our type checking from mypy to [pyrefly](https://pyrefly.org/) because its much faster (>20x!), easier to understand, and well supported. Read our new [typing guide](https://napari.org/stable/developers/contributing/typing.html) for more information on typing the napari code base. Contributors have found typing contributions as a great introduction to contributing to napari and it is work that we welcome. To read more about Aniket's experience, check out the new island dispatch blog post: [From Any to Certainty](https://napari.org/island-dispatch/blog/from-any-to-certainty.html).

### New release policy with regular cadence

The napari team has been working hard to improve our release process, and based on our experience and feedback from the community, we have formally adopted a release policy ([napari/docs#1126](https://github.com/napari/docs/pull/1126)). Expect regular monthly releases and clearer communication about review and timing for contributions; read the [full policy](https://napari.org/stable/developers/coredev/release_policy.html).
