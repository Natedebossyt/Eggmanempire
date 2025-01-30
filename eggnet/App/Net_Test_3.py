import wx
import webview

class BrowserFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(800, 600))

        # Create a webview instance using PyWebView
        self.browser_window = webview.create_window("EGGNET 0.01", input("link here"), width=800, height=600)

        # Start the webview
        webview.start()

        self.Show(True)

class BrowserApp(wx.App):
    def OnInit(self):
        frame = BrowserFrame(None, "EGGNET 0.01")
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = BrowserApp(False)
    app.MainLoop()
