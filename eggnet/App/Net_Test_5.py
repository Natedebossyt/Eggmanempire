import wx
import wx.html2
import os

class BrowserFrame(wx.Frame):
    ICON_PATH = "E:\Eggman empire\eggnet\App\eggman_icon2.ico"  # Set your custom icon path here

    def __init__(self):
        super().__init__(None, title="EGGNET 0.05", size=(900, 700))

        # Set the custom icon
        self.set_custom_icon(self.ICON_PATH)

        # Create layout
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Toolbar for navigation and search
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

        # Search bar
        self.url_bar = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.url_bar.Bind(wx.EVT_TEXT_ENTER, self.load_page)
        toolbar.Add(self.url_bar, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        vbox.Add(toolbar, flag=wx.EXPAND)

        # Browser control
        self.browser = wx.html2.WebView.New(self)
        vbox.Add(self.browser, proportion=1, flag=wx.EXPAND)

        # Set initial URL
        self.browser.LoadURL("https://www.example.com")

        # Set layout
        self.SetSizer(vbox)
        self.Show()

    def set_custom_icon(self, icon_path):
        """Set a custom icon from the specified path."""
        if os.path.exists(icon_path) and icon_path.lower().endswith('.ico'):
            try:
                icon = wx.Icon(icon_path, wx.BITMAP_TYPE_ICO)
                self.SetIcon(icon)
            except Exception as e:
                wx.MessageBox(f"Error setting icon: {str(e)}", "Icon Error", wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox("Invalid or missing icon file. Please use a valid .ico file.", 
                           "Icon Error", wx.OK | wx.ICON_ERROR)

    def load_page(self, event):
        url = self.url_bar.GetValue()
        if not url.startswith("http"):
            url = f"https://{url}"
        self.browser.LoadURL(url)
        self.SetTitle(f"Browser - {url}")

    def go_back(self, event):
        if self.browser.CanGoBack():
            self.browser.GoBack()

    def go_forward(self, event):
        if self.browser.CanGoForward():
            self.browser.GoForward()

    def refresh_page(self, event):
        self.browser.Reload()


class BrowserApp(wx.App):
    def OnInit(self):
        frame = BrowserFrame()
        frame.Show(True)
        return True


if __name__ == "__main__":
    app = BrowserApp()
    app.MainLoop()
