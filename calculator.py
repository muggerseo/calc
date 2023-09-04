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
window.geometry('600x600')

label_1 = tk.Label(window, text='First number: ')
label_1.pack(pady=10)
input_1 = tk.Entry(window, bg='white')
input_1.pack()

label_2 = tk.Label(window, text='Second number: ')
label_2.pack(pady=10)
input_2 = tk.Entry(window, bg='white')
input_2.pack()

label_3 = tk.Label(window, text='Operation: ')
label_3.pack(pady=10)
input_3 = tk.Entry(window, bg='white')
input_3.pack()

calc_botton = tk.Button(window, text="Calculate", command=calculate)
calc_botton.pack(pady=20)

result_label = tk.Label(window, text="Result: ")
result_label.pack()

#======input=======

input_1.focus_set()

#=======NUM keys pannel=======

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.entry = tk.Entry(root)
        self.entry.grid(row=0, colomn = 0, colomnspan = 4)

        for i in  range(1,10):
            row_num = (i - 1) // 3 + 1
            col_num = (i + 1) % 3
            button = tk.Button(root, text=str(i), command=lambda i=i: self.on_digital_click(i))
            button.grid(row=row_num, column=col_num)

    def on_digital_click(self, digit):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current_text + str(digit))

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()

if __name__ == '__main__':
    window.mainloop()