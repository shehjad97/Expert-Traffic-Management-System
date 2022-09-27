# Import the required libraries
import tkinter as tk
from tkinter import ttk

import json

class Violations(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the size of the tkinter window
        self.title("Traffic Violations Data")
        self.geometry("800x350")

        # Create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(self, column=("Serial", "License Number", "Detected Violation"), show='headings', height=15)
        tree.column("# 1", minwidth=0, width=300, anchor="center")
        tree.heading("# 1", text="Serial")
        tree.column("# 2", minwidth=0, width=300, anchor="center")
        tree.heading("# 2", text="License Number")
        tree.column("# 3", minwidth=0, width=300, anchor="center")
        tree.heading("# 3", text="Detected Violation")

        with open('violations.json', 'r') as openfile:
            records = json.load(openfile)

        for record in records:
            tree.insert('', 'end', text="1", values=(record['no'], record['license'], record['violation']))

        tree.pack()

if __name__ == '__main__':
    app = Violations()
    app.mainloop()
