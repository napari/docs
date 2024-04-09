(magicgui_type_registration)=

# `magicgui` type registration

[`magicgui`](https://pyapp-kit.github.io/magicgui/) uses
[type hints](https://peps.python.org/pep-0484/) to infer the appropriate widget type
for a given function parameter. It allows third party packages
(like `napari`) to [register](https://pyapp-kit.github.io/magicgui/type_map/#registering-support-for-custom-types) support for their types using
{func}`~magicgui.type_map.register_type`. `napari` registers
a number of types, additionally specifying, where appropriate:

* widget type for the parameter type
* function for updating inputs for the widget
* return callback, for return types

This enables `magicgui` widgets to be easily created via type hints.

```{note}
This page provides implementation details on `napari`-specific type registration
in `magicgui` and is aimed at `napari` developers.

For information about using `magicgui` (for users and plugin developers) see
[](creating-widgets).
```

## Registration details

`napari` types are either registered via the
{func}`@register_type <magicgui.type_map.register_type>` decorator when they are defined or in
[`napari/types.py`](https://github.com/napari/napari/blob/main/napari/types.py).
For the full list of types registered, see [](magicgui-parameter-annotations).

All 'layer' types provide a `choices` callable when registering.
This means that annotating with these types will result in an input
{class}`~magicgui.widgets.bases.CategoricalWidget`, which will get updated via the
`choices` callable. This callable is either `get_layers_data` or `get_layers`.
These functions retrieve the closest parent `Viewer` of the native
{class}`~magicgui.widgets.bases.CategoricalWidget` widget and returns a list of
{class}`~napari.layers.Layer` or tuple of format ('layer name', `<LayerType>Data`).
This callable is set to the `choices` attribute of the
{class}`~magicgui.widgets.bases.CategoricalWidget` in its
{meth}`~magicgui.widgets.bases.CategoricalWidget.reset_choices` method and thus
gets called via {class}`~magicgui.widgets.bases.CategoricalWidget`'s `choices` setter.
`napari` {meth}`~napari.qt.Window.add_dock_widget` checks if the dock widget has
a `reset_choices` attribute and if so, connects it to layer events.
Note that `magicgui` {class}`~magicgui.widgets.bases.ContainerWidget`'s will call
`reset_choices` on all subwidgets. This means that when the dock widget is a
{class}`~magicgui.widgets.bases.ContainerWidget`, any subwidgets (e.g.,
{class}`~magicgui.widgets.bases.CategoricalWidget`s) are updated
whenever layers change.
**Note that {meth}`~napari.qt.Window.add_dock_widget` will
connect any existing `reset_choices` widget attribute to layer events for all widgets,
not just `magicgui` widgets.**

The 'layer' types also specify a `return_callback` function that adds the layer
to the closest parent `Viewer` of the native widget when a 'layer' type is a return
annotation.

{class}`~napari.viewer.Viewer` differs from the Layer types. `napari` simply specifies
that the {class}`~napari.viewer.Viewer` be bound to a widget (technically a
hidden {class}`~magicgui.widgets.EmptyWidget`). The user will need to specify
the widget type for this annotation.

```{important}
`magicgui` type registration allows `napari` to specify useful defaults when creating
widgets for specific types. It does **not** provide the type object.
This is done via dependency injection by "providers" (see
[](app_model_dep_inj_result) for details).
```
