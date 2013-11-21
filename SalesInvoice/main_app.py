# coding : utf-8

import wx
from main_frame import MainFrame

class MainApp(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = MainFrame(None, "Hello World")

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()