from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from matplotlib.figure import Figure
import tkinter as tk
import matplotlib
import pandas as pd
import json

matplotlib.use('TkAgg')

def get_month_count(month_str):
    with open('json_data.json', 'r') as openfile:
        records = json.load(openfile)
    
    months = []

    for record in records:
        month = record['timestamp'][3:5]
        months.append(month)

    months_counts = pd.Series(months).value_counts()
    if months_counts.get(month_str) == None:
        return 0
    else:
        return months_counts.get(month_str)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Traffic Density')

        # prepare data
        data = {
            '2016': 932147,
            '2017': 1042353,
            '2018': 1182063,
            '2019': 1353375,
            '2020': 1511782,
            '2021': 1630036,
        }
        languages = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('Yearly Traffic Data')
        axes.set_ylabel('(Number of Vehicles)')
        axes.set_xlabel('(Years)')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()
