import os

def read_directory_contents(directory_path):
    """
    Reads the contents of a directory and lists all files and subdirectories.

    :param directory_path: The path of the directory to read.
    :return: A list of files and subdirectories in the directory.
    """
    try:
        # Get a list of all files and directories in the specified path
        contents = os.listdir(directory_path)
        
        # Separate the contents into files and directories
        files = [f for f in contents if os.path.isfile(os.path.join(directory_path, f))]
        directories = [d for d in contents if os.path.isdir(os.path.join(directory_path, d))]

        print(f"Contents of the directory: {directory_path}")
        print("\nDirectories:")
        for directory in directories:
            print(f"  - {directory}")
        
        print("\nFiles:")
        for file in files:
            print(f"  - {file}")
        
        return files, directories

    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' was not found.")
        return [], []
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")
        return [], []

# Example Usage
if __name__ == "__main__":
    # Replace this with the directory path you want to read
    directory_path = input("Enter the directory path to read: ")
    read_directory_contents(directory_path)