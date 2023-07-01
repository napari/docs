(nap-7)=

# NAP-7 — Key Binding Dispatch

```{eval-rst}
:Author: "Kira Evans <mailto:contact@kne42.me>"
:Created: 2023-06-30
:Status: Draft
:Type: Standards Track
```

## Abstract

With the switching of the internal key binding system to use app-model's representation[^id1], there is discussion as to what exactly constitutes a valid key binding and how conflicts are handled[^id2].

This NAP seeks to clarify and propose a solution for how key bindings will be dispatched according to their priority, enablement, and potential conflicts.

## Motivation and Scope

Plugin developers are able to export commands in their manifest file but cannot similarly set their shortcuts in a code-free way. npe2 provides an option to bind commands to key binding but it is undocumented and unsupported since napari still uses an old dispatch system of chainmaps.

### A more versatile system

The proposed dispatch system would leverage weights to clearly separate default, plugin, and user-defined key binding as well as support a more advanced conditional system which would determine if a keybinding is active/enabled or not. Both of these properties are already part of the specification defined by app-model.

Separation of different sources of key binding makes it easier for a user to determine who set the binding as well as how to restore the default.

Conditional evaluation allows plugin developers to tie their keybinding to a specific viewer state.

### Definitions

**modifier keys** refer to `ctrl`, `shift`, `alt`, and `meta`. `meta` is also known as `cmd`, `win`, or `super` on osx, windows, or linux, respectively

a **base key** is one of the following supported keys:
- `f1-f12`, `a-z`, `0-9`
- `` ` ``, `-`, `=`, `[`, `]`, `\`, `;`, `'`, `,`, `.`, `/`
- `left`, `up`, `right`, `down`, `pageup`, `pagedown`, `end`, `home`
- `tab`, `enter`, `escape`, `space`, `backspace`, `delete`
- `pausebreak`, `capslock`, `insert`, `numlock`, `printscreen`
- `numpad0-numpad9`, `numpad_decimal`, `numpad_multiply`, `numpad_divide`, `numpad_add`, `numpad_subtract`

a **key combination** is a base key pressed with one or more modifier keys, e.g. `ctrl+c` or `ctrl+shift+z`

a **key chord** consists of two parts, of which each can be either a base key or a key combination, e.g, `ctrl+x v`

a **key sequence** refers to a series of inputs by the user which can be a base key, key combination, or key chord

a **key binding** binds a key sequence to a command with conditional activation

### Key binding validity: convenience vs. complexity

Some users want to use traditional modifier keys as a base key in key binding for convenience purposes [^id2]. However, this can lead to conflicts since many key bindings may include the modifier key in their key sequence and thus cause confusion and cost extra engineering effort.

The proposed restrictions on what key sequences can be used in a key binding aim to allow for the simplest user need while cutting down on any unnecessary complexities:

- key combinations containing any modifier keys as a base key are invalid
- key chords cannot contain a base key that is a modifier key (aka a single modifier)

Here are some examples:
- `alt` is **valid** as a base key because it contains no other modifiers and no other parts
- `alt-meta` is **invalid** because it is a key combination comprised of only modifiers
- `alt+t` is **valid** as a key combination
- `alt t` is **invalid** because it is a key chord whose first part is a single modifier 
- `ctrl+x alt` is **invalid** because it is a key chord whose second part is a single modifier
- `ctrl+x alt+v` is **valid** as a key chord
- `meta meta` is **invalid** because it is a key chord comprised of only single modifier parts

## Detailed Description

Even with conditional activation, many key bindings may find that they share the exact same key sequence as another key binding (a direct conflict), or that their key sequence is a subset of another key binding's key sequence (an indirect conflict). This requires the establishment of a system to determine when and how key bindings should be dispatched.

### Key binding properties

All key binding entries contain the following information:
- `command_id` is the unique identifier of the command that will be executed by this key binding
- `weight` is the main determinant of key binding priority. high value means a higher priority
- `when` is the context expression that is evaluated to determine if the key binding is active; if not provided, the key binding is always considered active
- (autoset) `block_rule` is enabled if `command_id == ''` and disables all lower priority key bindings
- (autoset) `negate_rule` is enabled if `command_id` is prefixed with `-` and disables all lower priority key bindings with the same sequence bound to this command

```python
from dataclasses import dataclass, field

from app_model.expressions import Expr

@dataclass(order=True)
class KeyBindingEntry:
    command_id: str = field(compare=False)
    weight: int
    when: Optional[Expr] = field(compare=False)
    block_rule: bool = field(init=False)
    negate_rule: bool = field(init=False)
    
    def __post_init__(self):
        self.block_rule = self.command_id == ''
        self.negate_rule = self.command_id.startswith('-')
```

### Direct conflicts

When two key bindings share the same key sequence, they are considered to be in direct conflict. They are sorted first according to their weight, then whether they are a blocking rule, whether they are a negate rule, and otherwise, based on their insertion order. This is done in ascending order such that higher weights and blocking/negate rules are moved further down the list.

Key bindings will automatically be assigned weights depending on who set them, prioritizing default ones the least and user-set ones the most:

```python
from enum import IntEnum

class KeyBindingWeights(IntEnum):
    CORE = 0
    PLUGIN = 300
    USER = 500
```

### Indirect conflicts

When a key sequence matches a key binding and is also a sub-sequence of a key sequence used by another key binding, it is considered an indirect conflict.

There are two ways indirect conflicts can exist:

A. the provided key sequence is a single modifier that is a modifier in another key binding's key combination or is a modifier in the first key combination of a key binding's key chord

B. the provided key sequence is a base key or key combination that is the first part of another key binding's key chord

In case (A), the corresponding command will not be triggered immediately, but will be delayed by user-defined miliseconds (e.g. 200ms), after which the press logic for the command will execute. If another key binding is triggered, this action will be canceled. If the base key is released early, the press logic will execute immediately and the delayed action will be canceled, along with the release logic being executed immediately afterwards.

In case (B), the corresponding command will never be triggered so long as it indirectly conflicts with another key binding. In this sense, multi-part key bindings will always take priority over single-part key bindings.

### Finding a match

When checking if an active key binding matches the entered key sequence, the resolver will fetch the pre-sorted list of direct conflicts and check if the last entry is active using its `when` property, moving to the next entry if it is not. When it encounters a blocking rule, it will return no match, and for a negate rule, it will store the affected command in an ignore list and continue to the next entry. If no special rules are present, it will return a match if the command is not in an ignore list, otherwise continuing to the next entry, and so on, until no more entries remain.

In psuedo-code this reads as:
```python
def find_active_match(entries: List[KeyBindingEntry]) -> Optional[KeyBindingEntry]:
    ignored_commands = []

    for entry in reversed(entries):
        if isactive(entry.when):
            if entry.block_rule:
                return None
            elif entry.negate_rule:
                ignored_commands.append(entry.command_id[1:])
            elif entry.command_id not in ignored_commands:
                return entry
```

### Leveraging data structures to find conflicts

Finding indirect conflicts can be tricky and computationally intensive. As such, all subsets are encoded in a data structure similar to a _[trie](https://en.wikipedia.org/wiki/Trie)_ (aka a _prefix tree_). Since modifier keys do not care about what order they are pressed in, we will use a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) instead of a traditional tree, essentially making this a _prefix [multitree](https://en.wikipedia.org/wiki/Multitree)_.

```{figure} ./_static/kb-example-graph.png
---
name: fig-1
---
Fig. 1: Example of a prefix multitree. Filled nodes have at least one key binding as detailed on the legend in the top left corner.
```

This effectively breaks the key sequences of the key bindings into their respective components, as in {ref}`Fig. 1 <fig-1>`, and can be represented with a fairly simple data structure:

```python
from app_model.types import KeyBinding

@dataclass
class Node:
    value: KeyBinding
    root: List[KeyBindingEntry]
    children: Dict[KeyCode, Node]
```

To check if a key binding has an indirect conflict, the children of the node can be recursively searched depth-first:

```python
def has_active_children(children: Dict[KeyCode, Node]) -> bool:
    for child in children.values():
        if find_active_match(child.root):
            return True
        elif has_active_children(child.children):
            return True
```

Additionally, in the future, this data structure could be used for command completion.

### Completing the dispatch

Putting everything together, the following psuedo code represents the logic of key binding dispatch:

```python
from threading import Timer

from app_model.types import KeyBinding, KeyCode, KeyMod

VALID_KEYS: List[KeyCode] = ...
PRESS_HOLD_DELAY_MS: int = 200

def search_node(children: Dict[KeyCode, Node], components: Sequence[KeyCode]) -> Optional[Node]:
    first, *rest = components
    if first in children:
        node = children[first]
        if rest:
            return search_node(rest, node.children)
        return node

class KeyBindingDispatcher:
    root: Dict[KeyCode, Node]
    prefix: Tuple[KeyCode]
    timer: Optional[Timer]
    active_mods: Optional[KeyMod]
    active_key: Optional[KeyCode]
    ...
    def on_key_press(self, mods: KeyMod, key: KeyCode):
        self.active_key = None
        if self.timer:
            self.timer.cancel()
            self.timer = None
        if key not in VALID_KEYS:
            # ignore input
            self.prefix = ()
            return

        keymod = key2mod(key)

        if keymod is not None:
            # modifier base key
            if self.prefix:
                # single modifier dispatch only works on first part of key binding
                return

            if mods & keymod:
                mods ^= keymod

            if mods == KeyMod.NONE:
                # single modifier
                if (node := search_node(self.root, (key,))) is None:
                    return
                if (match := find_active_match(node.root)):
                    self.active_key = key
                    if has_active_children(node.children):
                        # conflicts; exec after delay
                        self.timer = Timer(PRESS_HOLD_DELAY_MS / 1000, lambda: self.exec_press(match.command_id))
                        self.timer.start()
                    else:
                        # no conflicts; exec immediately
                        self.exec_press(match.command_id)
        else:
            # non-modifier base key
            components = keycombo2components(mods | key)
            if (node := search_node(self.root, self.prefix + components)) is None:
                return
            if (match := find_active_match(node.root)):
                if not self.prefix:
                    # first part of key binding, check for conflicts
                    if has_active_children(node.children):
                        return
            self.active_key = key
            self.active_mods = mods
            self.exec_press(match.command_id)

    def on_key_release(self, mods: KeyMod, key: KeyCode):
        if self.active_key == key:
            keymod = key2mod(key)

            if keymod is not None:
                # modifier base key
                if self.timer is not None:
                    # active timer, execute immediately
                    if not self.timer.finished.is_set():
                        # not already executed
                        self.timer.cancel()
                        self.exec_press(key)
                    self.timer = None
                    self.exec_release(key)
                    self.active_key = None
            else:
                # release segment of key binding
                self.exec_release(self.active_mods | self.active_key)
```

## Related Work

The entire key binding system is heavily influenced by [VSCode's keyboard shortcuts](https://code.visualstudio.com/docs/getstarted/keybindings), and to a lesser extent, [Emacs](https://www.gnu.org/software/emacs/manual/html_node/emacs/Key-Bindings.html) and [vim](https://vimdoc.sourceforge.net/htmldoc/map.html). However, as these are text editors and napari is not a text-based application, special casing had to be devised with regards to key bindings, such as handling both press and release events, and the additional conflicts that arose because of them.

## Implementation

- read and handle plugin key binding contributions (see [napari #5338](https://github.com/napari/napari/pull/5338))
- convert existing key bindings into actions that can be used by `app-model` (see [napari #5338](https://github.com/napari/napari/pull/5338))
- implement key binding resolution system as detailed in this NAP
- remove old action manager
- deprecate and translate key bindings set via `bind_key` for backwards compatibility (see below)

## Backward Compatibility

A change in the key binding dispatch system would affect anyone using `keymap` or `class_keymap` from the original `KeymapProvider`, as well as `bind_key` [^id3].

While `keymap` and `class_keymap` are unlikely to be commonly used, `bind_key` is, and thus will receive proper deprecation and continue to work by creating an equivalent entry in the new key binding dispatch system.

For example, following is how a user might have defined a key binding for an `Image` layer:
```python
@Image.bind_key('Control-C')
def foo(layer):
    ...
```

An entry would be created equivalent to:
```python
def wrapper(layer: Image):
    yield from foo(layer)

action = Action(id=foo.__qualname__, title=foo.__name__, callback=wrapper)
entry = KeyBindingEntry(command_id=foo.__qualname__, weight=KeyBindingWeight.USER, when=parse_expression("active_layer_type == 'image'"))

register_action(action)
register_key_binding('Ctrl+C', entry)
```

## Future Work

Future work may include key binding completion suggestions for key chords when the user inputs the first part of a binding.

Out of scope is work related to the GUI and how it may have to handle the new system.

## Alternatives

### Mapping approach

As opposed to the prefix tree approach, the key bindings could be stored in a map in integer form (as `KeyMod`, `KeyCode`, `KeyCombo`, and `KeyChord` are all `int`s):
```python
keymap = Dict[int, List[KeyBindingEntry]] = {
    KeyMod.CtrlCmd | KeyCode.KeyZ: ...,
    KeyMod.CtrlCmd | KeyMod.Shift | KeyCode.KeyZ: ...,
    KeyMod.CtrlCmd | KeyCode.KeyX: ...,
    KeyChord(KeyMod.CtrlCmd | KeyCode.KeyX, KeyCode.KeyC): ...,
    KeyChord(KeyMod.CtrlCmd | KeyCode.KeyX, KeyCode.KeyV): ...,
    KeyMod.Shift : ...,
}
```

To determine if an indirect conflict is present, entries would be filtered via bitwise operations:
```python
def has_shift(key: int) -> bool:
    return bool(key & KeyMod.Shift)

def starts_with_ctrl_cmd_x(key: int) -> bool:
    return key & 0x0000FFFF == (KeyMod.CtrlCmd | KeyCode.KeyX)

def multi_part(key: int) -> bool:
    return key > 0x0000FFFF

> list(filter(has_shift, keymap))
[<KeyCombo.CtrlCmd|Shift|KeyZ: 3115>, <KeyMod.Shift: 1024>]

> list(filter(starts_with_ctrl_cmd_x, keymap))
[
    <KeyCombo.CtrlCmd|KeyX: 2089>,
    KeyChord(<KeyCombo.CtrlCmd|KeyX: 2089>, <KeyCode.KeyC: 20>),
    KeyChord(<KeyCombo.CtrlCmd|KeyX: 2089>, <KeyCode.KeyV: 39>),
]

> list(filter(multi_part, keymap))
[
    KeyChord(<KeyCombo.CtrlCmd|KeyX: 2089>, <KeyCode.KeyC: 20>),
    KeyChord(<KeyCombo.CtrlCmd|KeyX: 2089>, <KeyCode.KeyV: 39>),
]
```

Note that because of the spec, querying for modifiers will only check the first part:
```python
> has_shift(KeyChord(KeyMod.CtrlCmd | KeyCode.KeyX, KeyMod.Shift | KeyCode.KeyY))
False
```

Putting this together:
```python
KEY_MOD_MASK = 0x00000F00
PART_0_MASK = 0x0000FFFF

def create_conflict_filter(conflict_key: int) -> Callable[[int], bool]:
    if conflict_key & KEY_MOD_MASK == conflict_key:
        # only comprised of modifier keys in first part
        def inner(key: int) -> bool:
            return key != conflict_key and key & conflict_key
    elif conflict_key <= PART_0_MASK:
        # one-part key sequence
        def inner(key: int) -> bool:
            return key > PART_0_MASK and key & PART_0_MASK == conflict_key
    else:
        # don't handle anything more complex
        def inner(key: int) -> bool:
            return NotImplemented

    return inner

def has_conflicts(key: int, keymap: Dict[int, List[KeyBindingEntry]]) -> bool:
    conflict_filter = create_conflict_filter(key)

    for _, entries in filter(conflict_filter, keymap.items()):
        if find_active_match(entries):
            return True
    
    return False
```

While this solution is undoubtedly more elegant, it has a much higher runtime complexity. Imagine that every possible valid key binding has at least one entry. Letting _K_ be the number of valid key codes, the amount of possible combinations for the first part of a key chord would be _16 * K_, plus 4 to include single modifiers. Combining this with the second part, it would be _(16 * K + 4)(16 * K)_, resulting in a conflict search runtime complexity of _O(n^2)_.

On the other hand, for a prefix tree, the amount of options for each node would be at most _K - D_, where _D_ is the depth of the node relative to the last completed part. When searching a key sequence with 4 modifiers for each part, the maximum number of options visited for one part would be _K + (K-1) + (K-2) + (K-3) + (K-4)_, or _2(5K-10)_ for two parts, resulting in a conflict search runtime complexity of _O(n)_.

Therefore, when searching for indirect conflicts, using a prefix-based data structure would be significantly more efficient than a mapping-based one, especially when an indirect conflict does not exist, since a mapping-based approach would potentially have to check every key in the map.

## Discussion

- **[April 19, 2023: napari #5747](https://github.com/napari/napari/issues/5747)** is opened, with discussion about what should be valid as a key binding. Arguments are made for the inclusion of single-modifier key bindings.

## Copyright

This document is dedicated to the public domain with the Creative Commons CC0
license [^id4]. Attribution to this source is encouraged where appropriate, as per
CC0+BY [^id5].

## References and Footnotes

[^id1]: napari #5103, <https://github.com/napari/napari/pull/5103>

[^id2]: napari #5747, <https://github.com/napari/napari/issues/5747>

[^id3]: KeymapProvider implementation, <https://github.com/napari/napari/blob/v0.4.17/napari/utils/key_bindings.py#L347C1-L369>

[^id4]: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication,
    <https://creativecommons.org/publicdomain/zero/1.0/>

[^id5]: <https://dancohen.org/2013/11/26/cc0-by/>