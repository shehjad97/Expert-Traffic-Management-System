import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class PieChart(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Traffic Density')

        fig = matplotlib.figure.Figure(figsize=(5, 5))
        ax = fig.add_subplot(111)

        ax.pie([13, 8, 17, 14, 7, 18, 13, 10])
        ax.legend(["DHA01 (13%)", "DHA02 (8%)", "DHA03 (17%)", "DHA04 (14%)", "DHA05 (7%)", "DHA06 (18%)", "DHA07 (13%)", "DHA08 (10%)"], loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, shadow=True)

        circle = matplotlib.patches.Circle((0, 0), 0.0, color='white')
        ax.add_artist(circle)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack()
        canvas.draw()

if __name__ == '__main__':
    app = PieChart()
    app.mainloop()
