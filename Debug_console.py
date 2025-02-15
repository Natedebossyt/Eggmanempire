from tkinter import colorchooser
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter
import webbrowser
import os
import tkinter as tk
import time
import os
import subprocess
import sys
import win32gui
import win32con
import win32api


print("DEBUG PANEL 0.01")

while True:
    print ("1. file integrity check.",
           "2. file permissions.",
           "3. open file admin mode.",
           "4. run a windows command.",
           "5. exit debug.")
    choice = input("Choose an option: ").strip()

    if choice == '1':
        import os
        import json

        def scan_directory(directory):
            file_data = {}
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    file_data[file_path] = file_size
            return file_data

        def save_baseline(directory, baseline_file='integrity_baseline.json'):
            file_data = scan_directory(directory)
            with open(baseline_file, 'w') as f:
                json.dump(file_data, f, indent=4)
            print("Baseline integrity file saved.")

        def check_integrity(directory, baseline_file='integrity_baseline.json'):
            if not os.path.exists(baseline_file):
                print("Baseline file not found. Please create one first.")
                return

            with open(baseline_file, 'r') as f:
                baseline_data = json.load(f)

            current_data = scan_directory(directory)

            for file, old_size in baseline_data.items():
                if file not in current_data:
                    print(f"Missing file: {file}")
                elif current_data[file] != old_size:
                    print(f"Modified file: {file}")

            for file in current_data:
                if file not in baseline_data:
                    print(f"New file detected: {file}")

            print("Integrity check complete.")

        def main():
            directory = input("Enter the directory to monitor: ")
            action = input("Enter 'save' to create a baseline or 'check' to verify integrity: ").strip().lower()

            if action == 'save':
                save_baseline(directory)
            elif action == 'check':
                check_integrity(directory)
            else:
                print("Invalid action. Use 'save' or 'check'.")

        if __name__ == "__main__":
            main()

    elif choice == '2':
        import os
        import shutil
        import stat
        import argparse

        def change_owner(file_path, user, group):
            try:
                shutil.chown(file_path, user=user, group=group)
                print(f"Successfully changed owner to {user}:{group} for {file_path}")
            except Exception as e:
                print(f"Error changing owner: {e}")

        def change_permissions(file_path, permission):
            try:
                os.chmod(file_path, int(permission, 8))
                print(f"Successfully changed permissions to {permission} for {file_path}")
            except Exception as e:
                print(f"Error changing permissions: {e}")

        if __name__ == "__main__":
            parser = argparse.ArgumentParser(description="Change file owner and permissions.")
            parser.add_argument("file", help="Path to the file")
            parser.add_argument("--user", help="New owner username", required=False)
            parser.add_argument("--group", help="New group name", required=False)
            parser.add_argument("--perm", help="New file permissions in octal (e.g., 755)", required=False)

            args = parser.parse_args()

            if args.user or args.group:
                change_owner(args.file, args.user, args.group)

            if args.perm:
                change_permissions(args.file, args.perm)

    elif choice == '3':
        def open_file_as_admin(file_path):
            try:
                # Use 'runas' to request admin privileges directly from Python
                subprocess.run(["runas", "/user:Administrator", f"notepad {file_path}"], check=True, shell=True)
            except subprocess.CalledProcessError:
                print("Failed to open file with admin privileges.")
            except Exception as e:
                print(f"An error occurred: {e}")

        if __name__ == "__main__":
            if len(sys.argv) < 2:
                print("Usage: python script.py <file_path>")
            else:
                file_path = sys.argv[1]
                open_file_as_admin(file_path)

    elif choice == '4':
        time.sleep(2)  # Delay to ensure smooth execution

        # Simulate Win + R keypress
        win32api.keybd_event(win32con.VK_LWIN, 0, 0, 0)  # Press Win key
        win32api.keybd_event(ord('R'), 0, 0, 0)  # Press R key
        win32api.keybd_event(ord('R'), 0, win32con.KEYEVENTF_KEYUP, 0)  # Release R key
        win32api.keybd_event(win32con.VK_LWIN, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release Win key

    elif choice == '5':
        print("Exiting debug mode...")
        time.sleep(5)
        quit()
