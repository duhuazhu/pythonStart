# _*_ coding : utf-8 _*_
# @Time :2023/5/17 16:00
# Author : 花猪
# @File : 替换
# @Project : python学习

with open('city.json', 'r') as f:
    data = f.read()
    data = data.replace("'", '"')
with open('city.json', 'w') as f:
    f.write(data)