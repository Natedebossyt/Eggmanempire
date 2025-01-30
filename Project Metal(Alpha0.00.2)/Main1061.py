import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess
import platform

def open_file():
    filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Select File",
        filetypes=(("Text files", "*.txt"), ("all files", "*.*"))
    )
    if filepath:
        with open(filepath, 'r') as file:
            content = file.read()
        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, content)
        global last_opened_file
        last_opened_file = filepath

def open_directory():
    global current_directory
    directory = filedialog.askdirectory(
        initialdir="/",
        title="Select Directory"
    )
    if directory:
        current_directory = directory
        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, f"Contents of directory: {directory}\n")
        for item in os.listdir(directory):
            text_display.insert(tk.END, f"{item}\n")

def search_files():
    if current_directory:
        search_term = search_entry.get()
        if search_term:
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, f"Searching for '{search_term}' in directory: {current_directory}\n")
            for root, dirs, files in os.walk(current_directory):
                for file in files:
                    if search_term in file:
                        text_display.insert(tk.END, os.path.join(root, file) + "\n")
    else:
        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, "No directory selected. Please select a directory first.\n")

def open_with_default_app():
    if last_opened_file:
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', last_opened_file))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(last_opened_file)
        else:                                   # Linux
            subprocess.call(('xdg-open', last_opened_file))
    else:
        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, "No file selected. Please open a file first.\n")

app = tk.Tk()
app.title("File Manager")

current_directory = ""
last_opened_file = ""

open_file_button = tk.Button(app, text="Open File", padx=10, pady=5, command=open_file)
open_file_button.pack()

open_dir_button = tk.Button(app, text="Open Directory", padx=10, pady=5, command=open_directory)
open_dir_button.pack()

search_label = tk.Label(app, text="Search Files:")
search_label.pack()

search_entry = tk.Entry(app, width=50)
search_entry.pack()

search_button = tk.Button(app, text="Search", padx=10, pady=5, command=search_files)
search_button.pack()

open_with_default_button = tk.Button(app, text="Open with Default App", padx=10, pady=5, command=open_with_default_app)
open_with_default_button.pack()

text_display = Text(app, wrap=tk.WORD, padx=10, pady=5)
text_display.pack(expand=True, fill='both')

app.mainloop()