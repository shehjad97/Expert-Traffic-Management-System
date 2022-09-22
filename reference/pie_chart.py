import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = matplotlib.figure.Figure(figsize=(5,5))
ax = fig.add_subplot(111)
ax.pie([13,8,17,14,7,18,13,10]) 
ax.legend(["DHA01 (13%)","DHA02 (8%)","DHA03 (17%)","DHA04 (14%)","DHA05 (7%)","DHA06 (18%)","DHA07 (13%)","DHA08 (10%)"])

circle=matplotlib.patches.Circle( (0,0), 0.0, color='white')
ax.add_artist(circle)

window= tk.Tk()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()
canvas.draw()
window.mainloop()