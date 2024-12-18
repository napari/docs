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
                self.stop_recording()
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
        if len(self.recording) >= 1:
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

        if len(self.recording) > 1:
            if (
                self.recording[-1]["action"] == "unclicked"
                and self.recording[-1]["button"] == "Button.right"
                and self.recording[-1]["_time"] - self.recording[-2]["_time"] > 2
            ):
                self.save_recording()
                print("Mouse recording ended.")
                self.stop_recording()
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
        self.recording = []

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

    def stop_recording(self):
        """Stop the recording and save the data."""
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        if self.mouse_listener:
            self.mouse_listener.stop()
        self.save_recording()

        if self.viewer:
            self.viewer.close()


def start_recording(output: str = "recording.json"):
    """Creates a napari window and starts recording mouse and keyboard interactions.

    Args:
        output (str): The name of the output JSON file to save the recording.
    """
    recorder = InteractionRecorder(output)
    recorder.start_recording()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Record mouse and keyboard interactions in a napari window."
    )
    parser.add_argument(
        "output",
        type=str,
        nargs='?',
        default="recording.json",
        help="Output JSON file name"
    )
    args = parser.parse_args()
    start_recording(args.output)
