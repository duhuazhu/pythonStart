# _*_ coding : utf-8 _*_
# @Time :2023/4/24 09:52
# Author : 花猪
# @File : urllib
# @Project : python学习

import urllib.request

#基本使用
#使用urllib 获取百度首页的源码

# 1.定义一个url 就是访问的地址
url=  'http://www.baidu.com'

# 2. 模拟游览器向服务器发送请求
response =  urllib.request.urlopen(url)

# 获取页面源码 content 内容的意思
# 讲二进制数据转换为字符串
content = response.read().decode('utf-8')
print(content)