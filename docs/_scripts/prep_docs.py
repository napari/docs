"""ALL pre-rendering and pre-preparation of docs should occur in this file.

Note: make no assumptions about the working directory
from which this script will be called.
"""
import sys
from pathlib import Path

DOCS = Path(__file__).parent.parent.absolute()
NPE = DOCS.parent.absolute() / 'npe2'

def prep_npe2():
    #   some plugin docs live in npe2 for testing purposes
    from subprocess import check_call

    check_call(f"rm -rf {NPE}".split())
    check_call(f"git clone https://github.com/napari/npe2 {NPE}".split())
    check_call([sys.executable, f"{NPE}/_docs/render.py", DOCS / 'plugins'])
    check_call(f"rm -rf {NPE}".split())


def main():
    prep_npe2()
    __import__('update_preference_docs').main()
    __import__('update_event_docs').main()
    __import__('update_ui_sections').main()


if __name__ == "__main__":
    main()
