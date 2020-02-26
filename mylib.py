#encoding=utf-8
import os
import include
import wx
from include import *
import win32ui

TABLESPACE_NAME='D:\\mysql_data\\test\\t.ibd'
VARIABLE_FIELD_COUNT = 1
NULL_FIELD_COUNT = 0


class myargv(object):
	def __init__(self, argv):
		self.argv = argv
		self.parms = {}
		self.tablespace = ''

	def parse_cmdline(self):
		argv = self.argv
		if len(argv) == 1:
			print('Usage: python py_innodb_page_info.py [OPTIONS] tablespace_file')
			print('For more options, use python py_innodb_page_info.py -h')
			return 0
		while argv:
			if argv[0][0] == '-':
				if argv[0][1] == 'h':
					self.parms[argv[0]] = ''
					argv = argv[1:]
					break
				if argv[0][1] == 'v':
					self.parms[argv[0]] = ''
					argv = argv[1:]
				else:
					self.parms[argv[0]] = argv[1]
					argv = argv[2:]
			else:
				self.tablespace = argv[0]
				argv = argv[1:]
		if self.parms.get('-h'):
			print('Get InnoDB Page Info')
			print('Usage: python py_innodb_page_info.py [OPTIONS] tablespace_file\n')
			print('The following options may be given as the first argument:')
			print('-h        help ')
			print('-o output put the result to file')
			print('-t number thread to anayle the tablespace file')
			print('-v        verbose mode')
			return 0
		return 1

def mach_read_from_n(page,start_offset,length):
	ret = page[start_offset:start_offset+length]
	return ret.hex()

def more(offset,len):
	pass

def get_innodb_page_type(text, detail,cn):
    dia = win32ui.CreateFileDialog(1)
    dia.SetOFNInitialDir('C:/')
    dia.DoModal()

    filename = dia.GetPathName()
    if (filename):
        text.Clear()
        f = open(filename, 'rb')
        fsize = os.path.getsize(f.name) // INNODB_PAGE_SIZE
        ret = {}
        back = ''
        lang = include.CN_words if cn else include.EN_words
        innodb_page_type = include.CN_type if cn else include.EN_type
        text.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        text.AppendText(lang['NUM'] % fsize)
        for i in range(fsize):
            page = f.read(INNODB_PAGE_SIZE)
            page_offset = mach_read_from_n(page, FIL_PAGE_OFFSET, 4)
            page_type = mach_read_from_n(page, FIL_PAGE_TYPE, 2)

            if detail:
                if page_type == '45bf':
                    page_level = mach_read_from_n(page, FIL_PAGE_DATA + PAGE_LEVEL, 2)
                    back += lang['TREE'] % (page_offset, innodb_page_type[page_type], page_level)
                else:
                    back += lang['NORMAL'] % (page_offset, innodb_page_type[page_type])

            if not ret.get(page_type):
                ret[page_type] = 1
            else:
                ret[page_type] = ret[page_type] + 1


        for type in ret:
            text.AppendText("\n%s: %s" % (innodb_page_type[type], ret[type]))
        text.SetDefaultStyle(wx.TextAttr('rgb(77,77,77)'))
        text.AppendText(back)