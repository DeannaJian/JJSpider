# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr 17 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frame1
###########################################################################

class frame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"晋江取书", pos = wx.DefaultPosition, size = wx.Size( 576,261 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 57, 57, 57 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"小说目录地址：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft JhengHei UI" ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer51.Add( self.m_staticText2, 1, wx.ALL, 5 )


		bSizer2.Add( bSizer51, 1, wx.EXPAND, 1 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrlNovelURL = wx.TextCtrl( self, wx.ID_ANY, u"http://www.jjwxc.net/onebook.php?novelid=XXXXXX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlNovelURL.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft JhengHei UI" ) )

		bSizer6.Add( self.m_textCtrlNovelURL, 3, wx.ALL, 5 )


		bSizer2.Add( bSizer6, 5, wx.EXPAND, 1 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 1 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"输出目录：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )
		self.m_staticText5.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer7.Add( self.m_staticText5, 1, wx.ALL, 5 )


		bSizer5.Add( bSizer7, 1, wx.EXPAND, 1 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft JhengHei UI" ) )
		self.m_dirPicker1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer8.Add( self.m_dirPicker1, 3, wx.ALL, 5 )

		self.m_buttonOpenDir = wx.Button( self, wx.ID_ANY, u"打开", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonOpenDir.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft JhengHei UI" ) )
		self.m_buttonOpenDir.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_buttonOpenDir.SetBackgroundColour( wx.Colour( 69, 69, 69 ) )

		bSizer8.Add( self.m_buttonOpenDir, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer8, 5, wx.EXPAND, 1 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 1 )

		self.m_checkBoxRelogin = wx.CheckBox( self, wx.ID_ANY, u"重新登陆（如果拿不到VIP章节请勾选）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxRelogin.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )
		self.m_checkBoxRelogin.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1.Add( self.m_checkBoxRelogin, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"用户名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft JhengHei UI" ) )
		self.m_staticText3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3.Add( self.m_staticText3, 1, wx.ALL, 5 )

		self.m_textCtrlUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrlUsername.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft JhengHei UI" ) )

		bSizer3.Add( self.m_textCtrlUsername, 2, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft JhengHei UI" ) )
		self.m_staticText4.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3.Add( self.m_staticText4, 1, wx.ALL, 5 )

		self.m_textCtrlPasswd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_READONLY )
		self.m_textCtrlPasswd.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )

		bSizer3.Add( self.m_textCtrlPasswd, 2, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 1 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_buttonGetBook = wx.Button( self, wx.ID_ANY, u"取书", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonGetBook.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ) )
		self.m_buttonGetBook.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_buttonGetBook.SetBackgroundColour( wx.Colour( 69, 69, 69 ) )

		bSizer1.Add( self.m_buttonGetBook, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_statusBar1.SetBackgroundColour( wx.Colour( 99, 99, 99 ) )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_dirPicker1.Bind( wx.EVT_DIRPICKER_CHANGED, self.update_output_dir )
		self.m_buttonOpenDir.Bind( wx.EVT_BUTTON, self.open_output_dir )
		self.m_checkBoxRelogin.Bind( wx.EVT_CHECKBOX, self.enable_relogin )
		self.m_buttonGetBook.Bind( wx.EVT_BUTTON, self.begin_get_book )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def update_output_dir( self, event ):
		event.Skip()

	def open_output_dir( self, event ):
		event.Skip()

	def enable_relogin( self, event ):
		event.Skip()

	def begin_get_book( self, event ):
		event.Skip()


