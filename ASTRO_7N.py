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

def get_best_match(r, value):
    similarities = [[SequenceMatcher(None, value, elem).ratio(), elem] for elem in r]
    best_match = max(similarities, key=lambda elem: elem[0])
    if best_match[0] < 0.875:
        global CopperQuizzes
        CopperQuizzes = False
        print(f"ERROR: The string [{best_match[1]}] is not similar enough to the string [{value}]. ")
        return 0
    return best_match

CopperQuizzes = input("Do you want the program to complete copper quizzes as well as advance the dialogue? [Y/N] ") == 'Y'
info = setup(3 if CopperQuizzes == False else 5)
x, y, expectedRGBColor = info["detection_point"]
if CopperQuizzes:
    dialogue_box = info["dialogue_box"]
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
            extracted_text = extract_screen_text()
            text_block = clean_extracted_text(extracted_text)

            best_match_question = get_best_match(quizlet.keys(), text_block[0])
            best_match_answer = get_best_match(text_block, quizlet[best_match_question[1]])
            gui.press(str(text_block.index(best_match_answer[1])))
            gui.press('ENTER')