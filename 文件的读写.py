# _*_ coding : utf-8 _*_
# @Time :2023/4/24 09:02
# Author : 花猪
# @File : 文件的读写n

# fp= open('file/test1.txt','a')
# fp.write('hello world i am here\n' * 5)
# fp.close()

# 默认是一字节一字节的读取
fp = open('file/test1.txt','r')
# print(fp.read())
#读取一行 一行的读取
# print(fp.readline())
#返回列表
print(fp.readlines())


