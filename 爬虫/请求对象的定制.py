# _*_ coding : utf-8 _*_
# @Time :2023/4/24 13:35
# Author : 花猪
# @File : 请求对象的定制
# @Project : python学习



import ssl
import urllib.request

import certifi
# from urllib.request import urlopen

url = 'https://www.baidu.com'

# url 的组成
# http / https
# 协议  主机  端口号
# http 80
# https 443
# mysql 3306
# oracle 1521
# MongoDB 27017


# 设置 User-Agent 头
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.3'}


# 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# 打开一个 URL，并在请求中添加 User-Agent 头
req = urllib.request.Request('https://www.baidu.com', headers=headers)
response = urllib.request.urlopen(req,context=context)

# 读取页面内容
html = response.read().decode('utf-8')

# 输出内容
print(html)