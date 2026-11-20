This release mostly contains a lot of bug fixes and performance improvements.
But look out for 0.5.0, coming to a software repository near you — we expect to
release a lot of new features then!

### BIG improvements to the Labels layer

[#3308](https://github.com/napari/napari/pull/3308) closed *many* long-standing
bugs in the handling of colors in the Labels layer: the color swatch in the
Labels controls now always matches the color on the canvas, direct color
mapping with thousands of colors works fine, and shuffling colors (when two
touching labels coincidentally had the same color) is now much more likely to
map them to different colors. 🎨🚀🚀🚀

Unfortunately, the fix turned out to have rather
terrible consequences for the rendering performance of 3D Labels, and each time
we fixed one thing something else reappeared in a game of bug fix whack-a-mole
that any programmer would recognize. A great many
fixes later (
[#6411](https://github.com/napari/napari/pull/6411),
[#6439](https://github.com/napari/napari/pull/6439),
[#6459](https://github.com/napari/napari/pull/6459),
[#6460](https://github.com/napari/napari/pull/6460),
[#6461](https://github.com/napari/napari/pull/6461),
[#6467](https://github.com/napari/napari/pull/6467),
[#6479](https://github.com/napari/napari/pull/6479),
[#6520](https://github.com/napari/napari/pull/6520),
[#6540](https://github.com/napari/napari/pull/6540),
[#6571](https://github.com/napari/napari/pull/6571),
[#6580](https://github.com/napari/napari/pull/6580),
[#6596](https://github.com/napari/napari/pull/6596),
[#6602](https://github.com/napari/napari/pull/6602),
[#6607](https://github.com/napari/napari/pull/6607),
[#6616](https://github.com/napari/napari/pull/6616),
[#6618](https://github.com/napari/napari/pull/6618)
) — thank you for your patience! 😅 — Labels are faster than ever
*and* color accurate. *But*, to get the best performance, if you can use
8- or 16-bit integers as your data type, you should do so, and if not, you
should install *numba*, a just-in-time compiler for numerical code in Python.
(Ultimately, the data sent to the GPU will be 8- or 16-bit, so if you use a
larger data type, you will pay some conversion cost.)

These improvements in color handling are accompanied by updates to the Labels
API. You can now easily set a specific color cycle for Labels data. For
example, to use the famous [Glasbey look-up table/color
cycle](https://onlinelibrary.wiley.com/doi/10.1002/col.20327), you can combine
the [`glasbey`](https://pypi.org/project/glasbey/) Python package with the new
`CyclicLabelColormap` API:

```python
import glasbey
from napari.utils.colormaps import CyclicLabelColormap
# ...
labels_layer = viewer.add_labels(
    segmentation, colormap=CyclicLabelColormap(glasbey.create_palette(256))
)
```

See the ["Deprecations" section below](#Deprecations) for more information on
the new API. ([#6542](https://github.com/napari/napari/pull/6542))

### More on colormaps!

Yes, this is the colors update! 🌈

Making image layers with linear colormaps using custom colors is easier than
ever! You can just do `viewer.add_image(data, color='turquoise')` to get a
black-to-turquoise linear colormap for that image. For the full list of colors
available, see the
[VisPy color dict](https://github.com/vispy/vispy/blob/269ed1ac4d8126421fd5a7eb06a2996d63f46b17/vispy/color/_color_dict.py#L181)
([#6102](https://github.com/napari/napari/pull/6102)). You can also pass in an
RGB hex color prefixed with `#`, as in
`napari.imshow(data, colormap=`#88ff1a`)`.

(For an amusing side note, though, check out the [API Changes](#api-changes)
note related to this PR. 😅)

### Some technical stuff

If you were worried about those pesky "public access to `qt_viewer` will be
removed" warnings, fret not! Its removal has been postponed until at least
0.6.0! We want to spend more time working with the community to ensure your
use case is supported before pulling out the rug. 🤝 If you are using the
`qt_viewer` because we don't have another public API to do what you need,
please [raise an issue](https://github.com/napari/napari/issues/new) so we can
make sure your use case is supported before we remove it.
([#6283](https://github.com/napari/napari/pull/6283))

Finally, although we still use pydantic 1.0 objects internally, napari
installs correctly with both pydantic v1 and pydantic v2. If you wanted to
upgrade your napari library or plugin to use Pydantic 2, now you can!

Note though, for 0.4.19, the napari bundled app still ships with Pydantic 1.x.
However, we will bundle v2 starting with 0.5.0, so if you use Pydantic
internally, now is a good time to check that you are compatible either v2 or
both v1 and v2
([#6358](https://github.com/napari/napari/pull/6358)).

### Onwards!

As always, napari is developed by the community, for the community. We want to
hear from you and help you get your napari visualization and/or plugin use done
faster! And if napari is missing something you need, we can help you add it! So
please remember to ask [questions on
image.sc](https://forum.image.sc/tag/napari), join our [Zulip chat
room](https://napari.zulipchat.com/), come to our [community
meetings](https://napari.org/stable/community/meeting_schedule.html), or [tag
us on Mastodon](https://fosstodon.org/@napari)!

Read on for the full list of changes that went into this release.
