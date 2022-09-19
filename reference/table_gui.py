# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(win, column=("FName", "LName", "Roll No"), show='headings', height=5)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="FName")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="LName")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Roll No")

# Insert the data in Treeview widget
tree.insert('', 'end', text="1", values=('Amit', 'Kumar', '17701'))
tree.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
tree.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
tree.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))

tree.pack()

win.mainloop()