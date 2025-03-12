
import os
import hashlib
import requests

API_KEY = "4d2512c06d5fe619a89ac1ed0a0f0b905c70938f909c8cb45c85b3030ce6713d"  # Get from VirusTotal
DIR_PATH = "C:"  # Replace with your directory path

def get_file_hash(file_path):
    """Compute SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error hashing {file_path}: {e}")
        return None

def check_virustotal(file_hash):
    """Check the hash against VirusTotal."""
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        positives = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious", 0)
        return positives
    elif response.status_code == 404:
        return "Not Found"
    else:
        return None

def scan_directory(directory):
    """Scan all files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Scanning: {file_path}")
            
            file_hash = get_file_hash(file_path)
            if not file_hash:
                continue
            
            result = check_virustotal(file_hash)
            if result == "Not Found":
                print(f"  [UNKNOWN] {file}")
            elif result is not None:
                print(f"  [DETECTED: {result} engines] {file}" if result > 0 else f"  [CLEAN] {file}")
            else:
                print(f"  [ERROR] Could not check {file}")

# Run the scan
scan_directory(DIR_PATH)

