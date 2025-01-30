import tkinter as tk
from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk  # Import Pillow for image handling

def show_custom_warning():
    # Create a custom warning window
    warning_window = Toplevel(root)
    warning_window.title("EGGNET 0.05")
    warning_window.geometry("350x200")
    warning_window.configure(bg="White")

    # Load and display the image using Pillow
    img = Image.open("E:/Eggman empire/eggnet/App/MetalSonic3.png")
    img = img.resize((100, 100))  # Resize for better display
    img_tk = ImageTk.PhotoImage(img)

    image_label = Label(warning_window, image=img_tk, bg="White")
    image_label.image = img_tk  # Keep a reference to avoid garbage collection
    image_label.pack(pady=5)

    # Display a warning message
    message_label = Label(
        warning_window, text="Do not share files if you aren't sure what you are doing. If you do, continue.", font=("Arial", 14), bg="white"
    )
    message_label.pack()

    # Close the entire application 2 seconds after clicking OK
    def stop_program():
        root.after(2000, root.destroy)  # Close entire program after 2 seconds

    Button(warning_window, text="OK", command=stop_program).pack(pady=10)

root = tk.Tk()
root.title("Main Window")

Button(root, text="Show Warning", command=show_custom_warning).pack(pady=20)

root.mainloop()

