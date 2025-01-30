import time
import os

def check_file_integrity(file_path):
    """Check if a file can be read without errors."""
    try:
        print(f"Checking file: {file_path}")
        print(f"Readable: {os.access(file_path, os.R_OK)}")
        print(f"Exists: {os.path.exists(file_path)}")
        
        with open(file_path, "rb") as f:
            f.read()  # Attempt to read the entire file
        print(f"The file '{file_path}' is accessible and intact.")
        return True
    except Exception as e:
        print(f"Error accessing file '{file_path}': {e}")
        return False

if __name__ == "__main__":
    file_paths = [
        "E:\Eggman empire\Project Metal(Alpha0.00.2)",
    ]

    for file_path in file_paths:
        check_file_integrity(file_path)

print("please wait while we get your OS ready.")

time.sleep(8)

import Logingui2