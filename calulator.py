import PySimpleGUI as sg
import math

# Define the GUI theme
sg.theme("LightGrey1")

# Define the button size
button_size = (5, 2)

# Define the GUI layout
layout = [
    [sg.Input(size=(18, 1), key="-DISPLAY-", justification="right", font=("Helvetica", 20))],
    [
        sg.Button("√", size=button_size, font=("Helvetica", 15)),
        sg.Button("^", size=button_size, font=("Helvetica", 15)),
        sg.Button("CE", size=button_size, font=("Helvetica", 15)),
        sg.Button("C", size=button_size, font=("Helvetica", 15)),
    ],
    [
        sg.Button("7", size=button_size, font=("Helvetica", 15)),
        sg.Button("8", size=button_size, font=("Helvetica", 15)),
        sg.Button("9", size=button_size, font=("Helvetica", 15)),
        sg.Button("/", size=button_size, font=("Helvetica", 15)),
    ],
    [
        sg.Button("4", size=button_size, font=("Helvetica", 15)),
        sg.Button("5", size=button_size, font=("Helvetica", 15)),
        sg.Button("6", size=button_size, font=("Helvetica", 15)),
        sg.Button("*", size=button_size, font=("Helvetica", 15)),
    ],
    [
        sg.Button("1", size=button_size, font=("Helvetica", 15)),
        sg.Button("2", size=button_size, font=("Helvetica", 15)),
        sg.Button("3", size=button_size, font=("Helvetica", 15)),
        sg.Button("-", size=button_size, font=("Helvetica", 15)),
    ],
    [
        sg.Button(".", size=button_size, font=("Helvetica", 15)),
        sg.Button("0", size=button_size, font=("Helvetica", 15)),
        sg.Button("=", size=button_size, font=("Helvetica", 15)),
        sg.Button("+", size=button_size, font=("Helvetica", 15)),

    ],
]

# Create the window
window = sg.Window("Calculator", layout, return_keyboard_events=True)

expression = ""
result = ""

# Event loop to process window events
while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event.isdigit():
        expression += event
        window["-DISPLAY-"].update(expression)

    if event in ("+", "-", "*", "/"):
        expression += event
        window["-DISPLAY-"].update(expression)

    if event == ".":
        expression += event
        window["-DISPLAY-"].update(expression)

    if event == "√":
        try:
            result = str(math.sqrt(eval(expression)))
            window["-DISPLAY-"].update(result)
            expression = result
        except ValueError:
            window["-DISPLAY-"].update("Error: Invalid input")
            expression = ""

    if event == "^":
        expression += "**"
        window["-DISPLAY-"].update(expression)

    if event == "C":
        expression = ""
        result = ""
        window["-DISPLAY-"].update("")

    if event == "CE":
        expression = expression[:-1]
        window["-DISPLAY-"].update(expression)

    if event == "=":
        try:
            result = str(eval(expression))
            window["-DISPLAY-"].update(result)
            expression = result
        except ZeroDivisionError:
            window["-DISPLAY-"].update("Error: Division by zero")
            expression = ""

# Close the window
window.close()
