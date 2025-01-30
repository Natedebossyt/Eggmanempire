import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # Update time every second (1000 milliseconds)

# Create the main window
root = tk.Tk()
root.title("Time App")

# Create a label to display the time
time_label = tk.Label(root, font=("Arial", 24), bg="white", fg="black")
time_label.pack(pady=20)

# Start updating the time
update_time()

# Run the application
root.mainloop()