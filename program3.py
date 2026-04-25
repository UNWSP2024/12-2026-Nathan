# By Nathan Nelsen
# Written 4/24/26
# Long-Distance Calls

import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    try:
        minutes = float(entry_minutes.get())

        if minutes < 0:
            raise ValueError

        if rate_var.get() == 1:      # Daytime
            rate = 0.02
        elif rate_var.get() == 2:    # Evening
            rate = 0.12
        elif rate_var.get() == 3:    # Off-Peak
            rate = 0.05
        else:
            messagebox.showwarning("Selection Error", "Please select a rate category.")
            return

        charge = minutes * rate
        messagebox.showinfo("Call Charge", f"Total charge: ${charge:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of minutes.")

root = tk.Tk()
root.title("Long Distance Call Calculator")

rate_var = tk.IntVar()

tk.Label(root, text="Select Rate Category:").pack(anchor='w')

tk.Radiobutton(root, text="Daytime (6:00 A.M. - 5:59 P.M.)  $0.02/min",
               variable=rate_var, value=1).pack(anchor='w')

tk.Radiobutton(root, text="Evening (6:00 P.M. - 11:59 P.M.)  $0.12/min",
               variable=rate_var, value=2).pack(anchor='w')

tk.Radiobutton(root, text="Off-Peak (12:00 A.M. - 5:59 A.M.)  $0.05/min",
               variable=rate_var, value=3).pack(anchor='w')

tk.Label(root, text="Enter number of minutes:").pack(pady=5)
entry_minutes = tk.Entry(root)
entry_minutes.pack()

tk.Button(root, text="Calculate Charge", command=calculate_charge).pack(pady=10)

root.mainloop()
