#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Last modified: Sep. 26, 2018
#
import wx
import GetBookGui
from get import *


class GetBookDialog(GetBookGui.frame1):
    def __init__(self, parent):
        GetBookGui.frame1.__init__(self, parent)
        self.relogin = False

    def enable_relogin(self, event):
        self.relogin = (self.m_checkBoxRelogin.GetValue() == wx.CHK_CHECKED)
        self.m_textCtrlUsername.SetEditable(self.relogin)
        self.m_textCtrlPasswd.SetEditable(self.relogin)

    def extract_book_number(self, url):
        import re

        # http://www.jjwxc.net/onebook.php?novelid=XXXXXX
        pattern = re.compile(r'\d+')
        book_number = pattern.findall(url)[0]
        return book_number

    def begin_get_book(self, event):
        self.m_statusBar1.SetStatusText("开始取书")
        url = self.m_textCtrlNovelURL.GetValue()
        book_number = self.extract_book_number(url)
        output_folder = self.m_dirPicker1.GetPath()
        username = self.m_textCtrlUsername.GetValue()
        password = self.m_textCtrlPasswd.GetValue()
        get_book(book_number, output_folder, self.relogin, username, password)
        self.m_statusBar1.SetStatusText("完成")


app = wx.App(False)
dlg = GetBookDialog(None)
dlg.Show(True)
app.MainLoop()
