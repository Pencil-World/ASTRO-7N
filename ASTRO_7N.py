import keyboard
import pyautogui as gui
import time
from functions import setup

level = 1 if input("Enter y if you want the program to complete copper quizes as well as advance the dialogue. ") == 'y' else 0
info = setup(2 if level == 0 else 4)
x, y, expectedRGBColor = info[:3]
if level == 1:
    dialogue_box, quizlet = info[3:]

origin = time.time()
gui.PAUSE = 0.025
i = 0
while not keyboard.is_pressed('ESC+`') and time.time() - origin < 1800:
    if keyboard.is_pressed('SHIFT+CTRL'):
        if not gui.pixelMatchesColor(x=x, y=y, expectedRGBColor=expectedRGBColor, tolerance=10):
            gui.press(str(i := i % 5 + 1))
            gui.press('ENTER')
        elif level == 1:
            print()
            # take a screenshot here
            