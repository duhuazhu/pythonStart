# _*_ coding : utf-8 _*_
# @Time :2023/4/24 09:29
# Author : 花猪
# @File : 异常
# @Project : python学习


try:
    fp = open('text.txt', 'r')
    fp.read()
except FileNotFoundError:
    print('没有文件读不到')
