import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from utils import cam_data

class PieChart(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Traffic Distribution Based on Cameras')

        fig = matplotlib.figure.Figure(figsize=(5, 5))
        ax = fig.add_subplot(111)

        data = cam_data()
        data_percentage = [each["counts"] for each in data]
        data_legend = [f'{each["name"]} ({each["counts"]}%)' for each in data]

        ax.pie(data_percentage)
        ax.legend(data_legend, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, shadow=True)

        circle = matplotlib.patches.Circle((0, 0), 0.0, color='white')
        ax.add_artist(circle)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack()
        canvas.draw()

if __name__ == '__main__':
    app = PieChart()
    app.mainloop()
