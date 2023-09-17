import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

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
    a_str = float(input_1.get())
    b_str = float(input_2.get())
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

def operator(a, b, operator):
    result = 0
    
    if operator == '+':
        result = calc.add(a, b)
    elif operator == '-':
        result = calc.substract(a, b)
    elif operator == '*':
        result = calc.multiply(a, b)
    elif operator == '/':
        if operator == '/' and b == 0:
            messagebox.showerror("Error!!!", "Can't be divided by 0!")
            input_2.focus_set()
        else:
            result = calc.divide(a, b)
    elif operator not in ('+','-','/','*'):
            messagebox.showerror("Error!!!", "only + - / * operators acceptable!")
            input_3.focus_set()
    elif a is not int:
        messagebox.showerror("Type Error", "Enter number")
        input_1.focus_set()
    elif b is not int:
        messagebox.showerror("Type Error", "Enter number")
        input_2.focus_set()
    else:
        result = "Invalid operator!"

    return result

def reset_fields():
    input_1.delete(0, tk.END)
    input_2.delete(0, tk.END)
    input_3.delete(0, tk.END)
#==================program interface start========================        
window = tk.Tk()
window.title("Calculator")
window.resizable(True,True)
window.geometry('250x300')

#----create a frame for the input fields----
input_frame = tk.Frame(window)
input_frame.grid(pady=20)

label_1 = tk.Label(input_frame, text='First number: ', font=("Helvetica", 10, 'bold'))
label_1.grid(row=0, column=0)
input_1 = tk.Entry(input_frame, bg='white')
input_1.grid(row=0, column=1)
input_1.focus_set()
input_1.bind('<Return>', lambda event: input_2.focus_set())

label_2 = tk.Label(input_frame, text='Second number: ', font=("Helvetica", 10, 'bold'))
label_2.grid(row=1, column=0)
input_2 = tk.Entry(input_frame, bg='white')
input_2.grid(row=1, column=1)
input_2.bind('<Return>', lambda event: input_3.focus_set())

label_3 = tk.Label(input_frame, text='Operation: ', font=("Helvetica", 10, 'bold'))
label_3.grid(row=2, column=0)
input_3 = tk.Entry(input_frame, bg='white')
input_3.grid(row=2, column=1)
input_3.bind('<Return>', lambda event: calc_button.focus_set())

calc_button = tk.Button(input_frame, text="Calculate", width=10, height=2, command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
calc_button.bind('<Return>', lambda event=None:calculate())

result_label = tk.Label(input_frame, text='Result: ')
result_label.grid(row=4, column=0)

reset_button = tk.Button(input_frame, text="Reset", bg='grey', fg='red', width=10, height=2, command=reset_fields)
reset_button.grid(row=5, column=0, columnspan=2, pady=30)

# Create a frame for the numeric keypad
# keypad_frame = tk.Frame(window)
# keypad_frame.grid()

# enter_button = tk.Button(input_frame, text='Next number')
# enter_button.grid(row=7, column=0, columnspan=3, pady=20)

#======input=======
input_1.focus_set()
#=======NUM keys pannel=======

# class CalculatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Calculator")

#         self.entry = tk.Entry(root)
#         self.entry.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

#         self.current_number = "" # Initialize a variable to store the current number

#         for i in  range(1, 10):
#             row_num = (i - 1) // 3 + 1
#             col_num = (i - 1) % 3
          
#             button = tk.Button(root, text=str(i), command=lambda digit=i: self.on_digital_click(digit))
#             button.grid(row=row_num, column=col_num, sticky="nsew")

#     def on_digital_click(self, digit):
#         current_text = self.entry.get()
#         self.entry.delete(0, tk.END)
#         self.entry.insert(0, current_text + str(digit))

#     def move_to_first_number(self):
#         self.current_number = "" # clear the current number
#         self.entry.delete(0, tk.END) # clear the entry field

# app = CalculatorApp(window)

if __name__ == '__main__':
    window.mainloop()
