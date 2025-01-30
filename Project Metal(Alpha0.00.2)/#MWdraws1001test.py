#MWdraws1001test

import tkinter as tk
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename
import pillow as PIL
from PIL import ImageGrab

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint")
        self.root.geometry("600x400")

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.setup_menu()

        self.prev_x = None
        self.prev_y = None
        self.color = "black"
        self.line_width = 2

        self.canvas.bind("<B1-Motion>", self.draw)

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def draw(self, event):
        x, y = event.x, event.y
        if self.prev_x and self.prev_y:
            self.canvas.create_line(self.prev_x, self.prev_y, x, y, fill=self.color, width=self.line_width, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.prev_x = x
        self.prev_y = y

    def save(self):
        file_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            messagebox.showinfo("Info", "Image saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()