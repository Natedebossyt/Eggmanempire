import tkinter as tk
from tkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Save As",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    # You can write your text content to the selected file here

# Create a simple Tkinter window
root = tk.Tk()
root.title("Save File Example")

# Add a button to trigger the save_file function
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

root.mainloop()