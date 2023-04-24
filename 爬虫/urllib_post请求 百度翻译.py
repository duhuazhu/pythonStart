# _*_ coding : utf-8 _*_
# @Time :2023/4/24 15:15
# Author : 花猪
# @File : urllib_post请求 百度翻译
# @Project : python学习

import urllib.request
import urllib.parse
import ssl

url = 'https://fanyi.baidu.com/sug'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.3'}

data = {
    'kw':'spider'
}
# 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# post 请求 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url = url,data = data ,headers=headers)

response  = urllib.request.urlopen(request,context=context)

context  =  response.read().decode('utf-8')

import json

obj = json.loads(context)
print(obj)