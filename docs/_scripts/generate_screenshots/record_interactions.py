"""
Opens a napari window and records mouse and keyboard interactions to a JSON file

To begin recording:
- Run `python record.py`

To end recording:
- Hold right click for 2 seconds then release to end the recording for mouse.
- Press 'ESC' to end the recording for keyboard.
- Both are needed to finish recording.
"""

import time
import json
import napari
import platform
import argparse
from pynput import mouse, keyboard


class InteractionRecorder:
    def __init__(self, output_file="recording.json"):
        self.recording = []
        self.output_file = output_file
        self.keyboard_listener = None
        self.mouse_listener = None
        self.viewer = None

    def on_press(self, key):
        try:
            json_object = {"action": "pressed_key", "key": key.char, "_time": time.time()}
        except AttributeError:
            if key == keyboard.Key.esc:
                print("Keyboard recording ended.")
                self.stop_recording("keyboard")
                return False

            json_object = {"action": "pressed_key", "key": str(key), "_time": time.time()}

        self.recording.append(json_object)

    def on_release(self, key):
        try:
            json_object = {"action": "released_key", "key": key.char, "_time": time.time()}
        except AttributeError:
            json_object = {"action": "released_key", "key": str(key), "_time": time.time()}

        self.recording.append(json_object)

    def on_move(self, x, y):
        if len(self.recording) > 1:
            if (
                self.recording[-1]["action"] == "pressed"
                and self.recording[-1]["button"] == "Button.left"
            ) or (
                self.recording[-1]["action"] == "moved"
                and time.time() - self.recording[-1]["_time"] > 0.02
            ):
                json_object = {"action": "moved", "x": x, "y": y, "_time": time.time()}
                self.recording.append(json_object)

    def on_click(self, x, y, button, pressed):
        json_object = {
            "action": "clicked" if pressed else "unclicked",
            "button": str(button),
            "x": x,
            "y": y,
            "_time": time.time(),
        }

        self.recording.append(json_object)

        if len(self.recording) > 2:
            if (
                self.recording[-1]["action"] == "unclicked"
                and self.recording[-1]["button"] == "Button.right"
                and self.recording[-1]["_time"] - self.recording[-2]["_time"] > 2
            ):
                self.save_recording()
                print("Mouse recording ended.")
                self.stop_recording("mouse")
                return False

    def on_scroll(self, x, y, dx, dy):
        json_object = {
            "action": "scroll",
            "vertical_direction": int(dy),
            "horizontal_direction": int(dx),
            "x": x,
            "y": y,
            "_time": time.time(),
        }

        self.recording.append(json_object)

    def save_recording(self):
        """Save the recorded interactions to a JSON file."""
        with open(self.output_file, "w") as f:
            json.dump(self.recording, f)
        print(f"Recording saved to {self.output_file}")

    def start_recording(self):
        """Creates a napari window and starts recording mouse and keyboard interactions."""
        napari.Viewer.close_all()
        # Open napari with standard window size (800x600)
        self.viewer = napari.Viewer()
        self.viewer.window._qt_window.setGeometry(0, 0, 800, 600)

        # Reset recording for this session
        self.recording = [{
            "metadata": {
                "start_time": time.time(),
                "napari_version": napari.__version__,
                "python_version": platform.python_version(),
                "os": platform.system()
            }
        }]

        print("Press 'ESC' to end the keyboard recording")
        print("Hold right click for 2 seconds then release to end the mouse recording")

        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.mouse_listener = mouse.Listener(
            on_click=self.on_click,
            on_scroll=self.on_scroll,
            on_move=self.on_move
        )

        self.keyboard_listener.start()
        self.mouse_listener.start()

        # Show the napari window
        napari.run()

        # Wait for listeners to finish
        self.keyboard_listener.join()
        self.mouse_listener.join()

    def stop_recording(self, mode: str):
        """Stop the recording and save the data.

        Args:
            mode (str): The mode of recording ("mouse" or "keyboard").
        """
        if self.keyboard_listener and mode == "keyboard":
            self.keyboard_listener.stop()
        if self.mouse_listener and mode == "mouse":
            self.mouse_listener.stop()

        if not self.keyboard_listener.running and not self.mouse_listener.running:
            self.save_recording()
            # if self.viewer:
            #     self.viewer.close()
            print("Recording stopped. Please close the napari window.")


def read_json_file(json_input: str) -> tuple:
    """
    Takes the JSON output 'recording.json'

    Excludes released and scrolling events to
    keep things simple.
    """
    with open(json_input) as f:
        recording = json.load(f)
    metadata = recording.pop(0)

    def excluded_actions(object):
        return "released" not in object["action"] and "scroll" not in object["action"]

    recording = list(filter(excluded_actions, recording))

    return metadata, recording


def convert_recording(json_input: str, output_file: str = "play.py"):
    """Converts the recorded interactions from JSON to a Python script using pyautogui.

    Converts the:

    - Mouse clicks
    - Keyboard input
    - Time between actions calculated

    Args:
        json_input (str): The path to the JSON file containing the recorded interactions.
        output_file (str): The name of the output Python script file.
    """

    key_mappings = {
        "cmd": "win",
        "alt_l": "alt",
        "alt_r": "alt",
        "ctrl_l": "ctrl",
        "ctrl_r": "ctrl",
    }

    metadata, recording = read_json_file(json_input)

    if not recording:
        return

    output = open(output_file, "w")
    output.write(f"# {metadata}\n")
    output.write("import time\n")
    output.write("import pyautogui\n\n")
    output.write("# Open napari with standard window size (800x600)\n")
    output.write("self.viewer = napari.Viewer()\n")
    output.write("self.viewer.window._qt_window.setGeometry(0, 0, 800, 600)\n")

    for i, step in enumerate(recording):
        print(step)

        not_first_element = (i - 1) > 0
        if not_first_element:
            ## compare time to previous time for the 'sleep' with a 10% buffer
            pause_in_seconds = (step["_time"] - recording[i - 1]["_time"]) * 1.1

            output.write(f"time.sleep({pause_in_seconds})\n\n")
        else:
            output.write("time.sleep(1)\n\n")

        if step["action"] == "pressed_key":
            key = (
                step["key"].replace("Key.", "")
                if "Key." in step["key"]
                else step["key"]
            )

            if key in key_mappings.keys():
                key = key_mappings[key]

            output.write(f"pyautogui.press('{key}')\n")

        if step["action"] == "clicked":
            output.write(f"pyautogui.moveTo({step['x']}, {step['y']})\n")

            if step["button"] == "Button.right":
                output.write("pyautogui.mouseDown(button='right')\n")
            else:
                output.write("pyautogui.mouseDown()\n")

        if step["action"] == "unclicked":
            output.write(f"pyautogui.moveTo({step['x']}, {step['y']})\n")

            if step["button"] == "Button.right":
                output.write("pyautogui.mouseUp(button='right')\n")
            else:
                output.write("pyautogui.mouseUp()\n")

    print(f"Recording converted. Saved to '{output_file}'")


def start_recording(json_output: str = "recording.json"):
    """Creates a napari window and starts recording mouse and keyboard interactions.

    Args:
        output (str): The name of the output JSON file to save the recording.
    """
    recorder = InteractionRecorder(json_output)
    recorder.start_recording()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Record mouse and keyboard interactions in a napari window.",
        epilog="Use --json-output to specify the temporary json output file name. Use --output to specify the output Python script file name."
    )
    parser.add_argument(
        "--json-output",
        type=str,
        nargs='?',
        default="recording.json",
        help="Output JSON file name"
    )
    parser.add_argument(
        "--output",
        type=str,
        nargs='?',
        default="play.py",
        help="Output Python script file name (default: play.py)"
    )
    parser.add_argument(
        "--no-convert",
        action='store_true',
        help="Do not convert the recording to a Python script after recording"
    )
    args = parser.parse_args()
    start_recording(args.json_output)
    if not args.no_convert:
        convert_recording(args.json_output, args.output)
