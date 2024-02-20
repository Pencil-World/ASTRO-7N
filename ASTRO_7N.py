import time
import keyboard
from PIL import Image
import pyautogui as gui

origin = time.time()
gui.PAUSE = 0.01
i = 0
while not keyboard.is_pressed('ESC+SHIFT') and time.time() - origin < 1800:
    try:
        gui.locateOnScreen('copper.png', region=(2054, 892, 95, 49), confidence=0.9)
        break
    except:
        if keyboard.is_pressed('SHIFT+CTRL'):
            gui.press(str(i := i % 5 + 1))
            gui.press('ENTER')