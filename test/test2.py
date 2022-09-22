from tkinter import *
from tkinter import ttk
import time

def do_something():
   label.configure(text="Process Started")
   time.sleep(5) #some process/script that takes few seconds to execute
   label.configure(text="Process Completed")

root = Tk()

label = ttk.Label(root, text="Welcome")
label.pack()
button = ttk.Button(root, text="Click to Start Process", command=do_something)
button.pack()

root.mainloop()