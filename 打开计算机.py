import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def calculate():
    try:
        result = eval(entry.get())
        history_text.insert(tk.END, f"{entry.get()} = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def add_negative_sign():
    current = entry.get()
    if current and (current[0].isdigit() or current[0] in "("):
        entry.insert(0, "-")

def clear_history():
    history_text.delete(1.0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('±', 5, 1), ('Clear History', 5, 2)  # 添加清除历史记录按钮
]

for label, row, col in buttons:
    if label == 'C':
        button = tk.Button(root, text=label, command=clear, width=10)
    elif label == '=':
        button = tk.Button(root, text=label, command=calculate, width=10)
    elif label == '±':
        button = tk.Button(root, text=label, command=add_negative_sign, width=10)
    elif label == 'Clear History':
        button = tk.Button(root, text=label, command=clear_history, width=15)
    else:
        button = tk.Button(root, text=label, command=lambda label=label: button_click(label), width=10)
    button.grid(row=row, column=col)

history_text = tk.Text(root, height=5, width=30)
history_text.grid(row=6, column=0, columnspan=4)

root.mainloop()