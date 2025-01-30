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
        googlebutton = Button(self, text="Google", command=self.clickgoogleButton)

        calcbutton = Button(self, text="Calculator", command=self.clickcalcButton)

        newsbutton = Button(self, text="Fox News", command=self.clicknewsButton)

        wifibutton = Button(self, text="wfif connect", command=self.clickwifiButton)

        piechartbutton = Button(self, text="pie charts", command=self.clickpieButton)

        versionbutton = Button(self, text="OS version", command=self.clickversionButton)

        explorerbutton = Button(self, text="file explorer", command=self.clickexplorerButton)

        notebutton = Button(self, text="notepad app", command=self.clicknoteButton)

        otherbutton = Button(self, text="go back?", command=self.clickotherButton)

        mwdrawsbutton = Button(self, text="mwdraw pad", command=self.clickmwdrawsButton)

        filecheckbutton = Button(self, text="file check", command=self.clickfilecheckButton)

        filesaverbutton = Button(self, text="make file", command=self.clickfilesaveButton)

        calendarbutton = Button(self, text="calendar", command=self.clickcalButton)

        launchbutton = Button(self, text="launch missles", command=self.clicklaunchButton)

        exitbutton = Button(self, text="power off", command=self.clickexitButton)

        # place button at 
        googlebutton.place(x=100, y=700)

        calcbutton.place(x=200, y=700)

        newsbutton.place(x=300, y=700)

        wifibutton.place(x=400, y=700)

        piechartbutton.place(x=500, y=700)

        explorerbutton.place(x=600, y=700)

        notebutton.place(x=700, y=700)

        filecheckbutton.place(x=800, y=700)

        otherbutton.place(x=900, y=700)

        mwdrawsbutton.place(x=100, y=600)

        calendarbutton.place(x=200, y=600)

        filesaverbutton.place(x=300, y=600)

        launchbutton.place(x=400, y=600)

        versionbutton.place(x=1100, y=700)

        exitbutton.place(x=1200, y=700)

    def clickgoogleButton(self):
        import googleguitest1
        
    def clickcalcButton(self):
        import calculatorguitest1

    def clicknewsButton(self):
        webbrowser.open("www.foxnews.com")

    def clickwifiButton(self):
        import wififorgui1

    def clickpieButton(self):
        import piecharttest1

    def clickversionButton(self):
        messagebox.showinfo("EGG PANEL", "DEATH EGG MOON PANEL version 1.01")

    def clickexplorerButton(self):
       import filesmanager1041

    def clickfilecheckButton(self):
        import filecheck

    def clicknoteButton(self):
        import notepadgui1

    def clickmwdrawsButton(self):
        import MWdraws    

    def clickcalButton(self):
        import calendar

    def clickotherButton(self):
        quit()

    def clickfilesaveButton(self):
       import file__saver1031

    def clicklaunchButton(self):
        import missile_panel

    def clickexitButton(self):
        import signingoff; quit()

root = Tk()
app = Window(root)
root.wm_iconbitmap('C:\\Users\\bella\Downloads\\microwarelogo.bmp')
root.wm_title("DEATH EGG MOON")
root.geometry("1440x720")
root.mainloop()

