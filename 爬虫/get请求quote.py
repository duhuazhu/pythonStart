# _*_ coding : utf-8 _*_
# @Time :2023/4/24 14:07
# Author : 花猪
# @File : get请求quote
# @Project : python学习


# 需求 获取 https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

import urllib.request

import ssl

import urllib.parse

url = 'https://www.baidu.com/s?wd='
headers={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
#汉字变成unicode 编码
name = urllib.parse.quote('周杰伦')

# 忽略 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# 打开一个 HTTPS URL
req = urllib.request.Request(url=url+name, headers=headers)

# 加上禁用ssl
response = urllib.request.urlopen(req, context=context)

# 读取页面内容
html = response.read().decode('utf-8')

# 输出内容
print(html)