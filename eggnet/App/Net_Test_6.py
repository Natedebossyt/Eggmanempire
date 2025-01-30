import wx
import wx.html2
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import os

class FileServerThread(threading.Thread):
    def __init__(self, directory="shared_files", port=8080):
        super().__init__()
        self.directory = directory
        self.port = port
        os.makedirs(directory, exist_ok=True)

    def run(self):
        os.chdir(self.directory)
        server = HTTPServer(("0.0.0.0", self.port), SimpleHTTPRequestHandler)
        print(f"Serving files on port {self.port}...")
        server.serve_forever()

class BrowserFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="EGGNET 0.05", size=(900, 700))

        # Set the application icon
        icon = wx.Icon("E:\Eggman empire\eggnet\App\eggman_icon2.ico", wx.BITMAP_TYPE_ICO)  # Specify your icon file path here
        self.SetIcon(icon)

        # Create layout
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Toolbar
        toolbar = wx.BoxSizer(wx.HORIZONTAL)

        # Back button
        back_btn = wx.Button(self, label="Back")
        back_btn.Bind(wx.EVT_BUTTON, self.go_back)
        toolbar.Add(back_btn, flag=wx.LEFT, border=5)

        # Forward button
        forward_btn = wx.Button(self, label="Forward")
        forward_btn.Bind(wx.EVT_BUTTON, self.go_forward)
        toolbar.Add(forward_btn, flag=wx.LEFT, border=5)

        # Refresh button
        refresh_btn = wx.Button(self, label="Refresh")
        refresh_btn.Bind(wx.EVT_BUTTON, self.refresh_page)
        toolbar.Add(refresh_btn, flag=wx.LEFT, border=5)

        # Start File Server button
        file_server_btn = wx.Button(self, label="Start File Server")
        file_server_btn.Bind(wx.EVT_BUTTON, self.start_file_server)
        toolbar.Add(file_server_btn, flag=wx.LEFT, border=5)

        # Search bar
        self.url_bar = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.url_bar.Bind(wx.EVT_TEXT_ENTER, self.load_page)
        toolbar.Add(self.url_bar, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        vbox.Add(toolbar, flag=wx.EXPAND)

        # Browser control
        self.browser = wx.html2.WebView.New(self)
        vbox.Add(self.browser, proportion=1, flag=wx.EXPAND)

        # Set initial URL
        self.browser.LoadURL("bing.com")

        # Set layout
        self.SetSizer(vbox)
        self.Show()

    def start_file_server(self, event):
            wx.MessageBox(f"File server started! Access it at https://github.com/Natedebossyt/Eggmanempire", "Server Info", wx.OK)
            self.browser.LoadURL("https://github.com/Natedebossyt/Eggmanempire")


        

    def load_page(self, event):
        url = self.url_bar.GetValue()
        if not url.startswith("http"):
            url = f"http://{url}"
        self.browser.LoadURL(url)
        self.SetTitle(f"Browser - {url}")

    def refresh_page(self, event):
        self.browser.Reload()

    def go_back(self, event):
        """Navigate back in the browser history."""
        if self.browser.CanGoBack():
            self.browser.GoBack()

    def go_forward(self, event):
        """Navigate forward in the browser history."""
        if self.browser.CanGoForward():
            self.browser.GoForward()

class BrowserApp(wx.App):
    def OnInit(self):
        frame = BrowserFrame()
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = BrowserApp()
    app.MainLoop()
