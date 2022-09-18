import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('ETMS - Expert Traffic Manangement System')
root.geometry("780x648")
Label(root, text="ETMS_CAM01").pack() 

def button_clicked():
    print('Button clicked')

button = Button(root, text='Click Me', command=button_clicked)
button.pack()

root.mainloop()