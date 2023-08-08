import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operator.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2

    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Calculator")

label_num1 = tk.Label(root, text="Enter first number: ")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number: ")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

operator = tk.StringVar(root)
operator.set("+")
operations = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(root, operator, *operations)
operation_menu.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()