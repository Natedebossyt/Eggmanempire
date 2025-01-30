from tkinter import colorchooser
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter
import webbrowser
import os
import tkinter as tk
import time

class Window(Frame):

    

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        time.sleep(4)
        messagebox.showwarning("Metal panel", "defensive mode active")