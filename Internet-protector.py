import requests
import time
import browser_cookie3
from urllib.parse import urlparse
import os
import sys
import ctypes

# Function to check if the script is running as admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

# Function to restart the script with admin rights
def run_as_admin():
    if not is_admin():
        print("Restarting with admin privileges...")
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, '"' + os.path.abspath(__file__) + '"', None, 1)
            sys.exit()  # Exit the current instance after launching the elevated one
        except Exception as e:
            print(f"Failed to elevate to admin: {e}")
            sys.exit(1)

# Function to log suspicious activity
def log_suspicious_activity(domain):
    try:
        with open("suspicious_activity.log", "a") as log_file:
            log_file.write(f"Suspicious domain detected: {domain} - {time.ctime()}\n")
    except OSError as e:
        print(f"Error writing to log file: {e}")

# Function to check if a domain is malicious using an online service
def is_malicious(domain):
    try:
        response = requests.get(f"https://www.virustotal.com/vtapi/v2/url/report", params={
            'apikey': '4d2512c06d5fe619a89ac1ed0a0f0b905c70938f909c8cb45c85b3030ce6713d',
            'resource': domain
        })
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get("positives", 0) > 0:
                return True
    except requests.RequestException as e:
        print(f"Error checking domain: {e}")
    return False

# Function to get the most recent URL from browser cookies
def get_recent_url():
    try:
        cj = browser_cookie3.load()
        for cookie in cj:
            if 'youtube.com' in cookie.domain or 'google.com' in cookie.domain:
                return f"https://{cookie.domain}{cookie.path}"
    except Exception as e:
        print(f"Error getting recent URL: {e}")
    return None

# Function to get the domain from a URL
def get_domain_from_url(url):
    try:
        parsed_url = urlparse(url)
        return parsed_url.netloc
    except Exception:
        return None

# Main loop to monitor internet activity
def monitor_internet_activity():
    print("Active Internet Protector is running...")
    while True:
        url = get_recent_url()
        if url:
            domain = get_domain_from_url(url)
            if domain:
                if is_malicious(domain):
                    print(f"Warning! The domain {domain} is marked as malicious.")
                    log_suspicious_activity(domain)
                else:
                    print(f"The domain {domain} appears to be safe.")
        time.sleep(5)  # Adjust the check interval as needed

# Run the monitoring function
if __name__ == "__main__":
    run_as_admin()
    if is_admin():
        monitor_internet_activity()
    else:
        print("Failed to obtain admin rights. Exiting...")
        sys.exit(1)
