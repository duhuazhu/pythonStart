# _*_ coding : utf-8 _*_
# @Time :2023/4/25 13:27
# Author : 花猪
# @File : handler 处理器
# @Project : python学习
import ssl
# 需求 适应handler访问百度 获取源码

import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# handler   build_opener   open


# 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# 获取handler对象
handler = urllib.request.HTTPHandler()

# 获取opener对象
opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

print(content)