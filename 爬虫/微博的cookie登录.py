# _*_ coding : utf-8 _*_
# @Time :2023/4/25 11:06
# Author : 花猪
# @File : 微博的cookie登录
# @Project : python学习
import ssl
# 绕过登录 进入到某个页面

import urllib.request

url = 'https://weibo.com/u/3166075683'

headers = {
    'authority': 'weibo.com',
    'method': 'GET',
    'path': '/3166075683',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh,zh-CN;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'referer': 'https://d.weibo.com/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

# 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request, context=context)

content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)