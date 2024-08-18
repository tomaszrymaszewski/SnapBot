# Automated Snap Sending Script

This Python script automates the process of sending snaps through the Snapchat web app using the `pyautogui` library. It allows you to send a specified number of snaps by simulating mouse movements and clicks on predetermined screen coordinates. 

## Installation

1. Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. Install the `pyautogui` library using pip:

## Usage

1. Log into Snapchat on the CHROME browser.

2. Modify the coordinates (the ones provided work on a MacBook Pro)

3. Press on the camera icon on the send Snap area so that you can see your camera feed (I would suggest covering your webcam)

4. Run `main.py`

5. Make sure the Snapchat window is in the foreground. The script will automatically move the mouse and send the snaps.

## Notes

- **Screen Resolution**: The script relies on specific screen coordinates, so it may not work correctly if your screen resolution or browser window size changes. Determine the coordinates by e.g. downloading an app (idk). On a Mac you can just press CMD + SHIFT + 4 to start taking a screenshot of a part of the screen and you see the coordinates next to the cursor. 
- **Testing**: Test the script with a small number of snaps to ensure it works as expected before using it for a larger number.

---

This script is a simple automation tool and is intended for educational purposes. Modify and use it at your own risk. 🫣
