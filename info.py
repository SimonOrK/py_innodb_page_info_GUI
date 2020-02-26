#! /usr/bin/env python 
#encoding=utf-8
import mylib
import wx
import controller

class mainController(controller.frame):
	def onOpenFile(self, event):
		mylib.get_innodb_page_type(self.text, self.show_detail.IsChecked(), self.lang.IsChecked())
	def onClear( self, event ):
		self.text.Clear()
def main():
	app = wx.App()
	frame = mainController(None)
	frame.Show()
	app.MainLoop()

if __name__ == '__main__':
	main()
