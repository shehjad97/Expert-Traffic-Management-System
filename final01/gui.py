# Imports
import tkinter as tk					
from tkinter import ttk

# Import tk functions
from components import table, chart, anpr

# Root Initialization
root = tk.Tk()
root.title('ETMS - Expert Traffic Manangement System')
root.geometry("250x250")
style = ttk.Style()
style.theme_use('clam')

# Labels
ttk.Label(root, text="Expert Traffic Management System").pack()

def exit():
    root.destroy()

# Buttons
ttk.Button(root, text="Start Detection", command=anpr).pack()
ttk.Button(root, text="Data", command=table).pack()
ttk.Button(root, text="Chart", command=chart).pack()
ttk.Button(root, text="Exit", command=exit).pack()

# Mainloop
root.mainloop()