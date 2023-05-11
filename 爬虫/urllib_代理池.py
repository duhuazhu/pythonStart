# _*_ coding : utf-8 _*_
# @Time :2023/5/4 10:38
# Author : 花猪
# @File : urllib_代理池
# @Project : python学习

import random
import ssl

proxies_pool = [
    {
        'http:118.24.219.151:16817'
    },
    {
        'http:118.24.219.151:16811'
    },
]

#  随机数
proxies = random.choice(proxies_pool)

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

import urllib.request

request = urllib.request.Request(url, headers=headers)

# 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

result = response.read().decode('utf-8')

with open('daili2.html', 'w', encoding='utf-8') as fp:
    fp.write(result)
