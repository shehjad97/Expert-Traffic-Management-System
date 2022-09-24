# Import the required libraries
import tkinter as tk
from tkinter import ttk

import json

class Table(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the size of the tkinter window
        self.title("All Vehicle Data")
        self.geometry("800x350")

        # Create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(self, column=("Serial", "License Number", "Owner's NID", "License Validity", "Cam", "Timestamp"), show='headings', height=15)
        tree.column("# 1", minwidth=0, width=70, anchor="center")
        tree.heading("# 1", text="Serial")
        tree.column("# 2", minwidth=0, width=110, anchor="center")
        tree.heading("# 2", text="License Number")
        tree.column("# 3", minwidth=0, width=120, anchor="center")
        tree.heading("# 3", text="Owner's NID")
        tree.column("# 4", minwidth=0, width=120, anchor="center")
        tree.heading("# 4", text="License Validity")
        tree.column("# 5", minwidth=0, width=70, anchor="center")
        tree.heading("# 5", text="Cam")
        tree.column("# 6", minwidth=0, width=160, anchor="center")
        tree.heading("# 6", text="Timestamp")

        with open('json_data.json', 'r') as openfile:
            records = json.load(openfile)

        for record in records:
            tree.insert('', 'end', text="1", values=(record['no'], record['license_number'], record['nid'], record['license_validity'], record['camera'], record['timestamp']))

        tree.pack()

        # self.mainloop()

if __name__ == '__main__':
    app = Table()
    app.mainloop()
