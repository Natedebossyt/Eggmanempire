from tkinter import colorchooser
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter
import webbrowser
import os
import tkinter as tk

class Window(Frame):

    

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        

        # create button, link it to clickExitButton()
        defense1 = Button(self, text="defensive", command=self.clickdefenseButton)

        defense1.place(x=100, y=700)
 
        def clickdefenseButton(self):
            
        