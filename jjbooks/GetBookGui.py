# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"晋江取书", pos = wx.DefaultPosition, size = wx.Size( 576,261 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 237, 248, 248 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"小说目录地址：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		
		bSizer2.Add( self.m_staticText2, 1, wx.ALL, 5 )
		
		self.m_textCtrlNovelURL = wx.TextCtrl( self, wx.ID_ANY, u"http://www.jjwxc.net/onebook.php?novelid=XXXXXX", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrlNovelURL, 3, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"输出目录：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		
		bSizer5.Add( self.m_staticText5, 1, wx.ALL, 5 )
		
		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer5.Add( self.m_dirPicker1, 3, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		self.m_checkBoxRelogin = wx.CheckBox( self, wx.ID_ANY, u"重新登陆（如果拿不到VIP章节请勾选）", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBoxRelogin, 0, wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"用户名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		
		bSizer3.Add( self.m_staticText3, 1, wx.ALL, 5 )
		
		self.m_textCtrlUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer3.Add( self.m_textCtrlUsername, 2, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		
		bSizer3.Add( self.m_staticText4, 1, wx.ALL, 5 )
		
		self.m_textCtrlPasswd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_READONLY )
		bSizer3.Add( self.m_textCtrlPasswd, 2, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_buttonGetBook = wx.Button( self, wx.ID_ANY, u"取书", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonGetBook.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_buttonGetBook.SetBackgroundColour( wx.Colour( 204, 230, 230 ) )
		
		bSizer1.Add( self.m_buttonGetBook, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_dirPicker1.Bind( wx.EVT_DIRPICKER_CHANGED, self.update_output_dir )
		self.m_checkBoxRelogin.Bind( wx.EVT_CHECKBOX, self.enable_relogin )
		self.m_buttonGetBook.Bind( wx.EVT_BUTTON, self.begin_get_book )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def update_output_dir( self, event ):
		event.Skip()
	
	def enable_relogin( self, event ):
		event.Skip()
	
	def begin_get_book( self, event ):
		event.Skip()
