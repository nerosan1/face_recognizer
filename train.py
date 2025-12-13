from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Pannel")

        #title section
        title_lb1 = Label(self.root,text="Welcome to Training Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()