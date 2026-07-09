(napari-message-routing)=

# Notifications, warnings, and logging

napari exposes several ways to surface problems and status to users and
developers. The right route depends on whether the current operation should
fail, whether the condition has already been handled, and whether the message
needs to exist outside the GUI.

## Choose the route

- Let real exceptions propagate by default. This is the normal path for bugs,
  invalid state, and operations that should fail.
- Use `show_info()`, `show_warning()`, or `show_error()` for explicit
  user-facing messages after your code has already handled the condition.
- Use `warnings.warn()` for Python warning semantics, especially deprecations
  and library-style warnings that should still exist in tests, scripts, and
  headless usage.
- Use logging for developer diagnostics and post-hoc debugging, not as the
  main user-facing channel.

In a running napari session, uncaught exceptions are surfaced with traceback
UI. If you catch an exception and convert it to `show_error(str(exc))` or
`warnings.warn(str(exc))`, you are intentionally choosing a different route and
losing that traceback experience.

## Catching exceptions without losing the traceback UI

Catch an exception only when you can recover, return a fallback value, or
replace a misleading higher-level failure with a more accurate one.

If you catch a real exception but still want napari's traceback popup, forward
the original exception with `notification_manager.receive_error(...)`:

```python
from napari.utils.notifications import notification_manager


def run_plugin_action():
    try:
        raise ValueError("Bad user input")
    except ValueError as exc:
        notification_manager.receive_error(
            type(exc), exc, exc.__traceback__
        )
        return None
```

## Warnings are not a guaranteed GUI message channel

Repeated identical Python warnings are not a reliable way to communicate with
the viewer UI. Python warning filters apply first, and while napari's warning
hook is installed, repeated warnings from the same call site are deduplicated.

Default visibility also matters:

- `DeprecationWarning` is hidden by Python's default CLI warning filters.
- `UserWarning` is shown by default in the CLI.
- In napari, warnings may also appear as viewer notifications while the warning
  hook is installed, but that is not guaranteed before the window is visible.
- If you need a guaranteed viewer-side message, use `show_warning()` rather
  than relying on `warnings.warn()`.

## Set `stacklevel` deliberately

When you call `warnings.warn()`, set `stacklevel` so the warning points at the
code that should change.

- `stacklevel=2` is usually right when a public function or method warns
  directly.
- Increase it to `3` or more when the warning is emitted from a helper,
  wrapper, descriptor, or decorator and you want the warning to land on the
  external caller.
- Check the rendered warning location in a real call site rather than assuming
  `2` is always correct.

## Practical patterns

Use Python warnings for deprecations and other API-style warnings:

```python
import warnings


def old_function():
    warnings.warn(
        "old_function() is deprecated; use new_function() instead",
        DeprecationWarning,
        stacklevel=2,
    )
```

Use napari notifications for explicit GUI-visible user messages:

```python
from napari.utils.notifications import show_warning


def export_with_defaults(path):
    show_warning("No output path was chosen; using the default export location.")
```

Use logging for developer diagnostics and log review:

```python
import logging


logger = logging.getLogger(__name__)


def recompute_preview(shape):
    logger.debug("Recomputing preview for shape %s", shape)
```

You can inspect logs in a running viewer via **Help > Show logs**.