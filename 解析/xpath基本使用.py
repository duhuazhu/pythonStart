# _*_ coding : utf-8 _*_
# @Time :2023/5/4 14:42
# Author : 花猪
# @File : xpath基本使用
# @Project : python学习

from lxml import etree

# response.read().decode('utf-8')

tree = etree.parse('1.html')

print(type(tree))
# 查找ul下面的li


# //子孙  / 孙
# li_list = tree.xpath('//body/ul/li')
#  text()看内容

# 找到所有id属性的标签
# li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id位wh

# id后面加双引号
li_list = tree.xpath('//ul/li[@id="wh"]/text()')
print(li_list)


# 查找到id为li标签的class属性值
li =tree.xpath('//ul/li[@id="wh"]/@class')

print(li)

# 模糊查询 contains(@id,"b")
print(tree.xpath('//ul/li[contains(@id,"b")]/text()'))

#  以什么什么开头 starts-with(@id,"w")
print(tree.xpath('//ul/li[starts-with(@id,"w")]/text()'))

# 写在一个[] 内
print(tree.xpath('//ul/li[@id="wh" and @class="wuhan"]/text()'))

# | 或
print(tree.xpath('//ul/li[@id="wh11"]/text() | //ul/li[@id="wh"]/text()'))