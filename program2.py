# By Nathan Nelsen
# Written 4/24/26
# Joe's Automotive

import tkinter as tk

def calculate_total():
    total = 0

    if oil_var.get():
        total += 30
    if lube_var.get():
        total += 20
    if radiator_var.get():
        total += 40
    if transmission_var.get():
        total += 100
    if inspection_var.get():
        total += 35
    if muffler_var.get():
        total += 200
    if tire_var.get():
        total += 20

    result_label.config(text=f"Total Charges: ${total:.2f}")

root = tk.Tk()
root.title("Joe's Automotive Service")

oil_var = tk.IntVar()
lube_var = tk.IntVar()
radiator_var = tk.IntVar()
transmission_var = tk.IntVar()
inspection_var = tk.IntVar()
muffler_var = tk.IntVar()
tire_var = tk.IntVar()

tk.Checkbutton(root, text="Oil Change ($30.00)", variable=oil_var).pack(anchor='w')
tk.Checkbutton(root, text="Lube Job ($20.00)", variable=lube_var).pack(anchor='w')
tk.Checkbutton(root, text="Radiator Flush ($40.00)", variable=radiator_var).pack(anchor='w')
tk.Checkbutton(root, text="Transmission Fluid ($100.00)", variable=transmission_var).pack(anchor='w')
tk.Checkbutton(root, text="Inspection ($35.00)", variable=inspection_var).pack(anchor='w')
tk.Checkbutton(root, text="Muffler Replacement ($200.00)", variable=muffler_var).pack(anchor='w')
tk.Checkbutton(root, text="Tire Rotation ($20.00)", variable=tire_var).pack(anchor='w')

tk.Button(root, text="Calculate Total", command=calculate_total).pack(pady=10)

result_label = tk.Label(root, text="Total Charges: $0.00")
result_label.pack()

root.mainloop()
