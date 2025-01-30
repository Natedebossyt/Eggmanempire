import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple PyQt Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Create a QWebEngineView widget
        self.browser = QWebEngineView()

        # Set a default URL
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Set the browser widget as the central widget
        self.setCentralWidget(self.browser)

        # Create a navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # URL input field
        self.url_input = QLineEdit()
        self.url_input.returnPressed.connect(self.load_url_from_input)
        navbar.addWidget(self.url_input)

        # Connect the URL field to the browser URL
        self.browser.urlChanged.connect(self.update_url_input)

    def load_url_from_input(self):
        url = self.url_input.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url  # Add 'http://' if missing
        self.browser.setUrl(QUrl(url))

    def update_url_input(self, q):
        self.url_input.setText(q.toString())

# Initialize the application
app = QApplication(sys.argv)
QApplication.setApplicationName("PyQt Browser")

# Create the main window
window = Browser()

# Show the window
window.show()

# Run the application's event loop
try:
    app.exec_()
except Exception as e:
    print(f"Error: {e}")
