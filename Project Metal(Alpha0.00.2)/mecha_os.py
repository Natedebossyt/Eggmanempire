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
        googlebutton = Button(self, text="Google", command=self.clickgoogleButton)

        newsbutton = Button(self, text="Fox News", command=self.clicknewsButton)

        wifibutton = Button(self, text="wfif connect", command=self.clickwifiButton)

        versionbutton = Button(self, text="OS version", command=self.clickversionButton)

        explorerbutton = Button(self, text="file explorer", command=self.clickexplorerButton)

        notebutton = Button(self, text="notepad app", command=self.clicknoteButton)

        otherbutton = Button(self, text="go back?", command=self.clickotherButton)

        filecheckbutton = Button(self, text="file check", command=self.clickfilecheckButton)

        filesaverbutton = Button(self, text="make file", command=self.clickfilesaveButton)

        timebutton = Button(self, text="time app", command=self.clicktimeButton)

        reportbutton = Button(self, text="report", command=self.clickreportbutton)

        updaterbutton = Button(self, text="update", command=self.clickupdaterButton)

        stickynotebutton = Button(self, text="sticky note", command=self.clickstickynoteButton)

        metaldefensive = Button (self, text="defensive mode", command=self.clickdefensiveButton)

        exitbutton = Button(self, text="power off", command=self.clickexitButton)

        # place button at 
        googlebutton.place(x=100, y=700)

        newsbutton.place(x=300, y=700)

        wifibutton.place(x=400, y=700)

        explorerbutton.place(x=600, y=700)

        notebutton.place(x=700, y=700)

        filecheckbutton.place(x=800, y=700)

        otherbutton.place(x=900, y=700)

        updaterbutton.place(x=300, y=600)

        timebutton.place(x=400, y=600)

        filesaverbutton.place(x=500, y=600)

        stickynotebutton.place(x=600, y=600)

        metaldefensive.place(x=700, y=600)

        versionbutton.place(x=1100, y=700)

        reportbutton.place(x=1000, y=700)

        exitbutton.place(x=1200, y=700)

    def clickgoogleButton(self):
        import googleguitest1

    def clicknewsButton(self):
        webbrowser.open("www.foxnews.com")

    def clickwifiButton(self):
        import wififorgui1

    def clickversionButton(self):
        messagebox.showinfo("Metal Panel"," build 0.00.2")

    def clickexplorerButton(self):
        import Main1061

    def clickfilecheckButton(self):
        import filenotfoundalertfile

    def clicknoteButton(self):
        import notepadgui1

    def clickupdaterButton(self):
        import updater1101    

    def clicktimeButton(self):
        import timeapp1051
    
    def clickotherButton(self):
        quit()

    def clickfilesaveButton(self):
       import file__saver1031

    def clickdefensiveButton(self):
       import Defensive_mode

    def clickreportbutton(self):
        import reportfile
        messagebox.showinfo("info box", "look in python termanal")
        
    def clickstickynoteButton(self):
        import Stickynote

    def clickexitButton(self):
        import signingoff; quit()

root = Tk()
app = Window(root)
root.wm_title("Metal Sonic Test Panel")
root.geometry("1920x1200")
root.mainloop()
Font_tuple = ("LightAir", 20, "bold")
