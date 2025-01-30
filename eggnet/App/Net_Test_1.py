import http.client
from urllib.parse import urlparse


def fetch_webpage(url):
    try:
        # Parse the URL into components
        parsed_url = urlparse(url)
        host = parsed_url.netloc
        path = parsed_url.path if parsed_url.path else "/"

        if not host:
            print("Invalid URL. Please make sure it starts with http:// or https://")
            return

        # Establish an HTTP connection
        connection = http.client.HTTPConnection(host)
        connection.request("GET", path)
        response = connection.getresponse()

        # Display basic response details
        print(f"Status: {response.status} {response.reason}")

        # Read and display the content
        content = response.read().decode(errors="ignore")
        print(content[:1000])  # Print the first 1000 characters
        connection.close()

    except Exception as e:
        print(f"Error fetching the webpage: {e}")


if __name__ == "__main__":
    url = input("Enter a URL (starting with http:// or https://): ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    fetch_webpage(url)
