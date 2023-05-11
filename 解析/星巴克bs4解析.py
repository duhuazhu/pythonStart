# _*_ coding : utf-8 _*_
# @Time :2023/5/6 10:12
# Author : 花猪
# @File : 星巴克bs4解析
# @Project : python学习

import requests
from  bs4 import BeautifulSoup
from lxml import etree

url = 'https://www.starbucks.com.cn/menu/'


req  =requests.get(url)

# print(req.content.decode('utf-8'))
html = req.content.decode('utf-8')

with open('星巴克.html','w',encoding='utf-8') as fp:
    fp.write(html)




soup = BeautifulSoup(open('星巴克.html',encoding='utf-8'),'lxml')
arr = soup.select('ul[class="grid padded-3 product"] strong')
newArr = []
for item in arr:
    newArr.append(item.getText())

# tree = etree.parse('星巴克.html')
# content = tree.xpath('//ul[@class="grid padded-3 product"]//strong/text()')
# print(content)
print(newArr)

