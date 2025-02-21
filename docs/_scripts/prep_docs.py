"""ALL pre-rendering and pre-preparation of docs should occur in this file.

This script is called **before** Sphinx builds the documentation.

Note: make no assumptions about the working directory
from which this script will be called.
"""

import sys
from importlib.metadata import version
from pathlib import Path

from packaging.version import parse

# Set up paths to docs and npe2 docs source
DOCS = Path(__file__).parent.parent.absolute()
print(DOCS)
NPE = DOCS.parent.absolute() / "npe2"
print(NPE)


def prep_npe2():
    """Preps the npe2 plugin engine prior to Sphinx docs build.

    Some plugin-related docs live in the npe2 repo to simplify
    plugin testing.
    """
    print("Entered prep_npe2")
    #  Checks if the path to npe2 repo exist. If so, bail.
    if NPE.exists():
        print("npe2 is already installed. moving on")
        return
    from subprocess import check_call

    npe2_version = version("npe2")
    print(f"npe2 version: {npe2_version}")
    check_call(f"rm -rf {NPE}".split())
    print("removing NPE directory succeeded")
    check_call(f"git clone https://github.com/napari/npe2 {NPE}".split())

    if not parse(npe2_version).is_devrelease:
        check_call(f"git checkout tags/v{npe2_version}".split(), cwd=NPE)

    check_call([sys.executable, f"{NPE}/_docs/render.py", DOCS / "plugins"])
    check_call(f"rm -rf {NPE}".split())


def main():
    prep_npe2()
    __import__("update_preference_docs").main()
    print("update_preference_docs succeeded")
    __import__("update_event_docs").main()
    print("update_event_docs succeeded")
    __import__("update_ui_sections_docs").main()
    print("update_ui_sections_docs succeeded")


if __name__ == "__main__":
    main()
