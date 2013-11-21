# coding : utf-8

import wx
from order_form import OrderFormGrid

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="Soap", size=wx.DefaultSize)
        
        #create panel
        #self.__cretae_panel()
        #create tabs
        self.__create_tabs()
        
        #create menubar
        self.__create_menubar()
        
        #create toolbar
        self.__create_toobar()
        
        #create statusbar
        self.__create_statusbar()
        
        #show frame
        self.Show()

    def __create_menubar(self):
        self.menubar = wx.MenuBar()
        # file menu
        file_menu = wx.Menu()
        file_menu.Append(101, "&New", "")
        file_menu.AppendSeparator()
        exit_menu_item = file_menu.Append(wx.ID_EXIT, "E&xit", " Terminate Soap")
        # append file menu
        self.Bind(wx.EVT_CLOSE, self.on_exit, exit_menu_item)
        self.menubar.Append(file_menu, "&File")

        # edit menu
        edit_menu = wx.Menu()
        edit_menu.Append(201, "Hydrogen")
        edit_menu.Append(202, "Helium")
        # a submenu in edit menu
        submenu = wx.Menu()
        submenu.Append(2031,"Lanthanium")
        submenu.Append(2032,"Cerium")
        submenu.Append(2033,"Praseodymium")
        edit_menu.AppendMenu(203, "Lanthanides", submenu)
        # append edit menu
        self.menubar.Append(edit_menu, "&Edit")
        
        #help menu
        help_menu = wx.Menu()
        about_menu_item = help_menu.Append(wx.ID_ABOUT, "&About"," Information about Soap")
        self.Bind(wx.EVT_MENU, self.on_about, about_menu_item)
        # append help menu
        self.menubar.Append(help_menu, "&Help")

        self.SetMenuBar(self.menubar)
    
    def __cretae_panel(self):
        self.panel = wx.Panel(self, wx.ID_ANY)
        
        #create table
        self.__create_table()
    
    def __create_statusbar(self):
        self.CreateStatusBar()
    
    def __create_toobar(self):
        toolbar_flag = ( wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT)
        toolbar_size = (24, 24)
        self.toolbar = self.CreateToolBar(toolbar_flag)
        self.toolbar.SetToolBitmapSize(toolbar_size)
        #new label
        new_bmp =  wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, toolbar_size)
        self.toolbar.AddLabelTool(10, "New", new_bmp, shortHelp="New", longHelp="Long help for 'New'")
        #open label
        open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, toolbar_size)
        self.toolbar.AddLabelTool(20, "Open", open_bmp, shortHelp="Open", longHelp="Long help for 'Open'")
        
        #add separator
        self.toolbar.AddSeparator()
        
        #copy label
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, toolbar_size)
        self.toolbar.AddSimpleTool(30, copy_bmp, "Copy", "Long help for 'Copy'")
        #paste label
        paste_bmp= wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR, toolbar_size)
        self.toolbar.AddSimpleTool(40, paste_bmp, "Paste", "Long help for 'Paste'")
        
        
        #show toolbar
        self.toolbar.Realize()

    def __create_table(self):
        orderform_grid = OrderFormGrid(self.panel)
       
        self.panel.Sizer = wx.BoxSizer()
        self.panel.Sizer.Add(orderform_grid, 1, wx.EXPAND)
    
    def __create_tabs(self):
        pass
    
    def on_exit(self, event):
        print "exit"
        wx.Exit()
    
    def on_about(self, event):
        pass