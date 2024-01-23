(app-model)=

# napari's application model

```{warning}
**Work in progress!**
The napari application model is currently being developed. This document is here to
give guidance but things may change as we develop. It may link to current
pull requests and issues which have more up to date information on specific
areas.
```

## App-model

[`app-model`](https://app-model--142.org.readthedocs.build/en/142/) is a Python package
that provides a declarative schema for a GUI-based
application. It is an abstraction developed by napari developers, with the
needs of napari in mind, but it is agnostic to napari itself (i.e. it should be
reusable by any python GUI application).

The {class}`app_model.Application`
is the top level object that stores information about the commands, keybindings
and menus that make up the appliation.
The napari global application singleton, `app`, is a subclass of
{class}`app_model.Application`
and can be retrieved with {func}`napari._app_model.get_app`.

Currently, the primary purpose of the `app` is to compose the following
{mod}`app_model.registries` into a single name-spaced object:

* {class}`~app_model.registries.CommandsRegistry`: maintains all of the
  [commands](app-model-commands) (the actual callable objects) that have been
  registered with the application. Accessible via `app.commands`.
* {class}`~app_model.registries.MenusRegistry`: maintains all of the
  [menu and submenus](appp-model-menus) that have been registered with the application.
  Accessible via `app.menus`.
* {class}`~app_model.registries.KeyBindingsRegistry`: maintains the association
  between a [KeyBinding](app-model-keybindings) and a command id in the
  {class}`~app_model.registries.CommandsRegistry`. Accessible via `app.keybindings`.

The app-model
['Getting started'](https://app-model--142.org.readthedocs.build/en/142/getting_started/)
page provides a good general introduction to the app-model.
This documentation will focus on napari specific aspects.

(app-model-actions)=

## Actions

The {class}`app_model.types.Action` class is designed to easily create high level
'Action' object that is the "complete" representation of a command; a pointer
to a callable object and optionally placement in menus, keybindings, and additional
metadata like title, icons, tooltips etc. It subclasses
{class}`app_model.types.CommandRule` and takes {class}`app_model.types.MenuRule` and
{class}`app_model.types.KeyBindingRule` arguments.

The following code demonstrates the definition of a {class}`app_model.types.Action`
comprised of a "Split RGB" command, which is to be added to a specific section (group)
of the "layerlist context" menu, with a `Cmd+Alt+T` keybinding.

Note that while strings could be used for `id`, `title`, `menus.id` and
`keybindings.primary`, the usage of enums and constants makes refactoring and
maintenance much easier (and provides autocompletion in an IDE!). However, there is
currently intention to use plain strings for command `id` and `title` to simplify the
decalaration of Actions.

```python
from app_model.types import Action, KeyMod, KeyCode
from napari._app_model.constants import CommandId, MenuId, MenuGroup
from napari._app_model.context import LayerListContextKeys as LLCK


# `layers` will be injected layer when this action is invoked
def split_rgb_layer(layers: 'LayerList'):
    ...


action = Action(
    id=CommandId.LAYER_SPLIT_RGB,
    title=CommandId.LAYER_SPLIT_RGB.title,
    callback=split_rgb_layer,
    menus = [
        {
            'id': MenuId.LAYERLIST_CONTEXT,
            'group': MenuGroup.LAYERLIST_CONTEXT.SPLIT_MERGE,
            'when': LLCK.active_layer_is_rgb,
        }
    ],
    keybindings=[{'primary': KeyMod.CtrlCmd | KeyMod.Alt | KeyCode.KeyT }]
)
```

Actions can be registered via {func}`app_model.Application.register_action`. This
is essentially a shortcut for registering objects with the following registeries;
{class}`~app_model.registries.CommandsRegistry`,
{class}`~app_model.registries.MenusRegistry` and
{class}`~app_model.registries.KeyBindingsRegistry`. Note that a command ID may
currently only be registered once though this MAY change in the future if a need arises.

The code below shows how to register the `action` defined above with the napari
singleton `app`:

```python
from napari._app_model import get_app


get_app().register_action(action)
```

````{note}
If you're following along in the console, you may see the following error
when executing the above code:

```python
ValueError: Command 'napari:layer:split_rgb' already registered
```

This is because command id's may currently only be registered once, and associated with a single callback (and napari's internal app already used the `CommandId.LAYER_SPLIT_RGB` id).
````

(app-model-actions-napari)=

### Actions in napari

In napari non-Qt Actions are defined in
[`napari/_app_model/actions`](https://github.com/napari/napari/tree/main/napari/_app_model/actions)
while Qt Actions are defined in
[`napari/_qt/_qapp_model/qactions`](https://github.com/napari/napari/tree/main/napari/_qt/_qapp_model/qactions).
Non-Qt Actions get registered with `app` during
initialization of the napari `app`, in {meth}`NapariApplication.__init__`. Qt Actions
get registered in {func}`~napari._qt._qapp_model.qactions.init_qactions`, which gets
called during initialization of `_QtMainWindow`. Note this is relevant when
considering the differences between app-model and action manager implementation,
see [](app-model-action-manager-differences) for more.

(app-model-commands)=

## Commands

Commands represent callable objects that "do something" in napari, and usually
have a corresponding representation somewhere in the GUI (such as a button, a
menu item, or a keybinding).

Inline (lambda) and nested functions should be avoided for command callbacks to
prevent memory leakage.

All commands have a string id (e.g. '`napari:layer:duplicate`'). These are
currently `CommandID` enums but we are currently considering changing to using
plain strings to simplify decalaration of Actions.

{class}`app_model.types.CommandRule` class (of which {class}`app_model.types.Action`
is a subclass) includes many fields to detail various aspects of commands.
See {class}`app_model.types.CommandRule` for details on every field.
Notable {class}`~app_model.types.CommandRule` fields
are `enablement` and `toggled`, which both can take an
{class}`app_model.expressions.Expr`, an expression that can be evaluated, with
context if required (see [](context-expressions) for more details).
`enablement` determines whether the command is enabled in the UI. It does not prevent
the command from being executed via other means, e.g., via
{meth}`app_model.registries.CommandsRegistry.execute_command`. `toggled` determines
whether the command appears checked/toggled in GUI representations (e.g., menu or
button). It can also take a {class}`app_model.types.ToggleRule`, which allows
you to use a callable (instead of a expression) to determine toggle state.

### Commands should *not* be confused with the public napari API

While it is conceivable that plugins might need/want to refer to one of these
napari commands by its string id, it is **not** currently a goal that napari
end-users would execute any of these commands by their ID.  There should always
be a "pure python" way to import a napari object and call it. For example,
sample data is added to the `File` -> `Open Sample` menu but you can also
use {meth}`napari.Viewer.open_sample` to open a sample data in headless mode.

Commands mostly serve as a way to reference some functionality that needs to be exposed
in the GUI.

```{note}
Some of these command ID strings MAY be exposed externally in the future. For example, a plugin may wish to refer to a napari command.
```

### Commands in napari

Commands are usually defined with their Action definition or with it's class,
if it is a class method.
See [](app-model-actions-napari) for details on where Actions are defined in napari.

(app-model-menus)=

## Menus

App-model menus are not limited to the visible menus in the application menu bar, they
can appear anywhere, such as the layerlist context menu that appears when a user
right-clicks on the layer list. They may also be used to create a toolbar (a set
of clickable buttons that execute a command). For example, the mode buttons in
each of the layer controls could be represented as menus with a set of commands.

One of the benefits of the abstraction provided by `app-model` is that actual Qt
Menu objects become simple to construct:

```python
>>> from app_model.backends.qt import QModelMenu
>>> from napari._app_model.constants import MenuId

# create a QMenu with all of the commands registered in the
# layerlist context menu
>>> menu = QModelMenu(menu_id=MenuId.LAYERLIST_CONTEXT, app='napari')

>>> print([i.text() for i in menu.actions()])
[
    'Toggle visibility',
    '',
    'Convert to Labels',
    'Convert to Image',
    'Convert data type',
    '',
    'Duplicate Layer',
    'Split Stack',
    'Split RGB',
    'Merge to Stack',
    'Projections',
    '',
    'Link Layers',
    'Unlink Layers',
    'Select Linked Layers'
]
```

To specify which menu(s) to add an Action to, use the `menus` field in
{class}`app_model.types.Action`. `menus` takes a list of
{class}`app_model.types.MenuRule`. The `id` field allows you to specify which menu
or submenu to add the Action to. All napari menus and submenus will also have a string
id (e.g. `'napari/file'`, or `'napari/layers/context'`), which should be declared as a
member of the {class}`napari._app_model.constants.MenuId` enum. Internally, an instance
of this enum should be used instead of the string literal when referring to a menu.

The `group` and `order` fields let you control how menu items are grouped into sections,
and they are ordered within each section. See {class}`app_model.types.MenuItemBase` for
details on each field.

The `when` field lets you control when the menu item is visible. It can take a
{class}`app_model.expressions.Expr`, an expression that can be evaluated, with
context if required (see [](context-expressions) for more details).

To add a submenu append it to the `app`'s
{class}`~app_model.registries.MenusRegistry`, e.g., via `app.menus.append_menu_items`.
{meth}`app_model.registries.MenusRegistry.append_menu_items` takes a tuple of the
format (`MenuId`, [`MenuItem` or `SubmenuItem`]).

### Menus in napari

In napari `MenuId` and `MenuGroup` enums are defined in
[`napari/_app_model/constants/_menus.py`](https://github.com/napari/napari/blob/main/napari/_app_model/constants/_menus.py).
Menu bar menus are created during {class}`~napari.window.Window` initialization via
{func}`~napari._qt._qapp_model.build_qmodel_menu`. This creates a
{class}`~app_model.backends.qt.QModelMenu` (a subclass of
[`QMenu`](https://doc.qt.io/qt-5/qmenu.html)) instance.
It is the creation of the `QModelMenu` that creates `QActions` for the Actions
associated with that menu.

{class}`app_model.types.SubmenuItem`s are defined in
[`napari/_app_model/_submenus.py`](https://github.com/napari/napari/blob/main/napari/_app_model/_submenus.py).
These are registered during initialization of the napari `app`, in
{meth}`NapariApplication.__init__`.

(app-model-keybindings)=

## Keybindings

App-model has an extensive internal representation of
[Key codes](https://github.com/pyapp-kit/app-model/blob/main/src/app_model/types/_keys/_key_codes.py),
and combinations of key press events (including *chorded* key press sequences such
as `Cmd+K` *followed by* `Cmd+M`).

They will provide independence from
vispy's key codes, and have a nice `IntEnum` API that allows for declaration of
keybindings in a namespaced way that avoids usage of strings:

```python
>>> from app_model.types import KeyCode, KeyMod

>>> ctrl_m = KeyMod.CtrlCmd | KeyCode.KeyM

>>> ctrl_m
<KeyCombo.CtrlCmd|KeyM: 2078>
```

A keybinding can be specified using the `keybindings` field in
{class}`~app_model.types.Action`. This takes a {class}`app_model.types.KeyBindingRule`,
which will let you provide keybindings for all three operating systems.

### Keybindings in napari

App-model keybindings are currently only being used for menu bar items that
have migrated to using app-model `Actions`.
[Pull request 6204](https://github.com/napari/napari/pull/6204) aims to
migrate layer and viewer actions to app-model (though it is likely this pull request
will be split into several smaller pull requests for ease of review and better git
history). This pull request also implements [NAP-7](nap-7), which addresses
how keybindings are dispatched according to their priority, enablement, and potential
conflicts.

Currently keybindings are not able to be edited by the user at runtime but this
is planned. See [issue 6600](https://github.com/napari/napari/issues/6600) for more
details.

## Dependency injection and result processing

Dependency injection allows to write functions using parameter type annotations,
and then inject dependencies (arguments) into those functions at call time.
Very often in a GUI application, you may wish to infer some command arguments from
the current state of the application. For example, if you have menu item linked
to a "close window", you likely want to close the *current* window.
Dependency injection enables this by providing arguments to commands at runtime, based
on the type annotations in the command function definition. A 'provider', a function
that can be called to return an instance of a given type, is used to obtain the
dependency to be injected.

Result processing allows you to process the return value of the command function at
execution time, based on command return type annotations.
For example, you may wish to automatically add layer data output from a command
to the viewer. It is performed by 'processors', functions that accept an instance of a
given type and do something with it. Note that any value returned by a processor will
be ignored, it is the 'processor' function side effects that perform the desired
action (e.g., adding layer data to the viewer).

Dependency injection and result processing are provided by the package
[in-n-out](https://ino.readthedocs.io/en/latest/) (which spun out of an
internal napari module). App-model uses in-n-out to inject dependencies into all
commands in the {class}`~app_model.registries.CommandsRegistry`.
See the [in-n-out documentation](https://ino.readthedocs.io/en/latest/getting_started/)
for details on how providers and processors work.

In napari, providers and processors can be registered in the `app`'s
{attr}`~app_model.Application.injection_store` attribute, which is an instance of
[`in_n_out.Store`](https://ino.readthedocs.io/en/latest/reference/#in_n_out.Store).
This `Store` is just a collection of providers and processors. Providers
and processors in the `Store` will be automatically be used when executing
{class}`~app_model.registries.CommandsRegistry` commands.

```{note}
Injection is implemented in app-model, in the `run_injected` property of
`_RegisteredCommand`. All commands in the `CommandsRegistry` are represented using
the `_RegisteredCommand` type.

```

Below we demonstrate an example of provider use in napari.

A user/plugin provides a function, using the `Points` annotation:

```python
# some user provided function declares a need
# for Points by using type annotations.
def process_points(points: 'Points'):
    # do something with points
    print(points.name)
```

Internally, napari registers a provider that returns the first Points layer of the
current viewer, if there is one present (returning `None` if not). It is
registered in the `app.injection_store` via `app.injection_store.register_provider`. Processors can be registered in the same way.

```python
from napari._app_model import get_app

# return annotation indicates what this provider provides
def provide_points() -> Optional['Points']:
    import napari.viewer
    from napari.layers import Points

    viewer = napari.viewer.current_viewer()
    if viewer is not None:
        return next(
            (i for i in viewer.layers if isinstance(i, Points)),
            None
        )

get_app().injection_store.register_provider(provide_points)
```

This allows both internal and external functions to be injected with these
provided objects, and therefore called *without* parameters in certain cases.
This is particularly important in a GUI context, where a user can't always be
providing arguments:

```python
>>> injected_func = get_app().injection_store.inject(process_points)
```

Note: injection doesn't *inherently* mean that it's always safe to call an
injected function without parameters. In this case, we have no viewer and no
points:

```python
>>> injected_func()

TypeError: After injecting dependencies for NO arguments,
process_points() missing 1 required positional argument: 'points'
```

Our provider was context dependent. Only when we have an active viewer with a
points layer, can it be provided:

```python
>>> viewer = napari.view_points(name='Some Points')

>>> injected_func()
Some Points
```

The fact that `injected_func` may now be called without parameters allows it to
be used easily as a command in a menu, or bound to a keybinding.  It is up to
napari to determine what providers it will make available, and what type hints
plugins/users may use to request dependencies.

### Providers and processors in napari

Non-Qt providers and processors are defined in
[`napari/_app_model/injection`](https://github.com/napari/napari/tree/main/napari/_app_model/injection).
Qt providers and processors are defined in
[`napari/_qt/_qapp_model/injection`](https://github.com/napari/napari/tree/main/napari/_qt/_qapp_model/injection).

Non-Qt providers and processors are registered in the `app` `Store` during
initialization of the napari `app`, in {meth}`NapariApplication.__init__`.
Qt providers and processors are registered in
{func}`~napari._qt._qapp_model.qactions.init_qactions`, which gets called during
initialization of `_QtMainWindow`.

## app-model testing

This section provides a guide to testing app-model aspects of napari. For general
information on napari testing see [](napari-testing).


execute_command (regardless of enabled state)

# Migration from action manager

## Motivation & Future Vision

While it's certainly possible that there will be cases where this abstraction
in app-model proves to be a bit more annoying than the previous "procedural" approach,
there are a number of motivations for adopting this abstraction.

1. It gives us an abstraction layer on top of Qt that will make it much easier to explore different application backends (such as a web-based app, etc..)
1. It's easier to test: `app-model` can take care of making sure that commands, menus, keybindings, and actions are rendered, updated, and triggered correctly, and napari can focus on testing the napari-specific logic.
1. It's becomes **much** easier to add & remove contributions from plugins if our internal representation of a command, menu, keybinding is similar to the schema that plugins use. The previous procedural approach made this marriage much more cumbersome.
1. **The Dream**: The unification of napari commands and plugin commands into a registry that can execute commands in response to user input provides an excellent base for "recording" a user workflow.  If all GUI user interactions go through dependency-injected commands, then it becomes much easier to export a script that reproduces a set of interactions.

(app-model-action-manager-differences)=

## app-model vs action manager implementation differences
