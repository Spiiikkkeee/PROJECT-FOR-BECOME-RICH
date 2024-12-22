import tkinter as tk
import math

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def calculate_sqrt():
    try:
        current = float(entry.get())
        result = math.sqrt(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display numbers
entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 16), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button definitions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Back', 5, 0), ('√', 5, 1)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="lightgreen", command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="red", fg="white", command=clear_entry)
    elif text == "Back":
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="orange", command=backspace)
    elif text == "√":
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="lightblue", command=calculate_sqrt)    
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Make rows and columns stretchable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the app
root.mainloop()
