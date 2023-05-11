# _*_ coding : utf-8 _*_
# @Time :2023/5/4 15:57
# Author : 花猪
# @File : 站长之家爬虫
# @Project : python学习

import urllib.request

import ssl

import requests as requests
from lxml import etree

url = 'https://sc.chinaz.com/tupian/dahaitupian.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url,headers=headers)

# 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

response = urllib.request.urlopen(request,context=context)
html = response.read().decode('utf-8')

tree= etree.HTML(html)

name =tree.xpath('//div[@class="container"]//img/@alt')

img_url  = tree.xpath('//div[@class="container"]//img/@data-original')


for i in range(len(img_url)):
    path = 'img/'+name[i] + ".jpg"
    req = requests.get('http:'+img_url[i])
    with open(path,'wb') as f:
        f.write(req.content)