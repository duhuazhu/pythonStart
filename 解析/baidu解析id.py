# _*_ coding : utf-8 _*_
# @Time :2023/5/4 15:31
# Author : 花猪
# @File : baidu解析id
# @Project : python学习
import ssl

from lxml import etree

import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

# 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


request =urllib.request.Request(url,headers=headers)

response  = urllib.request.urlopen(request,context=context)

reHtml = response.read().decode('utf-8')

tree = etree.HTML(reHtml)


# xpath 返回值是一个列表数据
print(tree.xpath('//input[@id="su"]/@value'))