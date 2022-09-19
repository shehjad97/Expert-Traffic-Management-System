from tkinter import *
# Table class
class Table:
    # Initialize a constructor
    def __init__(self, gui):

        # An approach for creating the table
        for i in range(total_rows):
            for j in range(total_columns):
                print(i)
                if i ==0:
                    self.entry = Entry(gui, width=20, bg='LightSteelBlue',fg='Black',
                                       font=('Arial', 16, 'bold'))
                else:
                    self.entry = Entry(gui, width=20,
                               font=('Arial', 16, ''))

                self.entry.grid(row=i, column=j)
                self.entry.insert(END, employee_list[i][j])


# take the data
employee_list = [('Name', 'City', 'Age'),
        ('Gorge', 'California', 30),
       ('Maria', 'New York', 19),
       ('Albert', 'Berlin', 22),
       ('Harry', 'Chicago', 19),
       ('Vanessa', 'Boston', 31),
       ('Ali', 'Karachi', 30)]

# find total number of rows and
# columns in list
total_rows = len(employee_list)
total_columns = len(employee_list[0])

# create root window
gui = Tk()
gui.geometry("780x648")
table = Table(gui)
gui.mainloop()