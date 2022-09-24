# Imports
import tkinter as tk					
from tkinter import ttk

# Import tk functions
from components import table, yearly_chart, monthly_chart, pie_chart, anpr

# Root Initialization
root = tk.Tk()
root.title('ETMS - Expert Traffic Manangement System')
root.geometry("650x550")

parent = ttk.Frame(root)

# Labels
ttk.Label(parent, text="Expert Traffic Management System",font=("Arial", 16)).pack(pady=25)

# Buttons
tk.Button(parent, text="Start Detection",font="sans 10 bold",bg="#ddd",width=12, command=anpr).pack(ipadx=21,pady=5)
tk.Button(parent, text="Vehicle Data",font="sans 10 bold",bg="#ddd",width=12, command=table).pack(ipadx=21,pady=5)
tk.Button(parent, text="Yearly Data Chart",font="sans 10 bold",bg="#ddd",width=12, command=yearly_chart).pack(ipadx=21,pady=5)
tk.Button(parent, text="Monthly Data Chart",font="sans 10 bold",bg="#ddd",width=12, command=monthly_chart).pack(ipadx=21,pady=5)
tk.Button(parent, text="Cam Data Chart",font="sans 10 bold",bg="#ddd",width=12, command=pie_chart).pack(ipadx=21,pady=5)
tk.Button(parent, text="Help",font="sans 10 bold",bg="#ddd",width=12, command=root.destroy).pack(ipadx=21,pady=5)
tk.Button(parent, text="Exit",font="sans 10 bold",bg="#ddd",width=12, command=root.destroy).pack(ipadx=21,pady=5)

parent.pack(expand=1)

# Mainloop
root.mainloop()