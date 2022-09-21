import cv2

import numpy as np

from tkinter import *

from PIL import Image, ImageTk

import datetime

def capturetheimg():

    image= Image.fromarray(img1)

    time = str(datetime.datetime.now().today()).replace(":"," ")+".jpg"

    image.save(time)

root = Tk()

root.geometry("780x648")

root.configure(bg="black") 
Label(root, text="ETMS_CAM01", font=("times new roman", 38, "bold"), bg="black",fg="red").pack() 
f1=LabelFrame (root, bg="red")

f1.pack()

L1=Label(f1, bg="red") 
L1.pack()

cap = cv2.VideoCapture(0)

Button(root, text="Take Snapshot", font=("times new roman", 28, "bold"), bg="black", fg="red", command=capturetheimg).pack()
while True:
        img=cap.read()[1]

        img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        img=ImageTk. PhotoImage(Image.fromarray(img1)) 
        L1["image"]=img

        root.update()

cap.release()