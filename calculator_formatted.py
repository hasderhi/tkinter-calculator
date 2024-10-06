# tkinter calculator - a showcase of tkinter's capabilities!

# This is a small program in python using the tkinter module.
# It is a simple calculator that can perform addition, subtraction, multiplication and division.
# The program uses a GUI to get the user's input and display the result.

# Its purpose is to be an educational example of how tkinter can be used for small GUI applications
# and to demonstrate the use of the tkinter module in python.
# All variables and function names should be written in camelCase.

# Copyright (c) 2024 Tobias Kisling (Github: https://github.com/hasderhi).
# This software is released under the MIT license.
# tk_dev - Software with passion!


# First, the program tries to import all needed modules
try:
    from tkinter import *  # The main module for tkinter
    from tkinter import messagebox  # The messagebox module
except ImportError or ModuleNotFoundError:  # If something went wrong,try to import at least messagebox so it can display an error message
    try:
        from tkinter import messagebox

        messagebox.showerror(
            "Fatal Error",
            "Fatal Error occured while importing required modules. Program will be canceled.\nErrorcode = 000",
        )
        print(
            "Fatal Error occured while importing required modules. Program will be canceled. Errorcode = 000"
        )
    except ImportError or ModuleNotFoundError:  # If not even that works, just print an error msg to the terminal
        print(
            "Fatal Error occured while importing required modules. Program will be canceled. Errorcode = 000"
        )
    exit()  # And exit the program

from tkinter import *  # This could be removed as a double import (Not needed) but without this line, the IDE won't display the code colored as the real imports are in a try/except block.


# If the program has come to this part of the code, it means all imports were successful.


try:  # Try to initialize the equation array. If this fails, display an error message and exit the program.
    equation = []
except Exception as e:
    messagebox.showerror(
        "Fatal Error while initializing the equation variable. Program will be canceled. \nErrorcode = 003"
    )
    print(
        "Fatal Error while initializing the equation variable. Program will be canceled. Errorcode = 003"
    )
    exit()


# Now the program will define all functions for the GUI and the calculation processing


# This is the main function for the GUI that creates the tkinter window:
def createRoot():
    global display  # The variable for the display needs to be global in order other functions can change the text.
    root = Tk()  # Our main window is called 'root' (Most common naming in tkinter).
    root.title("Calculator")  # Window title - 'Calculator'
    root.geometry("540x600")  # The width and height of our window.
    root.resizable(False, False)  # The window shall not be resizable by the user
    root.configure(bg="#808080")  # The background (bg) of root

    # Now the program will initialize a frame for the 'display' (The part of the GUI that displays the calculation).

    # First, it creates a frame for the display in 'root'
    display_frame = Frame(root, width=540, height=100, bg="#808080")
    display_frame.place(x=10, y=10)

    display_frame.rowconfigure(0, weight=1)  # This centers the frame.
    display_frame.columnconfigure(0, weight=1)

    display = Label(
        display_frame,
        width=32,
        height=3,
        font=("TkDefaultFont", 21),
        text="Enter calculation",
    )  # Now the code creates a label called 'display'
    display.grid(row=0, column=0, sticky="nsew")  # Centers the label in the frame

    # Now that the display is created, the code will initialize another frame for the buttons of the calculator

    buttons_frame = Frame(root, width=480, height=500, bg="#808080")
    buttons_frame.place(x=10, y=120)

    # Now we create buttons that resemble a numpad with numbers, operators, a backspace ('del') and an 'AC' clear button.

    button7 = Button(
        buttons_frame,
        width=15,
        height=5,
        text="7",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation(7),
    )  # On click, it calls a anonymous (lambda) function 'createEquation' with the number of the button
    button7.grid(row=0, column=0, sticky="nsew")

    button8 = Button(
        buttons_frame,
        width=15,
        height=5,
        text="8",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation(8),
    )
    button8.grid(row=0, column=1, sticky="nsew")

    button9 = Button(
        buttons_frame,
        width=15,
        height=5,
        text="9",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation(9),
    )
    button9.grid(row=0, column=2, sticky="nsew")

    buttonDiv = Button(
        buttons_frame,
        width=15,
        height=5,
        text="/",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation("/"),
    )
    buttonDiv.grid(row=0, column=3, sticky="nsew")

    button4 = Button(
        buttons_frame,
        width=15,
        height=5,
        text="4",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation(4),
    )
    button4.grid(row=1, column=0, sticky="nsew")

    button5 = Button(
        buttons_frame,
        width=15,
        height=5,
        text="5",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation(5),
    )
    button5.grid(row=1, column=1, sticky="nsew")

    button6 = Button(
        buttons_frame,
        width=15,
        height=5,
        text="6",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation(6),
    )
    button6.grid(row=1, column=2, sticky="nsew")

    buttonMult = Button(
        buttons_frame,
        width=15,
        height=5,
        text="*",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation("*"),
    )
    buttonMult.grid(row=1, column=3, sticky="nsew")

    button1 = Button(
        buttons_frame,
        width=15,
        height=5,
        text="1",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation(1),
    )
    button1.grid(row=2, column=0, sticky="nsew")

    button2 = Button(
        buttons_frame,
        width=15,
        height=5,
        text="2",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation(2),
    )
    button2.grid(row=2, column=1, sticky="nsew")

    button3 = Button(
        buttons_frame,
        width=15,
        height=5,
        text="3",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation(3),
    )
    button3.grid(row=2, column=2, sticky="nsew")

    buttonSubt = Button(
        buttons_frame,
        width=15,
        height=5,
        text="-",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation("-"),
    )
    buttonSubt.grid(row=2, column=3, sticky="nsew")

    button0 = Button(
        buttons_frame,
        width=15,
        height=5,
        text="0",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation(0),
    )
    button0.grid(row=3, column=0, sticky="nsew")

    buttonDel = Button(
        buttons_frame,
        width=15,
        height=5,
        text="DEL",
        font=("TkDefaultFont", 10),
        command=lambda: backspace(),
    )
    buttonDel.grid(row=3, column=1, sticky="nsew")

    buttonAC = Button(
        buttons_frame,
        width=15,
        height=5,
        text="AC",
        font=("TkDefaultFont", 10),
        command=lambda: clear(),
    )
    buttonAC.grid(row=3, column=2, sticky="nsew")

    buttonAdd = Button(
        buttons_frame,
        width=15,
        height=5,
        text="+",
        font=("TkDefaultFont", 10),
        command=lambda: createEquation("+"),
    )
    buttonAdd.grid(row=3, column=3, sticky="nsew")

    frameEqualsButton = Frame(
        root, width=540, height=100, bg="#808080"
    )  # Now it creates a bigger frame for the equals ('=') button.
    frameEqualsButton.place(x=10, y=488)

    buttonEquals = Button(
        frameEqualsButton,
        width=31,
        height=5,
        text="=",
        font=("TkDefaultFont", 10),
        command=calculate,
    )  # On click, this button calls the function 'calculate'
    buttonEquals.grid(row=0, column=0, sticky="nsew")

    root.mainloop()  # Mainloop of the root window, here ends the code for the GUI itself


def reloadDisplay():  # This function reloads the displayed text in the window and replaces it with the current string in the equation array.
    display.configure(text=equation)


def resetDisplay():  # This resets the display text to the original state
    display.configure(text="Enter calculation")


def createEquation(
    num,
):  # This function is dependant on 'num'. This means, depending on the value the function was called with - for example: createEquation(7) - the function will act differently.
    equation.append(num)  # Adds the 'num' value to the equation array.
    reloadDisplay()  # And reloads the display.


def backspace():  # This function deletes the last entry in the array.
    if (
        equation != []
    ):  # Checks if the array is not empty because we cannot pop a empty array.
        equation.pop()  #'Pops' (delete last entry) the array.
        reloadDisplay()  # Reloads the display.


def clear():  # This function clears the whole array 'equation'.
    equation.clear()  # Deletes all entries.
    resetDisplay()  # Reloads the display.


def calculate():  # Main function of the calculation.
    if equation != []:  # If the array is not empty...
        try:  # ...it tries...
            total = str(
                eval("".join(map(str, equation)))
            )  # ...to get a result from the given equation.
            equation.clear()  # Then it clears the equation.
            equation.append(total)  # And instead appends the result.
            reloadDisplay()  # Then the program reloads.
        except Exception as e:  # If any error occurs...
            messagebox.showerror(
                "Error", "Error in calculation process occurred.\nErrorcode = 001"
            )  # The program shows an error message...
            print(
                "Error in calculation - Error in calculation process occurred. Errorcode = 001"
            )
            equation.clear()  # Deletes the faulty equation.
            resetDisplay()  # And resets the display.
    else:  # If no calculation is entered at all, it shows another error.
        messagebox.showerror("Error", "No calculation entered.\nErrorcode = 002")
        print("Error in calculation - No calculation entered. Errorcode = 002")


createRoot()  # After all functions are defined, the program starts itself by calling the main function.
