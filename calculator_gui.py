import tkinter as tk

def button_click(char):
    entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widget
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=39, pady=20, command=calculate).grid(row=row, column=col)
    elif button == '0':
        tk.Button(root, text=button, padx=91, pady=20, command=lambda: button_click(button)).grid(row=row, column=col, columnspan=2)
    else:
        tk.Button(root, text=button, padx=39, pady=20, command=lambda char=button: button_click(char)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Add clear button
tk.Button(root, text="Clear", padx=79, pady=20, command=clear).grid(row=row, column=0, columnspan=2)

root.mainloop()
