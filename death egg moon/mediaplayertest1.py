import os
from import pygame

class MediaPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        self.current_index = -1

    def add_to_playlist(self, file_path):
        if os.path.exists(file_path):
            self.playlist.append(file_path)
            print(f"Added '{file_path}' to the playlist.")
        else:
            print("File not found.")

    def play(self, index):
        if 0 <= index < len(self.playlist):
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
            self.current_index = index
            pygame.mixer.music.load(self.playlist[index])
            pygame.mixer.music.play()
            print(f"Now playing: {self.playlist[index]}")
        else:
            print("Invalid index.")

    def pause(self):
        pygame.mixer.music.pause()
        print("Playback paused.")

    def resume(self):
        pygame.mixer.music.unpause()
        print("Playback resumed.")

    def stop(self):
        pygame.mixer.music.stop()
        print("Playback stopped.")

    def display_playlist(self):
        print("Playlist:")
        for i, file_path in enumerate(self.playlist):
            print(f"{i}: {file_path}")

# Example usage:
player = MediaPlayer()

# Add audio files to the playlist
player.add_to_playlist("song1.mp3")
player.add_to_playlist("song2.mp3")

# Display the playlist
player.display_playlist()

# Play the first song
player.play(0)

# Pause playback
player.pause()

# Resume playback
player.resume()

# Stop playback
player.stop()