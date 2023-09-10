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
        return a % b

def calculate():
    a = float(input_1.get())
    b = float(input_2.get())
    selected_operator = input_3.get()

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
        if b == 0:
            messagebox.showerror("Error!!!", "Can't be divided by 0!")
        else:
            result = calc.divide(a, b)
    else:
        result = "Invalid operator!"

    return result
       
#==================program interface start========================        
window = tk.Tk()
window.title("Calculator")
window.resizable(True,True)
window.geometry('300x400')

#----create a frame for the input fields----
input_frame = tk.Frame(window)
input_frame.grid(pady=20)

label_1 = tk.Label(input_frame, text='First number: ')
label_1.grid(row=0, column=0)
input_1 = tk.Entry(input_frame, bg='white')
input_1.grid(row=0, column=1)

label_2 = tk.Label(input_frame, text='Second number: ')
label_2.grid(row=1, column=0)
input_2 = tk.Entry(input_frame, bg='white')
input_2.grid(row=1, column=1, padx=10)

label_3 = tk.Label(input_frame, text='Operation: ')
label_3.grid(row=2, column=0)
input_3 = tk.Entry(input_frame, bg='white')
input_3.grid(row=2, column=1)

calc_button = tk.Button(input_frame, text="Calculate", command=calculate)
calc_button.grid(row=4, columnspan=1, pady=5)

result_label = tk.Label(input_frame, text='Result: ')
result_label.grid(row=5, columnspan=1)

# Create a frame for the numeric keypad
keypad_frame = tk.Frame(window)
keypad_frame.grid(row=6, column=1, pady=20)

#======input=======

input_1.focus_set()

#=======NUM keys pannel=======

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.entry = tk.Entry(root)
        self.entry.grid(row = 0, column = 0, columnspan = 3)

        for i in  range(1, 10):
            row_num = (i - 1) // 3 + 1
            col_num = (i - 1) % 3
            if i == 9:
                col_num = 2
            button = tk.Button(root, text=str(i), command=lambda i=i: self.on_digital_click(i))
            button.grid(row=row_num, column=col_num)

    def on_digital_click(self, digit):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current_text + str(digit))

app = CalculatorApp(window)

if __name__ == '__main__':
    window.mainloop()