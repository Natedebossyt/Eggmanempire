import os
import wx
import wx.html2
import os
import threading
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

icon_path = ""

def set_custom_icon(self, icon_path):
    if os.path.exists(icon_path) and icon_path.lower().endswith('.ico'):
        try:
            icon = wx.Icon(icon_path, wx.BITMAP_TYPE_ICO)
            self.SetIcon(icon)
        except Exception as e:
            wx.MessageBox(f"Error setting icon: {str(e)}", "Icon Error", wx.OK | wx.ICON_ERROR)
    else:
        wx.MessageBox(f"Invalid or missing icon file: {icon_path}", "Icon Error", wx.OK | wx.ICON_ERROR)
