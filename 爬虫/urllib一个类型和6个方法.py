# _*_ coding : utf-8 _*_
# @Time :2023/4/24 10:44
# Author : 花猪
# @File : urllib一个类型和6个方法
# @Project : python学习
import urllib.request

url = 'http://www.baidu.com'

#发送请求
resource = urllib.request.urlopen(url)

# <class 'http.client.HTTPResponse'>
# print(type(resource))

#一字节去读
# read
# readline
# content = resource.readlines()
# content = resource.read(5)
# print(content)

#200
print(resource.getcode())

# url
print(resource.geturl())

print(resource.getheaders())


# 一个类型HTTPResponse
# 六个方法
# read
# readline
# readlines
# getcode()
# geturl()
# getheaders()

