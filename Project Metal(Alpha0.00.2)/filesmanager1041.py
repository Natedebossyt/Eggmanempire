import os
import shutil

class FileManager:
    def __init__(self):
        self.current_directory = os.getcwd()

    def list_directory(self):
        files = os.listdir(self.current_directory)
        for file in files:
            print(file)

    def change_directory(self, directory):
        new_path = os.path.join(self.current_directory, directory)
        if os.path.isdir(new_path):
            self.current_directory = new_path
            print(f"Changed directory to: {self.current_directory}")
        else:
            print(f"Error: '{directory}' is not a valid directory.")

    def create_directory(self, directory_name):
        new_directory_path = os.path.join(self.current_directory, directory_name)
        os.makedirs(new_directory_path)
        print(f"Created directory: {new_directory_path}")

    def delete_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print(f"Error: '{file_name}' not found.")

    def copy_file(self, source_file, destination_file):
        source_path = os.path.join(self.current_directory, source_file)
        destination_path = os.path.join(self.current_directory, destination_file)
        if os.path.exists(source_path):
            shutil.copy2(source_path, destination_path)
            print(f"Copied '{source_file}' to '{destination_file}'")
        else:
            print(f"Error: Source file '{source_file}' not found.")

if __name__ == "__main__":
    file_manager = FileManager()

    while True:
        print("\nCurrent Directory:", file_manager.current_directory)
        print("1. List directory contents")
        print("2. Change directory")
        print("3. Create directory")
        print("4. Delete file/directory")
        print("5. Copy file")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_manager.list_directory()
        elif choice == "2":
            directory = input("Enter directory name: ")
            file_manager.change_directory(directory)
        elif choice == "3":
            directory_name = input("Enter directory name to create: ")
            file_manager.create_directory(directory_name)
        elif choice == "4":
            file_name = input("Enter file/directory name to delete: ")
            file_manager.delete_file(file_name)
        elif choice == "5":
            source_file = input("Enter source file name: ")
            destination_file = input("Enter destination file name: ")
            file_manager.copy_file(source_file, destination_file)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")