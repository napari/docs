# Autogenerate screenshots and videos from pre-recorded napari interactions

This folder contains scripts designed to automate the generation of screenshots
and videos from pre-recorded interactions with napari. It uses `pyautogui` and
`pynput` to record the screen and mouse interactions, exports the results to a
json file, and then generates screenshots and videos based on this data.

## Usage

To use these scripts, follow these steps:
1. **Install Dependencies**: Ensure you have the required Python packages installed. You can do this by running:
   ```bash
   pip install pyautogui pynput
   ```
2. **Launch napari**: Start napari in a separate terminal or environment. Ensure it is running and ready to accept interactions.
3. **Record Interactions**: Use the `record.py` script to record your interactions with napari. This will create a JSON file containing the recorded mouse and keyboard events.
4. **Convert to Screenshots**: Use the `convert.py` script to convert the recorded interactions into screenshots. This will generate a series of PNG files in the `screenshots` directory.
5. The conversion will be saved as `play.py`. Run python play.py to play back the actions

## Attribution

These scripts are inspired by the code from https://github.com/shedloadofcode/mouse-and-keyboard-recorder
and its accompanying blog post at https://www.shedloadofcode.com/blog/record-mouse-and-keyboard-for-automation-scripts-with-python.
