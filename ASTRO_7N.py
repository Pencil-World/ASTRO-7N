# Basic
import keyboard
import pyautogui as gui
from functions import setup
import time

# Advanced
from functions import ocr
from difflib import SequenceMatcher
import string

def extract_screen_text():
    filename = 'screenshot.jpg'
    gui.screenshot(filename, region=dialogue_box)
    return ocr(filename)

def clean_extracted_text(extracted_text):
    remove_punctuation = lambda input: input.strip().lower().translate(str.maketrans('', '', string.punctuation))
    text_block = [""]
    index = 65
    for bounding_box in extracted_text:
        if ord(bounding_box[1][0]) == index and text_block[-1] != "":
            text_block.append("")
            index += 1
        text_block[-1] += remove_punctuation(bounding_box[1]) + " "
    return text_block

CopperQuizzes = input("Do you want the program to complete copper quizzes as well as advance the dialogue? [Y/N] ") == 'Y'
info = setup(3 if CopperQuizzes == False else 5)
x, y, expectedRGBColor = info["detection_point"]
if CopperQuizzes:
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
        elif CopperQuizzes:
            keyboard.wait('ENTER')
            keyboard.wait('SHIFT+CTRL')

            extracted_text = extract_screen_text()
            text_block = clean_extracted_text(extracted_text)

            # similarities = [[SequenceMatcher(None, text_block[0], question).ratio(), question, answer] for question, answer in quizlet.items()]
            # best_match = max(similarities, key=lambda elem: elem[0])
            # if best_match[0] < 0.875:
            #     CopperQuizzes = False
            #     print(f"ERROR: The observed string [{text}] from the application is not similar enough to the given string [{best_match[1]}] from the imported quizlet. ")
            #     continue

            # moara = [[SequenceMatcher(None, answer, best_match[2]).ratio(), answer] for answer in text]
            # best_match = max(moara, key=lambda elem: elem[0])
            # gui.press(str(best_match))
            # gui.press('ENTER')