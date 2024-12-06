import sys
import json


def update_version_switcher(new_version):
    """Update version_switcher.json after a new release."""
    with open("docs/_static/version_switcher.json", "r") as f:
        switcher = json.load(f)
    oldstable = switcher[1]

    newstable = oldstable.copy()
    newstable["version"] = new_version
    newstable["name"] = f"stable ({new_version})"

    oldstable["name"] = f"{oldstable['version']}"
    del oldstable["preferred"]
    oldstable["url"] = oldstable["url"].replace("stable", oldstable["version"])

    switcher[1] = oldstable
    switcher.insert(1, newstable)
    with open("docs/_static/version_switcher.json", "w") as f:
        json.dump(switcher, f, indent=4)

    print(f"Version switcher updated to {new_version}")
    print(f"Old stable version: {switcher[2]}")
    print(f"New stable version: {switcher[1]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_switcher.py <new_version>")
        sys.exit()
    new_version = sys.argv[1]
    update_version_switcher(new_version)
