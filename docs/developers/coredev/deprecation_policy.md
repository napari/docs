(napari-deprecation-policy)=

# Deprecation policy

This page states what napari promises when we change or remove public API, and
what plugin authors and downstream users can rely on. It is the entry point for
understanding how napari breaks things; the step-by-step mechanics of writing a
deprecation are in the [deprecation guide](napari-deprecation-guide).

```{note}
This policy is about *notice*. It does not prevent napari from making breaking
changes — it commits us to telling you about them in advance, on a schedule you
can plan around.
```

## What we promise

When napari changes or removes public API, we commit to:

1. **Warning you in code, where the runtime allows one.** Public API emits a
   warning when it is used, in the category that matches its state (see
   {ref}`napari-deprecation-states`). Surfaces that cannot warn — such as removals
   of support for a dependency — are announced and given a window instead.
2. **Publishing the removal window.** Every deprecation states the earliest
   window in which the API may be removed with search-friendly text.
3. **A minimum period of notice.** Two windows in most cases (see
   {ref}`napari-deprecation-minimum-notice`).

## Relationship to versioning

napari uses [EffVer](https://effver.org) and ships on a monthly cadence; see the
[release policy](napari-release) for the full schedule. Under EffVer, a deprecation
is *not* tied to a particular release type, which is a deliberate consequence of
this policy: **time-based windows exist precisely so that notice does not depend on
whether the next release turns out to be `macro` or `meso`.**

Removals still appear in release notes, and a release that removes deprecated API
is normally a larger-upgrade release, but you should not read a version number as a
promise about what was removed. Read the window instead.

(napari-deprecation-windows)=

## Deprecation windows

Deprecation windows are **quarters of a calendar year**, written as
`YYYY-QN` — for example `2027-Q2`. A window begins on:

| Window | Begins |
| --- | --- |
| `YYYY-Q1` | 1 January |
| `YYYY-Q2` | 1 April |
| `YYYY-Q3` | 1 July |
| `YYYY-Q4` | 1 October |

The format `YYYY-QN` should be used verbatim in the deprecation warning and in
the napari documentation, so a single search finds every deprecation and every
reference to a given window.

```{important}
A window is a **floor, not a ceiling**.

"May be removed as early as `2027-Q2`" means napari is permitted to remove the API
in any release from that window onward. It does **not** mean the API *will* be
removed in that window, and it does not mean the API will be removed at all. If we
choose not to remove something, we will re-window it (see
{ref}`napari-deprecation-lapsed`) rather than remove it quietly.
```

(napari-deprecation-minimum-notice)=

## Minimum notice

**Most deprecations get two windows** — if an API is deprecated during a given
quarter, it may first be removed from that quarter + 2, and thus is at least
six months of notice.

**Some deprecations get one window.** This is a fast track and it is only
available when a usage survey finds that plugins do not use the API in question.
See {ref}`napari-deprecation-survey`.

## What is covered

- **Public API** — anything documented in the [API reference](api) or
  described in our [usage documentation](usage).
- **Some undocumented names that plugins use.** While napari discourages developers
  from using private names, a few longstanding names are used by plugins,
  like `viewer._qt_viewer`. We will try to be mindful of these paths based on
  experience and issues opened by users and developers.
- **Behaviour and default changes.** If the *name* stays but the result changes,
  the same window applies. This matters more than it may appear: napari prioritises
  scientific accuracy, so a changed default can change what a researcher sees in
  their data and therefore is as important, if not more so, than a removed function
  because otherwise the change is silent.

(napari-deprecation-exempt)=

## What is exempt

The following do not go through this policy:

- **Security fixes.** A vulnerable or dangerously broken feature may be changed or
  removed without notice.
- **Genuinely internal code** — private names that are not part of any documented
  or plugin-facing surface.
- **Features that never worked**, provided nothing depends on the broken behaviour.
- **Features documented as experimental**, where the docstring says so. An
  experimental marker has to actually be in the documentation; it cannot be
  assumed.
- **Bug fixes that necessarily change behaviour.** These are exempt from the
  window, but *not* from disclosure: the change must appear in the release notes
  as a breaking change.

Judging whether a change is a bug fix or a breaking change is a judgement call. We
will make it in public, in the pull request, rather than silently.

## Dependency and platform support

Dropping support for a dependency or platform — a Qt binding, a Python version, a
NumPy version — cannot raise a `FutureWarning`, so it does not use a deprecation
warning. It does still get a **window**: support removals are announced at least
**two windows** ahead, so that a project which cannot move immediately knows when
it will be cut off. Supported versions of Python and scientific python libraries
follow, at minimum, [SPEC 0](https://scientific-python.org/specs/spec-0000/).

(napari-deprecation-states)=

## Deprecation states

napari recognises two states. Which state an API is in determines **which warning
category** it emits, and that category is what decides who sees it.

| State | Warning category | Who sees it | Window required? | Message must say |
| --- | --- | --- | --- | --- |
| **Hard** | `FutureWarning` | Everyone, including end users | **Yes** | "may be removed as early as `YYYY-QN`" |
| **Soft** | `DeprecationWarning` | Developers only — Python silences this category for library users, but pytest shows it | No | "there are no current plans to remove it" |

**Hard** states that an API is going away, and that it may be removed as early as the
window. **Soft** means an API we no longer recommend for new code but
**do not currently intend to remove**. It still warns, so developers are
informed, but the warning is quiet enough that end users are not troubled by
a removal that is not planned.

### Moving between states

| Transition | Allowed | Consequence |
| --- | --- | --- |
| soft → hard | Yes | **The clock restarts** — a full minimum notice, counted from the promotion |
| hard → soft | Yes | Must be recorded with a reason, exactly as a re-window is |

(napari-deprecation-survey)=

## Usage surveys

Before selecting a window, a deprecation must be supported by evidence about who
uses the API. In practice this means searching the napari plugin ecosystem for the
symbol and linking the search in the pull request. This is the same *impact
assessment* step that [NEP 23](https://numpy.org/neps/nep-0023-backwards-compatibility.html)
requires of NumPy deprecations.

The survey decides two things: whether the one-window fast track is available, and
which state is appropriate. An API that plugins use heavily is often a better
candidate for **soft** deprecation than for removal.

## How a deprecation is proposed

Deprecations are proposed like any other change, in a pull request, and reviewed by
the core team. A deprecation proposal should include:

- the API being deprecated and its replacement,
- the window, and the usage survey that justifies it,
- the state (hard or soft)

(napari-deprecation-lapsed)=

## When a window lapses

A window passing does not oblige anyone to act, but it does oblige someone to
*decide*. A window that has begun and has not been actioned is resolved at release
time in one of three ways:

1. **Remove it** and note the removal in the release notes.
2. **Re-window it** — declare a new window and record the reason. Re-windowing is
   permitted and is not a failure; doing it silently is.
3. **Demote it** to a soft deprecation, if we have concluded it will not be
   removed.

This process is meant to prevent a deprecation from being forgotten. It is not meant to force a removal.s
