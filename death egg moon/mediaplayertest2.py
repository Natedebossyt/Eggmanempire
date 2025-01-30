import tkinter as tk
import vlc
from tkinter import filedialog
from datetime import timedelta

class MediaPlayerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Media Player")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")
        self.initialize_player()

    def initialize_player(self):
        self.instance = vlc.Instance()
        self.media_player = self.instance.media_player_new()
        self.current_file = None
        self.playing_video = False
        self.video_paused = False
        self.create_widgets()

    def create_widgets(self):
        # Create a canvas widget to display the video
        self.canvas = tk.Canvas(self, bg="black", width=640, height=480)
        self.canvas.pack(pady=20)

        # Create a Select File button
        self.select_file_button = tk.Button(self, text="Select File", font=("Helvetica", 12), command=self.select_file)
        self.select_file_button.pack()

        # Create a label to display time elapsed and duration
        self.time_label = tk.Label(self, text="00:00 / 00:00", font=("Helvetica", 12), fg="blue", bg="#f0f0f0")
        self.time_label.pack()

    def select_file(self):
        # Open a file dialog to select a video file
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
        if file_path:
            self.current_file = file_path
            self.play_video()

    def play_video(self):
        if self.current_file:
            self.media = self.instance.media_new(self.current_file)
            self.media_player.set_media(self.media)
            self.media_player.set_hwnd(self.canvas.winfo_id())
            self.media_player.play()
            self.playing_video = True
            self.update_time()

    def update_time(self):
        if self.playing_video:
            time_elapsed = timedelta(seconds=int(self.media_player.get_time() / 1000))
            duration = timedelta(seconds=int(self.media_player.get_length() / 1000))
            self.time_label.config(text=f"{time_elapsed} / {duration}")
            self.after(1000, self.update_time)

if __name__ == "__main__":
    app = MediaPlayerApp()
    app.mainloop()