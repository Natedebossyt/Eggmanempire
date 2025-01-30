import hashlib
import os

def generate_hash(file_path):
    """Generates a SHA-256 hash for the given file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def check_integrity(directory):
    """Checks integrity of files by printing their hashes."""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = generate_hash(file_path)
            print(f"{file_path}: {file_hash}")

if __name__ == "__main__":
    directory = os.path.abspath("E:\Eggman empire\Project Metal(Alpha0.00.1)")  # Automatically set the folder to check
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
    else:
        check_integrity(directory); import mechaoslogin