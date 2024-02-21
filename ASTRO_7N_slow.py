import keyboard
import pyautogui as gui
import time
from functions import setup

setup(2)

def main():
    origin = time.time()
    gui.PAUSE = 0.1
    i = 0
    while not keyboard.is_pressed('RIGHT SHIFT+TAB') and time.time() - origin < 1800:
        if keyboard.is_pressed('RIGHT SHIFT'):
            gui.press(str(i := i % 5 + 1))
            gui.press('ENTER')

main()