### Dropped support for Qt5 backend

We started warning about this in release v0.8.0; it is now time to fully drop support of Qt5! Qt5 has reached End Of Life on the 26th of May 2025. We migrated our bundle to Qt6 (PySide6) a year ago.
[#9650](https://github.com/napari/napari/pull/9650) is effectively removing PyQt5 support. PySide2 support was already removed in release [0.7.0](https://github.com/napari/napari/pull/8450), so we are now fully on Qt6!

### Tidied up mouse callbacks

Custom mouse callbacks can be [defined via generators](https://napari.org/stable/howtos/extending/connecting_events.html#listening-for-mouse-events). Some quirks with this machinery have been smoothed out and some bugs fixed ([#9513](https://github.com/napari/napari/pull/9513)); this might cause some callbacks to no longer work as before. In principle, this should only affect callbacks that relied on buggy behavior, but please make sure to check if your old callbacks are still working, and open an issue on the napari repository if that's not the case.

A notable change is that `mouse_move` callbacks previously did not work during `drag`, but now they do. If that's not what you want, guard your callback with `if not event.is_dragging`!

### Removed `scale_bar.unit`

After deprecating it, we're finally removing this field completely ([#9218](https://github.com/napari/napari/pull/9218)). Now the only way to set the unit on the scale bar is by [setting units on the layers themselves](https://napari.org/stable/guides/units.html#scale-and-units-live-on-layers)!

### Unified default font sizes

We previously hardcoded default font sizes for all visuals in the canvas. Now ([#8667](https://github.com/napari/napari/pull/8667), [#9524](https://github.com/napari/napari/pull/9524)), they respond to the global application settings (`Preferences > Appearance > Font size`) unless the font size is explicitly set for that specific model (by default it will be `None`).

So if you use the `scale_bar`, or `Points.text` or other layers and overlays that display text and you don't like the new default, make sure to set your font size explicitly!

### Key-bindings auto-repeat enabled by default

With [#9361](https://github.com/napari/napari/pull/9361), key-binding callbacks are now auto-repeated as everything else on your system. If your callbacks is a single-shot function, it will repeat when held; if it's a generator, it will behave as before. The flag `repeatable=True` no longer has an effect.
