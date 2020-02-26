#encoding=utf-8
INNODB_PAGE_SIZE = 16*1024*1024

# Start of the data on the page
FIL_PAGE_DATA = 38


FIL_PAGE_OFFSET = 4 # page offset inside space
FIL_PAGE_TYPE = 24 # File page type

# Types of an undo log segment */
TRX_UNDO_INSERT = 1
TRX_UNDO_UPDATE = 2

# On a page of any file segment, data may be put starting from this offset
FSEG_PAGE_DATA = FIL_PAGE_DATA

# The offset of the undo log page header on pages of the undo log
TRX_UNDO_PAGE_HDR = FSEG_PAGE_DATA

PAGE_LEVEL = 26	#level of the node in an index tree; the leaf level is the level 0 */

EN_words = {
	'NUM' : 'Total number of page: %d:',
	'TREE' : "\npage offset: %s, page type: <%s>, page level: <%s>",
	'NORMAL' : '"\npage offset: %s, page type: <%s>"'
}

CN_words = {
	'NUM' : '页总数: %d:',
	'TREE' : "\n页偏移量: %s, 页类型: <%s>, 树中层次: <%s>",
	'NORMAL' : '"\n页偏移量: %s, 页类型: <%s>"'
}

EN_type={
	'0000':u'Freshly Allocated Page',
	'0002':u'Undo Log Page',
	'0003':u'File Segment inode',
	'0004':u'Insert Buffer Free List',
	'0005':u'Insert Buffer Bitmap',
	'0006':u'System Page',
	'0007':u'Transaction system Page',
	'0008':u'File Space Header',
	'0009':u'extend description page',
	'000a':u'Uncompressed BLOB Page',
	'000b':u'1st compressed BLOB Page',
	'000c':u'Subsequent compressed BLOB Page',
	'000d':u'Unknown',
	'000e':u'Compressed page',
	'000f':u'Encrypted page',
	'0010':u'Compressed and Encrypted page',
	'0011':u'Encrypted R-tree page',
	'0012':u'Uncompressed SDI BLOB page',
	'0013':u'Compressed SDI BLOB page',
	'0014':u'Unused',
	'0015':u'Rollback Segment Array page',
	'0016':u'Index pages of uncompressed LOB(Large Objects)',
	'0017':u'Data pages of uncompressed LOB(Large Objects)',
	'0018':u'The first page of an uncompressed LOB(Large Objects)',
	'0019':u'The first page of a compressed LOB(Large Objects)',
	'001a':u'Data pages of compressed LOB(Large Objects)',
	'001b':u'Index pages of compressed LOB(Large Objects)',
	'001c':u'Fragment pages of compressed LOB(Large Objects)',
	'001d':u'Index pages of fragment pages',
	'45bf':u'B-tree Node',
	'45be':u'R-tree Node',
	'45bd':u'Tablespace SDI Index page',
	}

CN_type={
	'0000':u'新分配的页',
	'0002':u'Undo 日志页',
	'0003':u'文件段inode页',
	'0004':u'插入缓冲空闲列表页',
	'0005':u'插入缓冲位图',
	'0006':u'系统页',
	'0007':u'事务系统页',
	'0008':u'文件空间头',
	'0009':u'扩展说明页',
	'000a':u'未压缩 BLOB 页',
	'000b':u'压缩的 BLOB 字段的第一个页',
	'000c':u'压缩的 BLOB 字段的页(非第一个)',
	'000d':u'未知',
	'000e':u'压缩页',
	'000f':u'加密页',
	'0010':u'加密+压缩的页',
	'0011':u'加密的R-tree Ndoe',
	'0012':u'解压的SDI blob 页',
	'0013':u'压缩的SDI blob 页',
	'0014':u'空闲页',
	'0015':u'回滚段-数组页',
	'0016':u'LOB(Large Objects)字段索引页',
	'0017':u'LOB(Large Objects)字段数据页',
	'0018':u'LOB(Large Objects)字段的第一个页',
	'0019':u'LOB(Large Objects)(压缩)字段的第一个页',
	'001a':u'LOB(Large Objects)(压缩)字段的数据页',
	'001b':u'LOB(Large Objects)(压缩)字段索引页',
	'001c':u'LOB(Large Objects)字段(压缩)的片段页',
	'001d':u'LOB(Large Objects)字段(压缩)的片段页的索引页',
	'45bf':u'B-tree 叶节点',
	'45be':u'R-tree 叶节点',
	'45bd':u'表空间的SDI索引页',
	}

innodb_page_direction={
	'0000': 'Unknown(0x0000)',
	'0001': 'Page Left',
	'0002': 'Page Right',
	'0003': 'Page Same Rec',
	'0004': 'Page Same Page',
	'0005': 'Page No Direction',
	'ffff': 'Unkown2(0xffff)'
}


INNODB_PAGE_SIZE=1024*16 # InnoDB Page 16K
