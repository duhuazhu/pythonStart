# _*_ coding : utf-8 _*_
# @Time :2023/4/24 08:51
# Author : 花猪
# @File : 文件的打开和关闭
# @Project : python学习

# f = open('file/test.txt','w')


# fp=open('file/test.txt', 'a')
# fp.write('11')

# r只读 默认的
# w 写入
# a追加


# 文件夹不可以暂时不能创建


# 文件的关闭
fp = open('file/a.txt','w')
fp.write('nihao')
fp.close()