"""Print the napari examples folder to use as the gallery source.

Used by the Makefile when ``GALLERY_PATH`` is not given. If napari is an
editable install (for example in the ``local-napari`` pixi workspace), the
``examples`` folder of that checkout is used, so the gallery always matches the
napari the docs are built against. The path is printed relative to
``docs/``, which is what the Makefile expects.

Prints nothing if napari is not importable or not installed from a source
checkout; the Makefile then falls back to its default.
"""

import importlib.util
import os
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parents[1]


def find_examples() -> Path | None:
    # find_spec locates the package without importing it, which keeps this fast
    spec = importlib.util.find_spec('napari')
    if spec is None or not spec.submodule_search_locations:
        return None
    pkg_dir = Path(next(iter(spec.submodule_search_locations))).resolve()
    # src layout: <repo>/src/napari; flat layout: <repo>/napari
    for repo in pkg_dir.parents[:2]:
        if (repo / 'pyproject.toml').is_file() and (repo / 'examples').is_dir():
            return repo / 'examples'
    return None


def main() -> None:
    examples = find_examples()
    if examples is None:
        return
    try:
        path = os.path.relpath(examples, DOCS_DIR)
    except ValueError:  # different drive on Windows
        path = str(examples)
    print(Path(path).as_posix())


if __name__ == '__main__':
    main()
