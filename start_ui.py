#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20130414
#  @date          20140907 - Enhanced "stop download" feature
"""
UI for windows application
"""

import threading

import wx

import configure as conf
from gplus_crawler import GplusCrawler

class CountingThread(threading.Thread):
    def __init__(self, crawler, picasa_id, d_type):
        threading.Thread.__init__(self)
        self._crawler = crawler
        self._picasa_id = picasa_id
        self._download_type = d_type

    def run(self):
        print(self._crawler.main(self._picasa_id, self._download_type))

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, pos=(400, 400), size=(600, 250))

        # A button
        self.button = wx.Button(self, label="Go Download!", pos=(350, 60))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.stop_button = wx.Button(self, label="Stop", pos=(350, 100))
        self.Bind(wx.EVT_BUTTON, self.StopDownload, self.stop_button)

        # Options
        self.d_type = 'photo'
        self.option1 = wx.RadioButton(self, label=u'圖片(photo)', style=wx.RB_GROUP, pos=(150, 30))
        self.option2 = wx.RadioButton(self, label=u'影片(video)', pos=(250, 30))
        self.Bind(wx.EVT_RADIOBUTTON, self.SetDType, id=self.option1.GetId())
        self.Bind(wx.EVT_RADIOBUTTON, self.SetDType, id=self.option2.GetId())

        # Checkbox
        # self.new_first = wx.CheckBox(self, label="New video first", pos=(350, 30))
        # self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.new_first)

        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label="google+ id:", pos=(20, 60))
        # self.datetxt = wx.StaticText(self, -1, 'Start Date: {0} to Today'.format(datetime.date.today().strftime('%Y-%m-%d')),
                                           # pos=(220,200))
        self.picasa_id = wx.TextCtrl(self, value="115975634910643785199", pos=(150, 60), size=(160, -1))
        self.Bind(wx.EVT_TEXT_ENTER, self.EvtTextEnter, self.picasa_id)

        # Setting up the menu.
        aboutmenu = wx.Menu()

        menuAbout = aboutmenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        menuExit = aboutmenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(aboutmenu, "&About") # Adding the "aboutmenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Set variables
        # self.start_date = datetime.date.today()

        self.Show(True)

    def SetDType(self, event):
        if self.option1.GetValue():
            self.d_type = 'photo'
        elif self.option2.GetValue():
            self.d_type = 'video'

    def EvtCheckBox(self, event):
        pass

    def EvtTextEnter(self, event):
        self.OnClick(event)

    def OnClick(self, event):
        self.my_exe = GplusCrawler()
        worker = CountingThread(self.my_exe, self.picasa_id.Value, self.d_type) # self.new_first.GetValue()
        worker.start()

    def StopDownload(self, event):
        self.my_exe.stop_download = True

    def OnAbout(self, e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        about_txt = conf.MENU_ABOUT_TXT
        dlg = wx.MessageDialog(self, about_txt, conf.MENU_ABOUT_TITLE, wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self, e):
        self.Close(True)  # Close the frame.
        self.Destory()

app = wx.App(False)
frame = MainWindow(None, conf.UI_TITLE)
app.MainLoop()
