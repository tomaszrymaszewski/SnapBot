import pyautogui  # pip install pyautogui
import time
from random import uniform

NO_OF_SNAPS = 100  # number of snaps you want to send

# Define the positions (x, y) on the screen for the cursor to move to
locations = [
    (745, 870),  # take picture
    (833, 922),  # send to
    (890, 376),  # to whom (add more coordinates changing y value if you want more people)
    (920, 920)   # SEND!
]

# time to open snap in CHROME browser
time.sleep(3)  # modify number of seconds if you need to

for i in range(NO_OF_SNAPS):

    for location in locations:

        pyautogui.moveTo(location[0], location[1], duration=uniform(0.1, 0.3))  # Move to the location at random speed
        pyautogui.click()  # Click at the location

        time.sleep(0.01)  # Wait for a short period before the next move
