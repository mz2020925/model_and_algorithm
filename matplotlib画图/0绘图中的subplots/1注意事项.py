# subplots_adjust
# 说明、参数
# Adjusting the spacing of margins and subplots调整边距和子图的间距
# subplots_adjust(self, left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
# 函数作用是调整子图布局，其主要参数含义和默认值为：
# left  = 0.125    # 图片中子图的左侧
# right = 0.9       # 图片中子图的右侧
# bottom = 0.1   # 图片中子图的底部
# top = 0.9         # 图片中子图的顶部
# wspace = 0.2   ＃为子图之间的空间保留的宽度，平均轴宽的一部分
# hspace = 0.2   ＃为子图之间的空间保留的高度，平均轴高度的一部分
# 加了这个语句，子图会稍变小，因为空间也占用坐标轴的一部分
# fig.subplots_adjust(wspace=0.5,hspace=0.5)