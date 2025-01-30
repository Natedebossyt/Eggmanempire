class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class StorageManager:
    def __init__(self, total_capacity):
        self.total_capacity = total_capacity
        self.available_capacity = total_capacity
        self.files = []

    def store_file(self, file):
        if file.size <= self.available_capacity:
            self.files.append(file)
            self.available_capacity -= file.size
            print(f"File '{file.name}' stored successfully.")
        else:
            print("Insufficient storage space.")

    def delete_file(self, file_name):
        for file in self.files:
            if file.name == file_name:
                self.files.remove(file)
                self.available_capacity += file.size
                print(f"File '{file_name}' deleted successfully.")
                return
        print(f"File '{file_name}' not found.")

    def list_files(self):
        print("Files in storage:")
        for file in self.files:
            print(f"Name: {file.name}, Size: {file.size} bytes")

# Example usage:
storage_manager = StorageManager(total_capacity=1000)  # Total capacity in bytes

# Store files
file1 = File("document1.txt", 200)
storage_manager.store_file(file1)

file2 = File("image.jpg", 500)
storage_manager.store_file(file2)

# List files
storage_manager.list_files()

# Delete a file
storage_manager.delete_file("document1.txt")

# List files after deletion
storage_manager.list_files()

import kernal