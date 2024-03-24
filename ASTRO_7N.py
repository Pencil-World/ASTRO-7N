import keyboard
import pyautogui as gui
import time
from functions import setup

level = int(input("Do you want the program to complete copper quizes as well as advance the dialogue? [Y/N] ") == 'Y')
info = setup(2 if level == 0 else 5)
x, y, expectedRGBColor = info["detection_point"]
if level == 1:
    dialogue_box = [info["dialogue_box"][0][0], info["dialogue_box"][0][1], info["dialogue_box"][0], info["dialogue_box"][0]]
    quizlet = info["quizlet"]

origin = time.time()
gui.PAUSE = 0.025
i = 0
while not keyboard.is_pressed('ESC+`') and time.time() - origin < 1800:
    if keyboard.is_pressed('SHIFT+CTRL'):
        if not gui.pixelMatchesColor(x=x, y=y, expectedRGBColor=expectedRGBColor, tolerance=10):
            gui.press(str(i := i % 5 + 1))
            gui.press('ENTER')
        elif level == 1:
            gui.screenshot('screenshot.jpg', region=dialogue_box)