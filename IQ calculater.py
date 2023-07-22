import tkinter as tk
import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = (num1 / num2) * 100
        label_result.config(text=f"Result: {result:.2f}%")
    except ValueError:
        label_result.config(text="Invalid input. Please enter valid numbers.")


root = tk.Tk()
root.title("IQ Calculater")

root.configure(bg="#f2f2f2")

window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

label_num1 = ttk.Label(root, text="Enter your mental age:", font=("Arial", 16))
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = ttk.Entry(root, font=("Arial", 16))
entry_num1.grid(row=0, column=1, padx=10, pady=10)


label_num2 = ttk.Label(root, text="Enter your real age:", font=("Arial", 16))
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = ttk.Entry(root, font=("Arial", 16))
entry_num2.grid(row=1, column=1, padx=10, pady=10)

button_calculate = ttk.Button(root, text="Calculate", command=calculate, style="TButton")
button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

label_result = ttk.Label(root, text="", font=("Arial", 18))
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create a style for the Calculate button
style = ttk.Style()
style.configure("TButton", foreground="blue", background="#007BFF", font=("Arial", 16), width=15)

root.mainloop()