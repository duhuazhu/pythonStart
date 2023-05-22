# _*_ coding : utf-8 _*_
# @Time :2023/5/11 20:01
# Author : 花猪
# @File : 基本使用
# @Project : python学习

import requests

url = 'https://www.baidu.com'

response = requests.get(url =url)

# 一个类型和六个属性
# print(type(response))

# 字符串 返回网页源码
response.encoding = 'utf-8'

# print(response.text)
# print(response.url)
# 二进制数据
# print(response.content)
# print(response.status_code)
# 响应头信息
print(response.headers)