
[#6102](https://github.com/napari/napari/pull/6102) added the ability to set
linear colormaps from black to a named color by using `colormap="color-name"`
syntax. It turns out that "orange" is both the name of a
white-to-orange colormap in VisPy, and one of the color names in the color
dictionary, therefore implicitly a *black-to-orange* colormap! We decided to use
the new, color-name behavior in this update. So if you are wondering why your
`imshow(data, colormap='orange')` calls look different — this is why.

In [#6178](https://github.com/napari/napari/pull/6178), the "action" type of
events emitted when editing Shapes or Points was changed to be more granular.
The types are no longer "add", "remove", and "change", but "adding", "added",
"removing", "removed", "changing", and "changed". This gives listeners more
control over when to take action in response to an event.
