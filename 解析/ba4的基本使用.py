# _*_ coding : utf-8 _*_
# @Time :2023/5/5 16:21
# Author : 花猪
# @File : ba4的基本使用
# @Project : python学习

from bs4 import BeautifulSoup

# 通过解析本地文件 来将bs4的基础语法进行讲解

soup = BeautifulSoup(open('test.html',encoding='utf-8'),'lxml')

# soup.a 第一个a标签
# print(soup.a.attrs)

# attrs 获取标签的属性 和属性值

# bs4的一些函数 find find_all select
# 返回的第一个符合条件的数据
# soup.find('a')
# 根据title的值找到对应的标签
# print(soup.find('a', title="a3"))

# class 不能用
# soup.find('a', class='h1')

# 返回列表 返回所有a标签  如果想获取多个标签数据 需要在findall参数中 添加列表的数据
# print(soup.findAll(['a','li']))

# print(soup)

# 如果只想要前2个呢   limit找到前几个数据
# print(soup.findAll('li',limit=2))

# select (推荐)
# 获取div 所有的后代
# print(soup.select('ul li'))

# 某标签的第一级子标签
# print(soup.select('ul > a'))


# 找到a标签和li标签的所有的对象
# print(soup.select('a,li'))

# 节点信息
# 节点内容
obj = soup.select('#d1')[0]
# 如果标签对象中只有内容 string 和 get_text()都可以使用
# 如果标签对象中 除了内容 还有标签 getText是可以获取数据的
# 推荐getText()
# print(obj.getText())
# print(obj.string)

# 节点属性
# print(soup.select('#p1'))
# name 标签的名字
# print(soup.select('#p1')[0].name)
# 将属性值作为一个字典返回
# print(soup.select('#p1')[0].attrs)

# 获取节点的属性 三种方式
obj1 = soup.select('#p1')[0]
# print(obj1.attrs.get('class'))
# print(obj1.get('class'))
print(obj1['class'])
