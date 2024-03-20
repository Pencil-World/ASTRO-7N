import json

def setup(index):
    array = ["Enter 1 to start the program. \n\tThis option assumes the loaded settings from file. \n\tThis is default if never altered. ", 
            "Enter 2 to set the Copper detection point. ", \
            "Enter 3 to import a quizlet for the quiz. ", \
            "Enter 4 to export a quizlet from the quiz. ", \
            "Enter 5 to set the size of the dialogue box reader. "]

    while True:
        text = input('\n'.join(array[:index]) + '\n')
        if text == '1':
            print("Program start")
            return json.load("settings.json") # only exit to the function
        elif text == '2':
            print("The copper detection point allows the program to stop the dialogue when copper presents his quizes. ")
            print("Set the application to full screen. ")
            print("Hover over a distinguishable part of copper. ")
            print("Press ENTER. ")
            print("Function continues. ")
            set_detection_point()
        elif text == '3':
            print()
            print("successful, quizlet is empty, blah, blah, blah")
            import_quizlet()
        elif text == '4':
            # print instructions to upload quizlet
            export_quizlet()
        elif text == '5':
            print("The dialogue box allows the program to read the questions and answers of copper quizes. ")
            print("Set the application to full screen. ")
            print("Hover over the top left of the dialogue box. ")
            print("Press ENTER. ")
            print("Hover over the top right of the dialogue box. ")
            print("Press ENTER. ")
            print("Function continues. ")
            set_dialogue_box()

# acts like the c++ indexing operator []. gets and sets. 
def subscript(key, val = None):
    obj = json.load("settings.json")
    if val == None:
        return obj[key]
    obj[key] = val

def set_detection_point():
    import keyboard
    import pyautogui as gui

    keyboard.wait("ENTER")
    mouse_x, mouse_y = gui.position()
    color = gui.pixel(mouse_x, mouse_y)
    subscript("detection_point", [mouse_x, mouse_y, color])

def set_dialogue_box():
    import keyboard
    import pyautogui as gui

    dialogue_box_coords = [None, None]
    keyboard.wait("ENTER")
    dialogue_box_coords[0] = gui.position()
    keyboard.wait("ENTER")
    dialogue_box_coords[1] = gui.position()
    subscript("dialogue_box", dialogue_box_coords)

def ocr():
    import easyocr
    from PIL import Image
    
def export_quizlet():
    print()

def import_quizlet():
    print()