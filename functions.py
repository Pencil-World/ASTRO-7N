import json
import keyboard
import pyautogui as gui
import string

def setup(index):
    array = ["Enter 1 to start the program. \n\tThis option assumes the loaded settings from file. \n\tThis is default if never altered. ", 
            "Enter 2 to set the Copper detection point. ", \
            "Enter 3 to import a quizlet for the quiz. ", \
            "Enter 4 to export a quizlet from the quiz. ", \
            "Enter 5 to set the size of the dialogue box reader. "]

    if index == 5:
        import easyocr
        global ocr
        ocr = easyocr.Reader(['en'])
        print('\n\n')

    while True:
        text = input('\n'.join(array[:index]) + '\n')
        print()

        if text == '1':
            print("Program start")
            with open('settings.json', 'r') as file:
                return json.load(file) # only exit to the function
        elif text == '2':
            print("The copper detection point allows the program to stop the dialogue when copper presents his quizes. ")
            print("Set the application to full screen. ")
            set_detection_point()
        elif text == '3':
            print("The following instructions will explain how to import a quizlet into the program. ")
            print("1. Navigate to the desired quizlet. This will be the quizlet url. ")
            print("2. Login to your quizlet account. You can use your school account for this. ")
            print("3. Press the copy and edit button. It will look like 2 overlapping rectangles. ")
            print("4. Click [Create]. The button is on the top right. ")
            print("5. Click the three horizontal dots and then [Export]. ")
            print("6. Copy and paste the exported text into the import.txt file. ")
            import_quizlet()
        elif text == '4':
            print("The following instructions will explain how to export a quizlet from the program. ")
            print("1. Start the copper quiz. ")
            print("2. Navigate to the question and answer screen")
            print("3. Press ENTER to record the question and answers. ")
            print("4. Repeat until the end of the quiz. ")
            print("5. When the quiz ends, press ESC and ` to exit. ")
            print("6. The quizlet should have been exported to export.txt file. ")
            export_quizlet()
        elif text == '5':
            print("The dialogue box allows the program to read the questions and answers of copper quizes. ")
            print("Set the application to full screen. ")
            set_dialogue_box()
        else: 
            print("Invalid input. ")
        print("Function continues. \n")

# acts like the c++ indexing operator []. gets and sets. 
def subscript(key, val = None):
    with open('settings.json', 'r+') as file:
        obj = json.load(file)
        if val == None:
            return obj[key]
        obj[key] = val

        file.truncate(0)
        file.seek(0)
        json.dump(obj, file, indent=4)

def set_detection_point():
    print("Hover over a distinguishable part of copper. ")
    print("Press ENTER. ")
    keyboard.wait("ENTER")
    mouse_x, mouse_y = gui.position()

    color = gui.pixel(mouse_x, mouse_y)
    subscript("detection_point", [mouse_x, mouse_y, color]) # is this correct json format?

def set_dialogue_box():
    dialogue_box_coords = [None, None, None, None]

    print("Hover over the top left of the dialogue box. ")
    print("Press ENTER. ")
    keyboard.wait("ENTER")
    dialogue_box_coords[:2] = gui.position()

    print("Hover over the bottom right of the dialogue box. ")
    print("Press ENTER. ")
    keyboard.wait("ENTER")
    dialogue_box_coords[2:] = [gui.position()[0] - dialogue_box_coords[0], gui.position()[1] - dialogue_box_coords[1]] # placeholder

    subscript("dialogue_box", dialogue_box_coords)

def ocr(file):
    return ocr.readtext(file)
    
def export_quizlet():
    dialogue_box = subscript("dialogue_box")
    quizlet_parsed = []

    while not keyboard.is_pressed('ESC+`'):
        keyboard.wait("SPACE")
        extracted_text = extract_screen_text(dialogue_box)
        text_block = clean_extracted_text(extracted_text)
        quizlet_parsed.append(text_block[0] + '\t' + ';'.join(text_block[1:]))
    with open('export.txt', 'w') as file:
        file.write('\n'.join(quizlet_parsed))

def import_quizlet():
    import string
    remove_punctuation = lambda input: input.lower().translate(str.maketrans('', '', string.punctuation))
    quizlet_parsed = dict()
    
    with open('import.txt', 'r') as file:
        for line in file:
            question, answer = line.strip().split('\t')
            quizlet_parsed[remove_punctuation(question)] = remove_punctuation(answer)
    subscript("quizlet", quizlet_parsed)

def extract_screen_text(dialogue_box):
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