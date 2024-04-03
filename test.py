from functions import ocr, setup
import pyautogui as gui
import keyboard
import string
from difflib import SequenceMatcher

info = setup(5)
dialogue_box = info["dialogue_box"]
quizlet = info["quizlet"]

remove_punctuation = lambda input: input.lower().translate(str.maketrans('', '', string.punctuation))
filename = 'screenshot.jpg'
keyboard.wait('SPACE')
gui.screenshot(filename, region=dialogue_box)
text = ocr(filename)


text = "Very well. What are the differences between open star clusters and globular star clusters?"
remove_punctuation = lambda input: input.lower().translate(str.maketrans('', '', string.punctuation))
text = remove_punctuation(text)
similarities = [[SequenceMatcher(None, text, question).ratio(), question, answer] for question, answer in quizlet.items()]
best_match = max(similarities, key=lambda elem: elem[0])
print(best_match)
print(text)