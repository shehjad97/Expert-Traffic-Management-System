import tkinter as tk					
from tkinter import ttk
# from main import webcam

root = tk.Tk()
root.geometry("1200x1200")
root.title("ETMS")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Home')
tabControl.add(tab2, text ='Data')
tabControl.add(tab3, text ='Chart')
tabControl.pack(expand = 1, fill ="both")

def button_clicked():
    print('Button clicked')
    # webcam()

button = tk.Button(tab1, text='Click Me', command=button_clicked)
button.pack()


# ttk.Label(tab1,text ="Welcome To Expert Traffic Management System").grid(column = 0,row = 0, padx = 30, pady = 30)
ttk.Label(tab2,text ="Lets dive into the world of computers").grid(column = 0,row = 0,padx = 30, pady = 30)

root.mainloop()