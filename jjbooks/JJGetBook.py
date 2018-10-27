#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Last modified: Oct. 27, 2018
#
import wx
import GetBookGui
from get import *
import os


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

    def open_output_dir(self, event):
        output_folder = self.m_dirPicker1.GetPath()
        if os.path.exists(output_folder):
            os.startfile(output_folder)

    def begin_get_book(self, event):
        self.m_statusBar1.SetStatusText("开始取书")
        url = self.m_textCtrlNovelURL.GetValue()
        book_number = self.extract_book_number(url)
        output_folder = self.m_dirPicker1.GetPath()
        username = self.m_textCtrlUsername.GetValue()
        password = self.m_textCtrlPasswd.GetValue()

        if self.relogin:
            self.m_statusBar1.SetStatusText("登陆")
            login_and_get_cookie(username, password)

        self.m_statusBar1.SetStatusText("获取文案")
        txt_filename = get_book_part(book_number, output_folder, "intro", "")
        self.m_statusBar1.SetStatusText("获取章节")
        get_book_part(book_number, output_folder, "content", txt_filename)
        self.m_statusBar1.SetStatusText("完成")


app = wx.App(False)
dlg = GetBookDialog(None)
dlg.Show(True)
app.MainLoop()
