This Python program creates a simple GUI-based calculator using the Tkinter library. The calculator allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

Key Features:

Graphical User Interface (GUI):
Uses the tkinter.Tk() window as the main application frame.
Provides a numeric keypad and basic operation buttons.

Functionalities:
Digit and Operator Input: Clicking a button adds the corresponding character to the entry field.
Clear Function: The "Clear" button removes all text from the entry field.
Calculation Execution: Pressing = evaluates the expression and displays the result.

Functions:
button_click(char): Inserts the clicked number or operator into the entry field.
clear(): Clears the entry field.
calculate(): Evaluates the mathematical expression entered by the user and displays the result. If the input is invalid, it shows "Error."

GUI Components:
tk.Entry(): Creates an input field for user input.
tk.Button(): Generates buttons for numbers, operations (+, -, *, /), and special functions (=, "Clear").
grid() Layout Manager: Arranges buttons in a 4x4 grid structure.

Execution:
The program initializes the GUI and waits for user interaction. Clicking buttons updates the entry field, and the = button evaluates the expression.
The main event loop (root.mainloop()) keeps the application running.
This simple calculator provides an intuitive way for users to perform arithmetic calculations within a GUI environment. 
