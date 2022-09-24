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

class MonthlyChart(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Traffic Density')

        # prepare data
        data = {
            'Jan': get_month_count('01'),
            'Feb': get_month_count('02'),
            'Mar': get_month_count('03'),
            'Apr': get_month_count('04'),
            'May': get_month_count('05'),
            'Jun': get_month_count('06'),
            'Jul': get_month_count('07'),
            'Aug': get_month_count('08'),
            'Sep': get_month_count('09'),
            'Oct': get_month_count('10'),
            'Nov': get_month_count('11'),
            'Dec': get_month_count('12'),
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
        axes.set_title('Monthly Traffic Data')
        axes.set_ylabel('(Number of Vehicles)')
        axes.set_xlabel('(Months)')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    app = MonthlyChart()
    app.mainloop()
