import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class Calculator:
    def __init__(self):
        pass

    def add(self,a,b):
        return a + b

    def substract(self,a,b):
        return a - b

    def multiply(self,a,b):
        return a * b

    def divide(self,a,b):
        return a / b

def calculate():
    a_str = input_1.get()
    b_str = input_2.get()
    selected_operator = input_3.get()

    try:
        a = int(a_str)
    except ValueError:
        messagebox.showerror("Type Error", "First number must be an integer")
        input_1.delete(0, 'end')
        input_1.focus_set()
        return
    try:
        b = int(b_str)
    except ValueError:
        messagebox.showerror("Type Error", "Second number must be an integer")
        input_2.delete(0, 'end')
        input_2.focus_set()
        return

    result = operator(a, b, selected_operator)
    result_label.config(text="Result: " + str(result))

calc = Calculator()

def operator(a,b, operator):
    result = 0

    if not isinstance(a, int) or not isinstance(b, int):
        messagebox.showerror("Type error", "Enter valid integer numbers")
        if not isinstance(a, int):
            input_1.delete(0, 'end')
            input_1.focus_set()
        if not isinstance(b, int):
            input_2.delete(0, 'end')
            input_2.focus_set()
    if operator == '+':
        result = calc.add(a,b)
    elif operator == '-':
        result = calc.substract(a,b)
    elif operator == '*':
        result = calc.multiply(a,b)
    elif operator == '/':
        if b == 0:
            messagebox.showerror("Error!!!", "Can't be divided by 0")
            input_2.delete(0, 'end')
            input_2.focus_set()
        else:
            result = calc.divide(a,b)
    elif operator not in ('+','-','*','/'):
        messagebox.showerror("Error!!!", "Only + - / * operators are acceptable!")
        input_3.delete(0, 'end')
        input_3.focus_set()
    else:
        result = "Invalid operator!"

    return result

def reset_fields():
    answer = messagebox.askquestion("Reset input fields?")
    if answer == "yes":
        input_1.delete(0, tk.END)
        input_2.delete(0, tk.END)
        input_3.delete(0, tk.END)
        result_label.config(text="Result: ")
        input_1.focus_set()
    elif answer == "no":
        messagebox._show("Cancelled", "Reset canceled.")

def validate_and_focus(event, entry_widget, next_widget):
    input_str = entry_widget.get()
    try:
        value = int(input_str)
        next_widget.focus_set()
    except ValueError:
        try:
            value = float(input_str)
            entry_widget.next_widget()
        except:
            messagebox.showerror("Error", "Integer numbers only")
            entry_widget.delete(0, 'end')
            entry_widget.focus_set()

def operator_check(event):
    input_valid = input_3.get()
    valid_operators = ('+','-','*','/')

    if input_valid in valid_operators:
        calc_button.focus_set()
    else:
        messagebox.showerror("Error", "'+','-','*','/' only")
        input_3.delete(0, 'end')
        input_3.focus_set()

# def on_closing():
#     if messagebox.askokcancel("Quit", "Do yo really want to close the window?"):
#         window.destroy()

# window = tk.Tk()
# window.protocol("WM_DELETE_WINDOW", on_closing) # intercept window close event
#==================program interface start========================
window = tk.Tk()
window.title("Calculator")
window.resizable(True,True)
window.geometry('250x300')

#------button style----------
image1 = Image.open("C:\\Users\\mugger\\Desktop\\programming\\calc\\images\\but_calculate.gif")
image1 = ImageTk.PhotoImage(image1)
image2 = Image.open("C:\\Users\\mugger\\Desktop\\programming\\calc\\images\\but_reset.gif")
image2 = ImageTk.PhotoImage(image2)

calc_buttom_style = ttk.Style()
calc_buttom_style.configure('Rounded.TButton', borderwidth=5, relief=tk.FLAT, background='#ccb800',
                foreground="brown", padding=0, font=("Helvetica", 10, 'bold'))
label_font=("Times new roman", 12, 'bold')

#----create a frame for the input fields----
input_frame = tk.Frame(window)
input_frame.grid(pady=20)

label_1 = ttk.Label(input_frame, text='First number: ', font=label_font)
label_1.grid(row=0, column=0)
input_1 = tk.Entry(input_frame, bg='white')
input_1.grid(row=0, column=1)
input_1.focus_set()
input_1.bind('<Return>', lambda event: validate_and_focus(event, input_1, input_2))

label_2 = tk.Label(input_frame, text='Second number: ', font=label_font)
label_2.grid(row=1, column=0)
input_2 = tk.Entry(input_frame, bg='white')
input_2.grid(row=1, column=1)
input_2.bind('<Return>', lambda event: validate_and_focus(event, input_2, input_3))

label_3 = tk.Label(input_frame, text='Operation: ', font=label_font, width=15)
label_3.grid(row=2, column=0)
input_3 = tk.Entry(input_frame, bg='white')
input_3.grid(row=2, column=1)
input_3.bind('<Return>', operator_check)

calc_button = ttk.Button(input_frame, image=image1, text="Calculate", command=calculate, style='Rounded.TButton')
calc_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)
calc_button.bind('<Return>', lambda event=None:calculate())

result_label = tk.Label(input_frame, text='Result: ', font=label_font)
result_label.grid(row=4, column=0)

reset_button = ttk.Button(input_frame, image=image2, style='Rounded.TButton', text="Reset", command=reset_fields)
reset_button.grid(row=5, column=0, columnspan=2, pady=20)
reset_button.bind('<Return>', lambda event=None:reset_fields())

if __name__ == '__main__':
    window.mainloop()