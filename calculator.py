import tkinter as tk

def update_display(value):
    if expression.get() == "Math Error":
        expression.set("")

    current_text = expression.get()
    expression.set(current_text + str(value))

def calculate():
    try:
        result = eval(expression.get().replace('x', '*'))
        expression.set(result)
    except:
        expression.set("Math Error")


def clear():
    expression.set("")

root = tk.Tk()
root.title("Python Calculator")
root.geometry("700x450")
# root.resizable(0, 0)     make the window not resizable        
root.configure(bg="black")
 

bg_color = "black"  # Dark background color
btn_color = "dimgrey"  # Button color
btn_operator_color = "mediumblue"  # Operator button color
btn_clear_colour = "firebrick"  # Clear button color
btn_calculate_color = "green"  # Calculate button color
btn_text_color = "white"  # Text color for buttons
entry_bg_color = "black"  # Background for entry widget
entry_text_color = "white"  # Text color for entry


expression = tk.StringVar()

entry = tk.Entry(root, textvariable=expression, font=("Arial", 24), bd=0, bg=entry_bg_color, fg=entry_text_color, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, sticky="nsew")

#Buttons definition and placement
buttons = [
    ('AC', 1, 2), ('/', 1, 1), ('x', 1, 1),
    ('7', 1, 1), ('8', 1, 1), ('9', 1, 1), ('-', 1, 1),
    ('4', 1, 1), ('5', 1, 1), ('6', 1, 1), ('+', 1, 1),
    ('1', 1, 1), ('2', 1, 1), ('3', 1, 1), ('=', 2, 1),
    ('0', 1, 2), ('.', 1, 1)
]



row = 1
col = 0
for button_text, row_span, col_span in buttons:
    
    #Create buttons and assign functions
    if button_text == 'AC':
        btn = tk.Button(root, text=button_text, font=("Arial", 14), bg=btn_clear_colour,fg=btn_text_color,bd=0, command=clear)
    elif button_text == '=':
        btn = tk.Button(root, text=button_text, font=("Arial", 14), bg=btn_calculate_color,fg=btn_text_color,bd=0, command=calculate)
    elif button_text in ['+', '-', '/', 'x']:
        btn = tk.Button(root, text=button_text, font=("Arial", 14), bg=btn_operator_color,fg=btn_text_color,bd=0, command=lambda bValue=button_text: update_display(bValue))
    else:
        btn = tk.Button(root, text=button_text, font=("Arial", 14), bg=btn_color,fg=btn_text_color,bd=0, command=lambda bValue=button_text: update_display(bValue))
    
    # Place the button in the grid with no padding
    btn.grid(row=row, column=col, rowspan=row_span, columnspan=col_span, sticky="nsew" ,padx=2, pady=2)

    # Increment the column index
    col += col_span
    if col > 3:
        col = 0
        row += 1



# Make all rows and columns expand evenly
for i in range(6):  # There are 5 rows (1 entry + 4 button rows) +1 to ensure the final row of buttons spread evenly
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # There are 4 columns
    root.grid_columnconfigure(i, weight=1)

root.mainloop()


