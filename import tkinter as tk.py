import tkinter as tk

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())  # Use eval to calculate the expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for the display
entry = tk.Entry(root, width=25, borderwidth=5, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('AC', 1, 0), ('%', 1, 1), ('x', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('00', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14),
                  bg="blue",command=calculate).grid(row=row, column=col, sticky="nsew")
    elif text == "AC":
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14),
                  bg="silver",command=clear).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14),
                  bg="brown",command=lambda t=text: button_click(t)).grid(row=row, column=col, sticky="nsew")

# Adjust row and column weights to make buttons expand
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()