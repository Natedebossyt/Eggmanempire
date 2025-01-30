import wx
import wx.html2

class BrowserFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="EGGNET 0.02", size=(900, 700))

        # Create layout
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Search bar
        self.url_bar = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.url_bar.Bind(wx.EVT_TEXT_ENTER, self.load_page)
        vbox.Add(self.url_bar, flag=wx.EXPAND | wx.ALL, border=5)

        # Browser control
        self.browser = wx.html2.WebView.New(self)
        vbox.Add(self.browser, proportion=1, flag=wx.EXPAND)

        # Set initial URL
        self.browser.LoadURL(input("LINK HERE >>> "))

        # Set layout
        self.SetSizer(vbox)
        self.Show()

    def load_page(self, event):
        url = self.url_bar.GetValue()
        if not url.startswith("http"):
            url = f"https://{url}"
        self.browser.LoadURL(url)
        self.SetTitle(f"Browser - {url}")


class BrowserApp(wx.App):
    def OnInit(self):
        frame = BrowserFrame()
        frame.Show(True)
        return True


if __name__ == "__main__":
    app = BrowserApp()
    app.MainLoop()
