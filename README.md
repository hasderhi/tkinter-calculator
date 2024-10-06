# Calculator GUI with Tkinter

This is a simple calculator GUI application built using Python's Tkinter library. The calculator allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.


# How it Works

## User Interface:

The calculator GUI consists of a display area at the top and a numpad with buttons for digits 0-9, basic arithmetic operators (+, -, *, /), and a few special buttons (DEL, AC, =). The user can interact with the calculator by clicking on these buttons.


## Equation Array:

The calculator uses an equation array to store the user's input. Each time a button is clicked, the corresponding value is appended to the equation array. The array is then used to evaluate the expression when the "=" button is clicked.


# Functions:

The calculator has several functions that work together to provide the desired functionality:
#### *createEquation(num):* Appends the input value to the equation array and updates the display.
#### *backspace():* Deletes the last entry in the equation array and updates the display.

#### *clear():* Clears the entire equation array and resets the display.
#### calculate():* Evaluates the expression in the equation array and updates the display with the result.


## Error Handling:

The calculator includes basic error handling to handle cases such as:

Division by zero
Invalid input (e.g., trying to calculate an empty equation)
Errors during calculation (e.g., syntax errors)
In such cases, the calculator displays an error message and resets the display.

# Running the Calculator


To run the calculator, simply execute the *calculator.py*, which initializes the GUI and starts the main event loop.


# License

This software is released under the MIT license. See the LICENSE file for details.

# Author

Tobias Kisling (Github: https://github.com/hasderhi)

# Version

1.0

# Dependencies


Python 3.x;
---
Tkinter library (included with Python)

