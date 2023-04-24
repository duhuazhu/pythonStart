# _*_ coding : utf-8 _*_
# @Time :2023/4/23 19:55
# Author : 花猪
# @File : 函数
# @Project : python学习


# def f1(name):
#     print('欢迎'+str(name))
#
# f1(212)

# 写1加到100
def add(a, b):
    num = a + b
    if b >= 100:
        print(num)
        return
    add(num ,b + 1)


add(1, 2)
