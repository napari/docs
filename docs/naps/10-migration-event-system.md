(nap-10-migration-event-system)=

# NAP-10 — Migration of the event system

```{eval-rst}
:Author: Wouter-Michiel Vierdag <michiel.vierdag@cellonautica.ai>
:Created: 2026-26-07
:Status: Draft
:Type: <Standards Track | Process>
```

## Purpose
Napari currently relies on several mechanisms for propagating information throughout the application, 
including _Qt signals_ and _slots_, _vispy_ events, _napari.utils.events_, and _psygnal_. 
These mechanisms are used interchangeably in different parts of the codebase, despite representing different 
concepts: some notify that state has changed, while others dispatch user interactions before any state change 
has occurred. As a result, application logic becomes coupled to backend-specific APIs and contributors must 
understand multiple communication models.

A key observation motivating this proposal is that not all communication in napari has the same semantics. 
State-change notifications (_signals_) and interaction dispatch (_events_ being dispatched, though not in the 
traditional sense of having one targeted receiver) serve different purposes and should not necessarily share 
the same abstraction.<br>
The goal is therefore not to replace every event with _psygnal_, but to establish a coherent application dispatch 
model with explicit semantics for signals, events, and the relationship between them. This document proposes an 
initial migration strategy rather than a fixed implementation plan. We expect to refine the design as experience 
is gained during implementation, documenting significant architectural decisions and any deviations from the 
original proposal.

![image](../_static/images/hang_the_code.gif)

## Terminology and concepts
Throughout this proposal, the terms _event_ and _signal_ are used in their architectural sense rather than according to 
napari's current implementation. The distinction is important because one of the goals of this migration is to 
clarify the semantics of communication throughout napari. Much of the confusion in previous discussions 
arose because the word _event_ has been used to describe both user interactions (such as mouse presses) and 
state-change notifications (such as layer properties changing), despite these representing fundamentally 
different concepts.

### _Events_ in _Qt_ terminology
_Events_ in the sense of _Qt_ are objects derived from `QEvent` (or one of its subclasses) that represent something 
that happened either inside an application or as a result of external activity that the application needs to 
respond to.
An event is delivered to a specific `QObject`, which acts as the intended receiver. Every `QObject` has an 
`event()` method that acts as a dispatcher: it does not normally handle the event itself, but routes it to 
the appropriate event handler such as `QObject.mousePressEvent()`, `QObject.keyPressEvent()`, or 
`QObject.paintEvent()`. An event handler is a method of a `QObject` subclass that contains the code responsible 
for responding to a particular type of event when it is delivered to that object.
If the handler accepts the event, Qt considers it handled. This means that the event is not propagated further. 
If it is ignored, Qt may attempt to propagate the event to another object, such as a parent widget.


```{mermaid}
flowchart TD
    A[External source<br/>Mouse / Keyboard / Timer / Application] --> B[Create QEvent object]

    B --> C[Event Queue]

    C --> D[Qt Event Loop]

    D --> E[Send event to target QObject]

    E --> F["QObject::event(QEvent*)"]

    F --> G{What type of event?}

    G -->|Mouse| H["mousePressEvent()<br/>mouseMoveEvent()"]
    G -->|Keyboard| I["keyPressEvent()<br/>keyReleaseEvent()"]
    G -->|Painting| J["paintEvent()"]
    G -->|Timer| K["timerEvent()"]

    H --> L{Accepted?}
    I --> L
    J --> L
    K --> L

    L -->|Yes| M[Event handled]
    L -->|No| N["Event ignored<br/>May propagate to parent"]

    M --> O[Qt continues event processing]
    N --> O
```
<br>
A Qt event is therefore a directed message with three important properties:

1. An event has a source
    - The operating system 
    - The Qt framework 
    - The application itself
2. An event has a target
    - A specific QObject 
    - Usually the widget under the mouse cursor, the widget with keyboard focus, etc.
3. Dispatch chain 
    - _Qt_ creates the event 
    - The event enters the event queue 
    - The event loop retrieves it 
    - _Qt_ sends it to the target object
    - _QObject.event()_ dispatches it to the appropriate handler 
    - The handler decides whether the event was handled

The key idea is:
A Qt event answers the question: "Something happened. Who should handle it?"

### Signals (Qt signals and slots)
Signals and slots are a different mechanism from events. 
- A __signal__ notification emitted by an object to announce that some observable state has changed. 
The emitter does not know, or need to know, which components are listening.
- A __slot__ is a function (or method) that is connected to a signal and is executed when that signal is emitted. A 
slot defines the action that should happen in response to a notification. It says "Perform this action when signal
happened".

The model looks like this:
```{mermaid}
flowchart TD
    A[Object changes state<br/>or something interesting happens] --> B[Object emits signal]

    B --> C[Signal]

    C --> D[Connected slot 1<br/>Callback function]
    C --> E[Connected slot 2<br/>Callback function]
    C --> F[Connected slot 3<br/>Callback function]
```
<br>

Unlike events:
- Signals do not have a single intended receiver.
- Signals can have zero, one, or many receivers.
- Signals are connected explicitly by the developer.
- Signals are not dispatched through `QObject.event()`.

The object emitting the signal does not need to know who is listening or what the listeners will do.

Now connecting a signal to a slot would look something like this:

```python
button.clicked.connect(save_file) # clicked is signal and save_file is the slot
```
Now `clicked` could also have other slots connected:

```{mermaid}
flowchart LR
    A[QPushButton] -->|emits| B[clicked signal]

    B --> C[save_file slot]

    B --> D[update_status slot]

    B --> E[other connected callbacks]
```
<br>

The button does not know:
- what save_file() does 
- how many listeners exist 
- whether anyone is listening at all

It just emits.

### _Signal_ / _slots_ vs _Events_
Although both mechanisms communicate information between components, they serve different purposes. 
_Events_ dispatch interactions to potential handlers, whereas _signals_ notify interested observers that state has 
already changed.

| | Qt Event | Qt Signal |
|---|---|---|
| __Meaning__ | Something happened | Notify observers about something |
| __Direction__ | One sender → one target | One sender → many receivers |
| __Receiver__ | Determined by Qt | Explicitly connected by programmer |
| __Routing__ | Event queue and event dispatcher | Signal-slot connection |
| __Handler__ | Event handler (`mousePressEvent`) | Slot / callback |
| __Propagation__ | Can be accepted, ignored, or propagated | No propagation |
| __Example__ | Mouse click, key press, paint event | Button clicked, value changed |

A dispatch mechanism determines how information flows between components. Both _events_ and _signals_ are 
dispatch mechanisms, but they have different semantics. 
_Event_ dispatch determines which component should respond to an interaction, potentially allowing handlers 
to consume or propagate it. Signal dispatch broadcasts that state has changed to any interested observers. 
The remainder of this proposal uses the term dispatch model to refer to the combination of these mechanisms 
that napari exposes at the application level.

### Current terminology in napari
By now it is perhaps already clear that napari is using terminology different from _Qt_ at the moment.
Most of the objects currently exposed through _napari.utils.events_ are semantically _signals_, despite 
being called _events_. They are emitted after state has changed, support multiple connected callbacks, 
and do not participate in event propagation or acceptance. In other words, they behave much more like 
_Qt signals_ than _Qt events_.
The example below showcasing a napari event that behaves like _signal_ -> _slot_ highlights this:

```python
layer.events.data.connect(callback)
```
This means that conceptually it looks like this:

```{mermaid}
flowchart TD
    A[Layer data changes] --> B[data changes]

    B --> C[layer.events.data]

    C -->|.connect| D[Viewer updates]

    C -->|.connect| E[Plugin reacts]

    C -->|.connect| F[Other listeners]
```

So in short, In napari terminology, an "event" is usually a state-change notification, which is much closer 
to a `QSignal` than a `QEvent`.<br>
Throughout the remainder of this proposal, the term _signal_ refers to state-change notifications, while _event_ 
refers to dispatching interactions that may be handled or propagated. This distinction reflects the intended 
semantics of the proposed architecture rather than the terminology used by the current implementation.

### Situation in envisioned rendering backend (_pygfx_)
For migration, it makes sense to look at how other rendering backends deal with events. From code in
_pygfx_ it is clear that the way _pygfx_ talks about events is very similar to the way _Qt_ talks about it.
This is clear from their docstring of the `Event` class:

```python
class Event:
    """Event base class.

    If a target is set, an event can bubble up through a hierarchy
    of targets, connected through a ``parent`` property.
    To prevent an event from bubbling up, use ``stop_propagation``.

    It is also possible to cancel events, which will stop any further
    handling of the event (also by the same target).

    Parameters
    ----------
    type : Union[str, EventType]
        The name of the event.
    bubbles : bool
        If True, the event bubbles up through the scene tree.
    target : EventTarget
        The object onto which the event was dispatched.
    root : RootEventHandler
        A reference to the root event handler.
    time_stamp : float
        The time at which the event was created (in seconds). Might not be an actual
        time stamp so please only use this for relative time measurements.
    cancelled : bool
        A boolean value indicating whether the event is cancelled.
    event_type : str
        Unused.
    """
```
<br>

Although the details differ slightly (for example, cancelled versus Qt's accepted state), the overall dispatch 
model is conceptually very similar to Qt's: events are dispatched to targets, may propagate, and may be consumed 
by handlers.

## Previous discussions
The ideas presented in this proposal have been discussed in various forms over several years, motivated 
by different but closely related goals including improved developer ergonomics, stronger static typing, 
backend independence, and simplification of napari's communication infrastructure. Although these discussions 
often focused on adopting _psygnal_, they collectively highlight a broader architectural need for a more coherent 
application dispatch model.

One of the earliest discussions arose from the migration of magicgui to _psygnal_ [#3373](https://github.com/napari/napari/issues/3373). That discussion 
highlighted the usability and maintainability benefits of replacing the dynamic __Event__ objects with 
explicit, typed signals. In particular, it noted that the current _napari.utils.events_ API relies heavily on 
dynamically generated event objects and `EmitterGroup`, making it difficult to discover available events, 
reason about callback signatures, provide IDE autocompletion, or perform static type checking. By contrast, 
_psygnal_ provides a _Qt_-like _signals_ and _slots_ API with explicit signal definitions, improved typing, 
and callback signatures that are immediately visible to users and developers.<br>
A second discussion, motivated by experiments replacing the _vispy_ canvas with a _pygfx_ backend 
[#7373](https://github.com/napari/napari/issues/7373), identified the event system as a key architectural obstacle to supporting multiple rendering 
backends. At present, many user interactions originate within _vispy_ before being propagated into napari, 
tightly coupling application behavior to a specific rendering backend. The discussion proposed that napari 
should instead own its application-level dispatch model, with rendering backends acting as integration layers 
that translate between backend-native communication mechanisms and napari's internal abstractions.<br> 
Building on these discussions, [@jacopoabramo](https://github.com/jacopoabramo) explored an initial prototype 
migration to _psygnal_ in [#8387](https://github.com/napari/napari/pull/8387), following an earlier discussion 
on Zulip. The prototype was primarily motivated by improving static typing across the codebase. It demonstrated 
that replacing `EmitterGroup` with explicit `psygnal.SignalGroup` definitions could provide significantly stronger 
typing and improve IDE support, although accommodating napari's inheritance hierarchy required additional typing 
protocols and highlighted several implementation challenges. The prototype also identified opportunities to 
simplify layer initialization, property setters, and event definitions. It was intentionally presented as an 
exploratory implementation rather than a mergeable solution, with the goal of informing future architectural 
discussions.

Finally, [#8509](https://github.com/napari/napari/pull/8509) demonstrated that _psygnal_-based models can 
coexist successfully within napari by migrating overlays from napari's custom `EventedModel` implementation 
to `psygnal.EventedModel`. Although limited in scope, this provided an initial proof of concept that parts 
of napari's event infrastructure can be migrated incrementally without requiring an immediate, project-wide 
transition.

# Rationale
The current communication infrastructure has served napari well, but it has become a significant source of 
architectural complexity. Today, napari uses several communication mechanisms simultaneously, including _Qt
signals_ and _slots_, _vispy_ events, _napari.utils.events_, and, in some places, _psygnal_. These mechanisms
are present throughout the codebase and represent different communication semantics, but there is currently no 
clear architectural distinction between them.<br>
As a result, contributors must understand multiple APIs with different connection patterns, callback signatures, and 
behaviors, while the napari application logic is often coupled directly to backend-specific communication mechanisms.
A key motivation for this migration is to establish a coherent application dispatch model for napari with explicit 
semantics for different types of communication. In particular, napari currently uses the term _event_ to describe
both state-change notifications and user interactions, despite these representing fundamentally different concepts.<br>
State changes, such as a layer's opacity changing or a layer being inserted, are naturally represented as _signals_: 
notifications that something has changed and that interested components may react. User interactions, such as mouse 
and keyboard input, are instead _events_: dispatched interactions that may require ordering, handling, propagation, 
or acceptance before application state is modified.<br>
The goal of this migration is therefore not to replace every event with _psygnal_, but to establish a clear 
separation between these concepts. _Psygnal_ provides the foundation for napari's internal signaling infrastructure, 
while backend-specific event systems such as those provided by _Qt_ and _vispy_ remain encapsulated where they are 
required. Rather than allowing GUI or rendering frameworks to define napari's application-level communication model, 
napari should own the interfaces between application components and treat backend-specific systems as implementation 
details at the boundaries of the architecture.<br>
Beyond the architectural benefits, the current _napari.utils.events_ implementation has several limitations when used 
for state-change notifications. These notifications are represented by dynamically constructed `Event` objects 
whose available attributes are determined at runtime, making them difficult to inspect, document, and type. 
Similarly, `EmitterGroups` are created dynamically, limiting IDE autocompletion and static analysis.<br>
In practice, many of these notifications have simple, well-defined signatures (for example, "opacity changed" 
or "layer inserted"), yet the current implementation obscures this information behind a generic event object.
_Psygnal_ provides a more explicit and familiar signaling model. Signals declare the values they emit, callback 
signatures are directly visible, and static type checkers and IDEs can infer the expected interfaces.
Many contributors are already familiar with the _Qt signals_ and _slots_ model, and _psygnal_ provides similar 
semantics in pure Python while remaining independent of any particular GUI framework.<br>
Finally, establishing a consistent application-level communication model will simplify the internal architecture 
and reduce the maintenance burden of supporting multiple overlapping abstractions. It will make communication 
pathways easier to reason about, improve static typing and documentation, and provide a clearer foundation for 
future work such as additional rendering backends.
While the migration represents a substantial effort, it provides an opportunity to modernize one of napari's core 
infrastructure components while preserving the semantics required by both state notifications and user 
interaction dispatch.
Please see below for a more concise display of the problems with the current communication model.

## The problem with the current communication model
Napari currently uses several different event systems throughout the codebase:
- the custom _napari.utils.events_ framework (derived from _vispy_)
- _vispy's_ event system
- _Qt signals_ and _slots_
- _psygnal_ (used in overlays)

As a result, different parts of napari communicate using different abstractions and are not translated 
into one signal / event model.
This has a number of consequences:

__Tight coupling to backend libraries__<br>
Much of napari's internal code is coupled directly to _Qt_ or _vispy_ because events are represented 
using their native mechanisms. This makes it difficult to separate application logic from rendering 
or UI concerns.

__Multiple programming models__<br>
Developers currently need to understand several different event APIs:
- _Qt signals_ and _slots_
- _vispy_ events
- _napari.utils.events_
- _psygnal_ (in case of overlays)

Each has different semantics, callback signatures, and connection patterns. This increases the cognitive
load for contributors and makes it harder to write reusable infrastructure.
Moving towards a single internal event abstraction reduces this complexity and makes behaviour more
consistent across the codebase.

__Threading__<br>
Napari already contains components that execute across different threads, including computational workloads and 
GUI-related components. However, threading behaviour is currently influenced by the specific event system being 
used rather than being managed consistently at the napari application level.
Different frameworks involved in napari's event handling have different assumptions and mechanisms for thread 
communication. For example, _Qt_ imposes strict thread-affinity rules for GUI objects, while _vispy_ has its own event 
handling model. As a result, code that emits or responds to events may need to be aware of backend-specific threading 
constraints, making event flow harder to reason about and increasing coupling between application logic and external 
libraries.

## Requirements of the implementation
There are a couple of things we would like to see from the implementation. These are here defined 
as guiding principles. Ultimately, some of these are not set in stone, but are meant to be guiding principles. 
Also, in case the guiding principles cannot be followed everywhere, there should be one central document describing 
why this was the case. The guiding principles:

1. __One event system__
Napari should have a single event mechanism for communication between internal components. <br>
While external libraries such as _Qt_ and _vispy_ may continue to expose their own native event systems, 
these should be treated as implementation details at the application boundary. Internal napari components 
should communicate through a common abstraction based on _psygnal_. This reduces the number of event models 
contributors need to understand and avoids coupling application logic to specific GUI or rendering frameworks.
2. __Backend agnostic__
The napari event model should not depend on the choice of GUI or rendering backend.<br>
Backends should translate their native events into napari events, and consume napari events where required, 
through clearly defined adapter layers. For example, a mouse event originating from _Qt_, _vispy_, or another 
future backend should be converted into a napari-defined signal rather than directly propagating through 
backend-specific APIs. This allows future backends to be integrated without requiring changes throughout 
the application codebase.
3. __Explicit and typed interfaces__
Event definitions should be explicit, discoverable, and statically analysable.<br>
_Signals_ should declare the values they emit (_psygnal_):
    ```python
    data = Signal(DataType)
    opacity = Signal(float)
    layers_changed = Signal(Layer)
    ```
    rather than relying on dynamically populated event objects (current system):
    ```python
    event.value
    event.source
    event.type
    ```
    This would improve:
    - type checking 
    - IDE autocompletion 
    - generated documentation 
    - developer understanding of APIs

    Where events require complex information, the payload should be represented by a well-defined Python type rather 
    than a dynamically modified event object.

4. __Separate event dispatch from event payloads__
The migration should distinguish between the mechanism used to deliver notifications and the data 
carried by those notifications.<br>
_Psygnal_ should provide the dispatch mechanism, while payload objects should represent domain-specific information. 
For example: Comment: not wanna do this with mouse event
   ```python
   mouse_press = Signal(MouseEvent)
   ```
   where _MouseEvent_ is a typed object containing information such as position, button, and modifiers.
This allows rich events to remain expressive while avoiding the limitations of the current dynamic 
_Event_ implementation.

5. __Preserve behaviour before improving APIs__
The migration should prioritize behavioral compatibility over immediate API redesign.<br>
Existing event semantics, including ordering, connection behavior, and lifecycle management, should be 
preserved where practical. Improvements to API clarity and typing should be introduced gradually through 
deprecation cycles. This reduces risk for users and plugin developers while allowing the underlying 
implementation to evolve.
6. __Make threading behavior explicit (not certain how achievable this is)(change documentation wise mostly)__
Event delivery across threads should have clearly defined semantics.<br>
Currently, GUI frameworks impose their own threading requirements, which can make event behaviour difficult 
to reason about when application logic, computation, and rendering operate on different threads.
The new event architecture should establish consistent rules for:
- emitting signals from worker threads 
- forwarding events to the GUI thread 
- interacting with backend-specific thread restrictions.<br>

   <br>Threading behaviour should be handled deliberately by the event infrastructure rather than being an implicit 
property of the backend. 
[_Psygnal_ docs](https://psygnal.readthedocs.io/en/latest/usage/?h=threa#connecting-across-threads) would be good to read for this.
7. __Minimise custom event infrastructure__
The migration should favour standard _psygnal_ abstractions over napari-specific event infrastructure.<br>
Wherever possible, functionality should be expressed using _Signal_, _SignalGroup_, and typed payload objects rather 
than introducing additional event abstractions. This reduces maintenance burden, simplifies the architecture, and 
makes the event system more familiar to contributors already accustomed to Qt's signals and slots.
8. __Focus on long term stability__
The event system is fundamental infrastructure used throughout napari and its plugin ecosystem.<br> 
Changes should favour simple, well-defined abstractions with stable semantics. This migration should establish 
an event architecture that can evolve without requiring repeated ecosystem-wide API changes.

## Proposed architecture
The proposed architecture establishes psygnal as the single event dispatch mechanism used throughout napari. 
Rather than application logic interacting directly with _Qt_, _vispy_, or other backend-specific event systems, 
napari owns a backend integration layer / adapter that translates between native backend events and napari's 
internal event model.<br>
Application components, including models, viewer state, user interactions etc., communicate exclusively through 
psygnal signals. Backend-specific event systems are confined to well-defined integration points (it is clear where 
backend ends and napari begins), allowing the rest of napari to remain independent of the underlying GUI or rendering 
framework.

Conceptually, the architecture becomes:

Create schematic!!!

Under this architecture:
- _psygnal.Signal_ and _SignalGroup_ become the primary mechanisms for event dispatch throughout napari.
- _EmitterGroup_ is replaced by explicit _SignalGroup_ definitions.
- State changes emit typed values directly (for example, _Signal(float)_ for an opacity change).
- Rich interaction events, such as mouse and keyboard events, are represented by strongly typed payload objects 
(e.g. _MouseEvent_ and _KeyEvent_) carried by psygnal signals rather than dynamically constructed _Event_ instances.
- _Qt_, _vispy_, and future backends remain responsible for their native event systems, but napari translates those 
events into its own event model through backend integration layers maintained within the napari codebase.

This architecture clearly separates napari's application logic from backend implementation details. Supporting a new 
rendering or GUI backend becomes a matter of implementing a new backend integration layer, rather than introducing 
another event system throughout the application.<br>
By adopting a single internal event abstraction, napari gains a more consistent programming model, improved static 
typing, clearer ownership of event flow, and a simpler foundation for future maintenance and development.

## Migration strategy
The migration should be incremental, allowing napari to move towards a single event system based on _psygnal_ 
while maintaining compatibility with existing internal code and external users where possible.

A full replacement of _napari.utils.events_ in a single step would introduce a large and difficult-to-review change, 
with a high risk of breaking behaviour across models, GUI components, rendering, and plugins. Instead, the 
migration should proceed component-by-component, prioritising internal infrastructure first and delaying public 
API changes until the underlying architecture has stabilised. Lorenzo’s work on overlays could be used as an example 
(reemitting events: code [here](https://github.com/napari/napari/blob/1f5d993eb55c93c3bb56d73861cc1f09f481ccc5/src/napari/utils/events/containers/_evented_dict.py#L126-L135))

The migration should follow the principles outlined previously.

__Backward compatibility__<br>
During the transition period, a compatibility layer will likely be required to bridge between the existing 
event system and _psygnal_. The compatibility layer should allow existing callbacks and event consumers to 
continue functioning while new components adopt _psygnal_. This may include:
- translating legacy _Event_ objects into typed signal payloads
- providing temporary wrappers around existing event groups / reemitting events
- supporting deprecated callback signatures during a migration period
- emitting deprecation warnings when legacy APIs are used

The compatibility layer should be considered temporary infrastructure. Its purpose is to enable gradual migration, 
not to maintain two event systems indefinitely.

__Migration order__<br>
Migration should proceed from lower-level infrastructure towards higher-level components.
A possible order is (which I by no means claim is the right order):
 Comment: first provide psygnalmodel to psygnal

1. __Core event infrastructure__<br>
Replace or adapt the foundations of the current event system:
- _Event_
- _EventEmitter_
- _EmitterGroup_
- event-related utility classes

Define the preferred psygnal patterns, naming conventions, and backward compatibility mechanisms.

2. __Evented models and core state__<br>
Migrate model classes that are involved with communicating napari state:
- _EventedModel_
- _Layers_ (await refactor)
- _ViewerModel_
- _Dimensions_
- _Camera_
- _Selections_
- Other 

   <br>The main reason for starting here is because I think these are good candidates because they might 
be more predictable.

3. __GUI and plugin facing components__<br>
Update components that consume model events:
- _Qt_ widgets 
- menus and actions 
- plugin-facing APIs 
- commands and controllers

   <br>At this stage, the majority of napari's application logic should communicate through _psygnal_.

4. __Backend integration layers__ (need to do this completely different)<br>
Move backend-specific event handling behind napari-owned adapters.
This includes:
- translating _Qt_ input events into napari signals 
- translating _vispy_ interaction events into napari signals 
- supporting future rendering backends through the same mechanism.

   <br>The goal is that backend implementations no longer define the event flow used by the rest of napari. 
One important aspect here I believe should be that this really needs to be benchmarked. Given the high 
right of event firing I expect that aspect here to be more crucial than with changing the events for the 
other components.

5. __Legacy API deprecation and removal__<br>
Once internal usage has been migrated:
- document the new event API
- provide migration guidance for plugin authors
- Deprecate legacy code
- remove compatibility layers after an appropriate transition period

   <br>some of the documentation might be created and published earlier, particularly developer facing 
	documentation as they need to be aware of the changes at an earlier stage.

## Success criteria
The migration will be considered successful when:
- napari has one primary internal event system based on _psygnal_
- application logic no longer depends directly on _Qt_ or _vispy_ event mechanisms 
- backend-specific events are handled through napari-owned integration layers 
- event definitions are explicit, typed, and discoverable 
- plugin developers have a documented migration path 
- the legacy event infrastructure can be removed / will not break napari internals 
- threading and event delivery semantics are clearly documented 
- supporting additional GUI or rendering backends does not require introducing new event abstractions

## Open questions
Several open ended questions around design should be put here.

## Immediate action points
Add glossary for people to understand difference between events / signals

## Points of contention
Things we are not sure about and have different opinion on.
