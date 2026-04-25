# By Nathan Nelsen
# Written 4/24/26
# MPG Calculator

import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        gallons = float(entry_gallons.get())
        miles = float(entry_miles.get())

        if gallons <= 0:
            messagebox.showerror("Error", "Gallons must be greater than 0.")
            return

        mpg = miles / gallons
        result_var.set(f"MPG: {mpg:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Gas Mileage Calculator")

label_gallons = tk.Label(root, text="Gallons of Gas:")
label_gallons.grid(row=0, column=0, padx=10, pady=10)

entry_gallons = tk.Entry(root)
entry_gallons.grid(row=0, column=1, padx=10, pady=10)

label_miles = tk.Label(root, text="Miles on Full Tank:")
label_miles.grid(row=1, column=0, padx=10, pady=10)

entry_miles = tk.Entry(root)
entry_miles.grid(row=1, column=1, padx=10, pady=10)

calc_button = tk.Button(root, text="Calculate MPG", command=calculate_mpg)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
