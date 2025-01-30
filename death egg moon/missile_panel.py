import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
import os

class Window(Frame):

    

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        googlebutton = Button(self, text="launch 1kt", command=self.clickgoogleButton)

        googlebutton.place(x=100, y=700)

    def clickgoogleButton(self):
         messagebox.showwarning("missile panel","are you sure?"); import missile_code

root = Tk()
app = Window(root)
root.wm_iconbitmap('C:\\Users\\bella\Downloads\\microwarelogo.bmp')
root.wm_title("DEATH EGG MOON")
root.geometry("1440x720")
root.mainloop()

