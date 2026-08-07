# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "napari[all] @ git+https://github.com/napari/napari.git@main",
#   "napari-animation @ git+https://github.com/TimMonko/napari-animation.git@766dbbbcd0ec8607e67f49da0402ad41d4e512fb",
#   "ndevio",
# ]
# ///

"""Reproducible generation of the homepage video using napari-animation

This script uses the tribolium embryo dataset from the napari cloudflare storage.
It can be used as a remote source and the script will render cleanly using the remote
(despite the realtime qt blocking and cache limitations).
To download the Zarr locally (which offers much easier animation development), use:
`uv tool run ome_zarr download https://data.napari.dev/fluo-n3dl-trif-01.ome.zarr --output docs/_scripts`

The author mode opens napari with the dataset and timeline widget popped out.
If a timelime JSON already exists, it will be loaded.
Note that some things, like colormap and contrast_limits, were not settable in the
napari-animation version used to develop this timeline. So, there is the ability
to set various constants at the top to modify the script easier.
(The napari-animation branch used to develop this contains both Windows encoding fixes
and .webm encoding support.)

The render mode takes an existing timeline JSON and renders it to a movie file.
By default, this will save a webm -- be aware that this encoding can be quite slow to encode,
especially compared to the quick speed of mp4, but the file size ~10x smaller.
Both the timeline and output paths can be configured via command line arguments.

Usage:
`uv run docs/_scripts/homepage_video.py author`
`uv run docs/_scripts/homepage_video.py render`
`uv run docs/_scripts/homepage_video.py author --timeline path/to/timeline.json`
`uv run docs/_scripts/homepage_video.py render --timeline path/to/timeline.json --output path/to/movie.webm`
"""

from __future__ import annotations

import argparse
from pathlib import Path

import napari
from napari._qt.qt_event_loop import get_qapp

from napari_animation import AnimationTimelineWidget

SCRIPT_DIR = Path(__file__).resolve().parent
REMOTE_DATA_URL = 'https://data.napari.dev/fluo-n3dl-trif-01.ome.zarr'
LOCAL_DATA_PATH = SCRIPT_DIR / 'fluo-n3dl-trif-01.ome.zarr'
DEFAULT_TIMELINE_PATH = SCRIPT_DIR / 'homepage-timeline.json'
DEFAULT_OUTPUT_PATH = SCRIPT_DIR.parent / '_static' / 'images' / 'tribolium.webm'

PLUGIN = 'ndevio'
THEME = 'dark'
WINDOW_SIZE = (1204, 640)  # Will raise a an encoding block warning (needs // 16 size), but this is a reasonable size close to what it needs
TIMELINE_DOCK_AREA = 'bottom'
TIMELINE_FLOATING = True

LAYER_NAME = 'tribolium embryo'
CONTRAST_LIMITS = (0, 4500)
RENDERING = 'attenuated_mip'
ATTENUATION = 0.04
COLORMAP = 'magma'

RENDER_FPS = 20
RENDER_QUALITY = 5
RENDER_SCALE_FACTOR = 1.0
RENDER_CANVAS_ONLY = False


def build_viewer(*, show: bool) -> napari.Viewer:
    data_source = _resolve_data_source()
    print(f'Opening {data_source}')

    viewer = napari.Viewer(show=show)
    viewer.theme = THEME
    viewer.open(data_source, plugin=PLUGIN)
    layer = viewer.layers[0]
    layer.name = LAYER_NAME
    layer.contrast_limits = CONTRAST_LIMITS
    layer.contrast_limits_range = CONTRAST_LIMITS
    layer.rendering = RENDERING
    layer.attenuation = ATTENUATION
    layer.colormap = COLORMAP
    layer.histogram.enabled = True
    viewer.dims.axis_labels = ('T', 'Z', 'Y', 'X')
    viewer.scale_bar.visible = True
    viewer.floating_axes.visible = True
    viewer.window._qt_window.resize(*WINDOW_SIZE)
    viewer.fit_to_view()
    return viewer


def build_timeline_widget(
    viewer: napari.Viewer,
    *,
    timeline_path: Path | None,
    dock: bool,
) -> AnimationTimelineWidget:
    widget = AnimationTimelineWidget(viewer)
    if dock:
        dock_widget = viewer.window.add_dock_widget(
            widget,
            name='Animation Timeline',
            area=TIMELINE_DOCK_AREA,
        )
        dock_widget.setFloating(TIMELINE_FLOATING)
        if TIMELINE_FLOATING:
            dock_widget.show()
            dock_widget.raise_()
    if timeline_path is not None:
        widget.load_timeline(timeline_path)
    return widget


def _close_viewer(viewer: napari.Viewer) -> None:
    viewer.close()
    _flush_qt()


def author(args: argparse.Namespace) -> None:
    viewer = build_viewer(show=True)
    timeline_path = _resolve_timeline_path(args.timeline, required=False)
    build_timeline_widget(viewer, timeline_path=timeline_path, dock=True)
    napari.run()


def render(args: argparse.Namespace) -> None:
    viewer = build_viewer(show=True)
    timeline_path = _resolve_timeline_path(args.timeline, required=True)
    widget = build_timeline_widget(viewer, timeline_path=timeline_path, dock=False)
    _flush_qt()

    output_path = args.output.expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    viewer.screenshot(
        path=output_path.with_suffix('.png'),
        canvas_only=RENDER_CANVAS_ONLY,
    )
    widget.save_movie(
        filename=output_path,
        fps=RENDER_FPS,
        quality=RENDER_QUALITY,
        canvas_only=RENDER_CANVAS_ONLY,
        scale_factor=RENDER_SCALE_FACTOR,
    )
    _close_viewer(viewer)


def _flush_qt() -> None:
    app = get_qapp()
    if app is not None:
        app.processEvents()


def _resolve_data_source() -> str:
    if (LOCAL_DATA_PATH / 'zarr.json').exists():
        return str(LOCAL_DATA_PATH)
    return REMOTE_DATA_URL


def _resolve_timeline_path(path: Path, *, required: bool) -> Path | None:
    candidates = [path.expanduser()]
    if not path.is_absolute():
        candidates.append(SCRIPT_DIR / path)

    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved.exists():
            return resolved

    if required:
        checked = ', '.join(str(candidate.resolve()) for candidate in candidates)
        raise FileNotFoundError(f'Timeline JSON not found. Checked: {checked}')
    return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            'Author or render the napari homepage animation using either a '
            'local OME-Zarr next to this script or the remote URL.'
        )
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    author_parser = subparsers.add_parser(
        'author',
        help='Open napari with the homepage data and the timeline widget.',
    )
    author_parser.add_argument(
        'timeline',
        nargs='?',
        type=Path,
        default=DEFAULT_TIMELINE_PATH,
        help='Timeline JSON to load if it already exists.',
    )

    render_parser = subparsers.add_parser(
        'render',
        help='Render the saved homepage timeline to a movie file.',
    )
    render_parser.add_argument(
        'timeline',
        nargs='?',
        type=Path,
        default=DEFAULT_TIMELINE_PATH,
        help='Timeline JSON to render.',
    )
    render_parser.add_argument(
        'output',
        nargs='?',
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help='Movie path to write.',
    )

    return parser.parse_args()

def main() -> None:
    args = parse_args()
    if args.command == 'author':
        author(args)
    else:
        render(args)


if __name__ == '__main__':
    main()
