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

        messagebox.showinfo("missle panel","enter nuclear code(look in py panel)"); input("enter nuclear code now"); import launched

root = Tk()
app = Window(root)
root.wm_iconbitmap('C:\\Users\\bella\Downloads\\microwarelogo.bmp')
root.wm_title("DEATH EGG MOON")
root.geometry("1440x720")
root.mainloop()