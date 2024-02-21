def setup(index):
    array = ["Enter 1 to start the program normally.", \
            "Enter 2 to set the Copper detection point.", \
            "Enter 3 to export a quizlet from the quiz.", \
            "Enter 4 to import a quizlet for the quiz. "]
    text = ""

    while text not in [str(elem) for elem in range(1, index + 1)]:
        text = input('\n'.join(array[:index]) + '\n')
        if text == '1':
            print()
        elif text == '2':
            print()
        elif text == '3':
            print()
        elif text == '4':
            print()