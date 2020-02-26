

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frame
###########################################################################

class frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"InnoDB工具", pos = wx.DefaultPosition, size = wx.Size( 973,549 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 4, 0, 0 )

		self.open_file = wx.Button( self, wx.ID_ANY, u"打开.ibd文件(数据库文件)", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.open_file, 0, wx.ALL, 5 )

		self.show_detail = wx.CheckBox( self, wx.ID_ANY, u"是否显示页信息", wx.Point( -100,1 ), wx.DefaultSize, 0 )
		gSizer1.Add( self.show_detail, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lang = wx.CheckBox( self, wx.ID_ANY, u"中文", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.lang, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button9, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )

		self.text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 960,470 ),  style = wx.TE_WORDWRAP|wx.TE_READONLY|wx.TE_RICH2 | wx.TE_MULTILINE|wx.TE_READONLY  )
		self.text.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.text.SetBackgroundColour('rgb(240,255,240)')

		bSizer1.Add( self.text, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.open_file.Bind( wx.EVT_BUTTON, self.onOpenFile )
		self.m_button9.Bind( wx.EVT_BUTTON, self.onClear )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onOpenFile( self, event ):
		event.Skip()

	def onClear( self, event ):
		event.Skip()
