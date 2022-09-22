# Imports
import tkinter as tk					
from tkinter import ttk

# Root Initialization
root = tk.Tk()
root.title('ETMS - Expert Traffic Manangement System')
root.geometry("650x550")
style = ttk.Style()
style.theme_use('clam')

# Labels
ttk.Label(root, text="Help",font=("Arial", 18)).pack(pady=25)
ttk.Label(root, text="1. Click Start Detection To Run The System",font=("Arial", 12)).pack(pady=5)
ttk.Label(root, text="2. Click Vehicle Data To Show the Table of Detected Vehicle",font=("Arial", 12)).pack(pady=5)
ttk.Label(root, text="3. Click Yearly Data Chart To Show The Chart",font=("Arial", 12)).pack(pady=5)
ttk.Label(root, text="4. Click Monthly Data Chart To Show The Chart",font=("Arial", 12)).pack(pady=5)
ttk.Label(root, text="5. Click Cam Data Chart To Show The Chart",font=("Arial", 12)).pack(pady=5)

# Buttons
tk.Button(root, text="Back",font="sans 10 bold",bg="#ddd",width=12, command=root.destroy).pack(pady=15)


# Mainloop
root.mainloop()