# Imports
import tkinter as tk					
from tkinter import ttk

# Root Initialization
root = tk.Tk()
root.title('ETMS - Expert Traffic Manangement System')
root.geometry("650x550")


parent = ttk.Frame(root)

label_texts = """1. Click Start Detection To Run The System
2. Click Vehicle Data To Show the Table of Detected Vehicle
3. Click Yearly Data Chart To Show The Chart
4. Click Monthly Data Chart To Show The Chart
5. Click Cam Data Chart To Show The Chart
"""

# Labels
ttk.Label(parent, text="Help",font=("Arial", 18)).pack(pady=25)
ttk.Label(parent, text=label_texts,font=("Arial", 12)).pack(padx=(50,0),pady=5)

# Buttons
tk.Button(parent, text="Back",font="sans 10 bold",bg="#ddd",width=12, command=root.destroy).pack(pady=15)

parent.pack(expand=1)

# Mainloop
root.mainloop()