import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the web engine view
        self.browser = QWebEngineView(self)

        # Set the URL to be opened
        self.browser.setUrl(QUrl("https://www.google.com"))  # Replace with the URL you want to open

        # Enable JavaScript if it's disabled by default
        settings = self.browser.settings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        # Handle page load finished event
        self.browser.loadFinished.connect(self.page_loaded)

        # Set the browser as the central widget
        self.setCentralWidget(self.browser)

    def page_loaded(self, success):
        if success:
            print("Page loaded successfully!")
        else:
            print("Failed to load the page.")

if __name__ == "__main__":
    # Initialize the application
    app = QApplication(sys.argv)

    # Create the browser window
    window = Browser()
    window.show()  # Show the browser window

    # Start the application's event loop
    sys.exit(app.exec_())
