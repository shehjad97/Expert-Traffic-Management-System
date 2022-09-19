# Import the required libraries
from tkinter import *
from tkinter import ttk

import json

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(win, column=("Serial", "License Number", "Timestamp"), show='headings', height=15)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Serial")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="License Number")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Timestamp")

with open('json_data.json', 'r') as openfile:
        records = json.load(openfile)

for record in records:
    # print(record['timestamp'])
    tree.insert('', 'end', text="1", values=(record['no'], record['license_number'], record['timestamp']))

# # Insert the data in Treeview widget
# tree.insert('', 'end', text="1", values=('Amit', 'Kumar', '17701'))
# tree.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
# tree.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
# tree.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))

tree.pack()

win.mainloop()