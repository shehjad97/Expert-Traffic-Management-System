# Imports
import tkinter as tk					
from tkinter import ttk

class Help(tk.Tk):
    def __init__(self):
        super().__init__()

        # Root Initialization
        self.title('Help')

        self.geometry("650x550")


        parent = ttk.Frame(self)

        label_texts = """ Jan: 1234  | Feb: 1234

 Mar: 1234  | Apr: 1234

 May: 1234  | Jun: 1234

 Jul: 1234    | Aug: 1234

 Sep: 1234  | Oct: 1234

 Nov: 1234  | Dec: 1234

        """
        label_texts1 = """ Sat: 1234         Sun: 1234       Mon: 1234       Tue: 1234 

 Wed: 1234       Thu: 1234       Fri: 1234 

   



         


        """

        # Labels
        ttk.Label(parent, text="Monthly",font=("Arial", 18)).pack(pady=25)
        ttk.Label(parent, text=label_texts,font=("Arial", 12)).pack(padx=(50,0),pady=5)
        ttk.Label(parent, text="Weekly",font=("Arial", 18)).pack(pady=25)
        ttk.Label(parent, text=label_texts1,font=("Arial", 12)).pack(padx=(50,0),pady=5)

        # Buttons
        tk.Button(parent, text="Back",font="sans 10 bold",bg="#ddd",width=12, command=self.destroy).pack(pady=15)

        parent.pack(expand=1)

if __name__ == '__main__':
    app = Help()
    app.mainloop()