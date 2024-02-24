import keyboard
import pyautogui as gui
import time
from functions import setup

x, y, expectedRGBColor = (2150, 955, (157, 159, 129))

def main():
    origin = time.time()
    gui.PAUSE = 0.025
    i = 0
    while not keyboard.is_pressed('ESC+`') and time.time() - origin < 1800:
        if keyboard.is_pressed('SHIFT+CTRL') and not gui.pixelMatchesColor(x=x, y=y, expectedRGBColor=expectedRGBColor, tolerance=10):
            gui.press(str(i := i % 5 + 1))
            gui.press('ENTER')

x, y, expectedRGBColor = setup(2)
main()