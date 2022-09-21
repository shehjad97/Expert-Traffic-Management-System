# Import the required libraries
import tkinter as tk
from tkinter import ttk

import json

# # Create an instance of tkinter frame
# table = Tk()

# # Set the size of the tkinter window
# table.geometry("800x350")
# table.title("ETMS-Expert Traffic Management System")

# # Create an object of Style widget
# style = ttk.Style()
# style.theme_use('clam')

# # Add a Treeview widget
# tree = ttk.Treeview(table, column=("Serial", "License Number", "Cam", "Timestamp"), show='headings', height=15)
# tree.column("# 1", anchor=CENTER)
# tree.heading("# 1", text="Serial")
# tree.column("# 2", anchor=CENTER)
# tree.heading("# 2", text="License Number")
# tree.column("# 3", anchor=CENTER)
# tree.heading("# 3", text="Cam")
# tree.column("# 4", anchor=CENTER)
# tree.heading("# 4", text="Timestamp")

# with open('json_data.json', 'r') as openfile:
#     records = json.load(openfile)

# for record in records:
#     tree.insert('', 'end', text="1", values=(record['no'], record['license_number'], record['camera'], record['timestamp']))

# tree.pack()

# table.mainloop()

class Table(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the size of the tkinter window
        self.title("ETMS-Expert Traffic Management System")
        self.geometry("800x350")

        # Create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(self, column=("Serial", "License Number", "Cam", "Timestamp"), show='headings', height=15)
        tree.column("# 1", anchor="center")
        tree.heading("# 1", text="Serial")
        tree.column("# 2", anchor="center")
        tree.heading("# 2", text="License Number")
        tree.column("# 3", anchor="center")
        tree.heading("# 3", text="Cam")
        tree.column("# 4", anchor="center")
        tree.heading("# 4", text="Timestamp")

        with open('json_data.json', 'r') as openfile:
            records = json.load(openfile)

        for record in records:
            tree.insert('', 'end', text="1", values=(record['no'], record['license_number'], record['camera'], record['timestamp']))

        tree.pack()

        # self.mainloop()

if __name__ == '__main__':
    app = Table()
    app.mainloop()
