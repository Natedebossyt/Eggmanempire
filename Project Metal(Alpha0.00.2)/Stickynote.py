import tkinter as tk
from tkinter import simpledialog, messagebox

class StickyNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticky Note App")
        
        self.notes = []
        
        self.add_button = tk.Button(self.root, text="Add Note", command=self.add_note)
        self.add_button.pack(pady=10)
        
        self.notes_frame = tk.Frame(self.root)
        self.notes_frame.pack(padx=10, pady=10)

    def add_note(self):
        note_text = simpledialog.askstring("Input", "Enter your note:")
        if note_text:
            self.create_note_widget(note_text)
            self.notes.append(note_text)
    
    def create_note_widget(self, text):
        note_frame = tk.Frame(self.notes_frame, bg="#fff8c4", bd=1, relief="solid")
        note_frame.pack(padx=5, pady=5, fill="both")
        
        note_text = tk.Text(note_frame, wrap="word", height=5, bg="#fff8c4", borderwidth=0)
        note_text.insert("1.0", text)
        note_text.pack(expand=True, fill="both")
        
        delete_button = tk.Button(note_frame, text="Delete", command=lambda: self.delete_note_widget(note_frame, note_text.get("1.0", "end-1c")))
        delete_button.pack()

    def delete_note_widget(self, note_frame, text):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this note?"):
            self.notes.remove(text)
            note_frame.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StickyNoteApp(root)
    root.mainloop()
