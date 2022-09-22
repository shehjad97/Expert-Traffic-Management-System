# Imports
import tkinter as tk					
from tkinter import ttk

# Import tk functions
from components import table, chart, anpr

# Root Initialization
root = tk.Tk()
root.title('ETMS - Expert Traffic Manangement System')
root.geometry("650x550")
style = ttk.Style()
style.theme_use('clam')

# Labels
ttk.Label(root, text="Expert Traffic Management System",font=("Arial", 16)).pack(pady=25)

# Buttons
tk.Button(root, text="Start Detection",font="sans 10 bold",bg="#ddd",width=12, command=anpr).pack(ipadx=21,pady=5)
tk.Button(root, text="Vehicle Data",font="sans 10 bold",bg="#ddd",width=12, command=table).pack(ipadx=21,pady=5)
tk.Button(root, text="Yearly Data Chart",font="sans 10 bold",bg="#ddd",width=12, command=chart).pack(ipadx=21,pady=5)
tk.Button(root, text="Monthly Data Chart",font="sans 10 bold",bg="#ddd",width=12, command=chart).pack(ipadx=21,pady=5)
tk.Button(root, text="Cam Data Chart",font="sans 10 bold",bg="#ddd",width=12, command=chart).pack(ipadx=21,pady=5)
tk.Button(root, text="Help",font="sans 10 bold",bg="#ddd",width=12, command=root.destroy).pack(ipadx=21,pady=5)
tk.Button(root, text="Exit",font="sans 10 bold",bg="#ddd",width=12, command=root.destroy).pack(ipadx=21,pady=5)


# Mainloop
root.mainloop()