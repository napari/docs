# Autogenerate screenshots and videos from pre-recorded napari interactions

This folder contains scripts designed to automate the generation of screenshots
and videos from pre-recorded interactions with napari. It uses `pyautogui` and
`pynput` to record the screen and mouse interactions, exports the results to a
json file, and then generates screenshots and videos based on this data.

NOTE: Make sure the Qt version on your system is compatible with the PyQt version
you are using.

## Usage

To use these scripts, follow these steps:
1. **Install Dependencies**: Ensure you have the required Python packages installed. You can do this by running:
   ```bash
   pip install pyautogui pynput
   ```
2. **Install napari**: You probably want to have a [development installation of napari](hhttps://napari.org/stable/developers/contributing/dev_install.html).
3. **Record Interactions**: Use the `record_interactions.py` script to record your interactions with napari. This will
   a. Open a napari window,
   b. Record mouse and keyboard actions,
   c. Save the recorded actions to a JSON file named `recording.json`,
   d. Convert the recorded actions into a Python script named `play.py`.
   You can use `python record_interactions.py --help` to see the available options for naming output files.
4. Run python `play.py` to play back the actions.

## Attribution

These scripts are inspired by the code from https://github.com/shedloadofcode/mouse-and-keyboard-recorder
and its accompanying blog post at https://www.shedloadofcode.com/blog/record-mouse-and-keyboard-for-automation-scripts-with-python.
