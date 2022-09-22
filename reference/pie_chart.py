import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = matplotlib.figure.Figure(figsize=(5,5))
ax = fig.add_subplot(111)
ax.pie([37,18,35]) 
ax.legend(["DHA01 (37%)","DHA02 (28%)","DHA03 (35%)"])

circle=matplotlib.patches.Circle( (0,0), 0.0, color='white')
ax.add_artist(circle)

window= tk.Tk()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()
canvas.draw()
window.mainloop()