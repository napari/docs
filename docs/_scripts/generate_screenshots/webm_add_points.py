# This script generates the video for the points layer tutorial.

# Before running, make sure to:
# 1. Install napari in development mode from the main branch
# 2. Run `napari --reset`

# To generate the video, install pyautogui and run:
# python webm_add_points.py

from pyautogui import click, alert, locateCenterOnScreen, moveTo, dragTo, screenshot
import numpy as np
from qtpy import QtCore
from skimage import data
from qtpy.QtWidgets import QApplication
import napari
import time


def apply_event(app, event, loc, msg=""):
    duration = 0.3
    if event == "click_button":
        button = locateCenterOnScreen(loc)
        click(button, duration=duration)
    if event == "click":
        click(*loc, duration=duration)
    if event == "move":
        moveTo(*loc, duration=duration)
    if event == "drag":
        dragTo(*loc, button="left", duration=duration)
    app.processEvents()
    print(msg)
    app.processEvents()


def run_actions():
    # Function that will be triggered from QTimer to run code even when running
    # `napari.run`
    print("Initial screenshot")
    app = QApplication.instance()
    time.sleep(1)
    print("Done")

    # 1. Click add points icon
    # Locate coordinates for the `Add points` buttons by using a image of the
    # button
    apply_event(
        app,
        "click_button",
        "../../images/point-adding-tool.png",
        msg="Click add points icon",
    )

    # 2. Add three new points
    apply_event(app, "click", (700, 400), msg="Click add point 1")
    apply_event(app, "click", (750, 200), msg="Click add point 2")
    apply_event(app, "click", (650, 300), msg="Click add point 3")

    # 3. Click select points icon
    apply_event(
        app,
        "click_button",
        "../../images/point-selecting-tool.png",
        msg="Click select points icon",
    )

    # 4. Select two points individually
    apply_event(app, "click", (750, 200), msg="Click select point 1")
    apply_event(app, "click", (650, 300), msg="Click select point 2")

    # 5. Drag mouse to select group of points
    apply_event(app, "move", (400, 100), msg="Move to selection start")
    apply_event(app, "drag", (600, 300), msg="Drag and select")

    # 6. Change face color
    apply_event(app, "move", (150, 240), msg="Move to face color selection")
    apply_event(app, "click", (150, 240), msg="Click face color selection")
    apply_event(app, "click", (200, 240), msg="Click face color grid")
    apply_event(app, "click_button", "../../images/ok.png", msg="Click OK")

    # 7. Change edge color
    apply_event(app, "move", (150, 270), msg="Move to edge color selection")
    apply_event(app, "click", (150, 270), msg="Click edge color selection")
    apply_event(app, "click", (220, 310), msg="Click edge color grid")
    apply_event(app, "click_button", "../../images/ok.png", msg="Click OK")

    # 8. Select group of points with different colors
    apply_event(app, "move", (400, 200), msg="Move to selection start")
    apply_event(app, "drag", (600, 400), msg="Drag and select")

    # 9. Use slider to increase point size
    apply_event(app, "move", (175, 155), msg="Move to point size slider")
    apply_event(app, "drag", (210, 155), msg="Drag slider")

    # 10. Select a group of points, click symbol dropdown and select cross
    apply_event(app, "move", (480, 215), msg="Move to selection start")
    apply_event(app, "drag", (680, 345), msg="Drag and select")
    apply_event(app, "click", (295, 200), msg="Click symbol dropdown")
    apply_event(app, "click", (295, 170), msg="Click cross symbol")

    # 11. Use slider to decrease and increase opacity
    apply_event(app, "move", (270, 132), msg="Move to opacity slider")
    apply_event(app, "drag", (180, 132), msg="Drag slider down")
    apply_event(app, "drag", (270, 132), msg="Drag slider up")

    # 12. Select point and click the "delete selected points" icon
    apply_event(app, "click", (440, 380), msg="Select one point")
    apply_event(app, "click_button", "../../images/point-deleting-tool.png", msg="Delete point")

    # 13. Click the add points icon
    apply_event(app, "click_button", "../../images/point-adding-tool.png", msg="Click add points icon")

    # 14. Use the face color dropdown to select a different color
    apply_event(app, "click", (150, 240), msg="Click face color selection")
    apply_event(app, "click", (310, 180), msg="Click face color grid")
    apply_event(app, "click_button", "../../images/ok.png", msg="Click OK")

    # 15. Use the slider to increase point size and add new points
    apply_event(app, "click", (210, 155), msg="Click point size slider")
    apply_event(app, "drag", (170, 155), msg="Drag slider down")
    apply_event(app, "click", (500, 500), msg="Click add point")
    apply_event(app, "move", (800, 600), msg="Move mouse")

    screenshot("fallback.png")


viewer = napari.Viewer()
viewer.window.set_geometry(0, 0, 800, 600)
viewer.add_image(data.astronaut(), rgb=True)
points = np.array([[100, 100], [200, 200], [300, 100]])
points_layer = viewer.add_points(points, size=30)
# Wait a bit so that the user has time to move the app to the foreground
print("Make sure the qt app is in the foreground... waiting 3s to trigger actions")
QtCore.QTimer.singleShot(3000, run_actions)

print("Launched napari")
napari.run()
