from PIL import Image
import keyboard
import pyautogui as gui
import time

origin = time.time()
gui.PAUSE = 0.025
i = 0
while not keyboard.is_pressed('ESC+`') and time.time() - origin < 1800:
    if keyboard.is_pressed('SHIFT+CTRL') and not gui.pixelMatchesColor(2150, 955, (157, 159, 129), tolerance=10):
        gui.press(str(i := i % 5 + 1))
        gui.press('ENTER')