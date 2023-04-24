# _*_ coding : utf-8 _*_
# @Time :2023/4/24 14:45
# Author : 花猪
# @File : urllib get请求多个参数
# @Project : python学习

#urlencode 多个参数的时候

# https://www.baidu.com/s?wd=周杰伦&sex=男
import ssl

# 忽略 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
import urllib.parse
import urllib.request
data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

headers={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

params = urllib.parse.urlencode(data)

base_url = 'https://www.baidu.com/s?'

req = urllib.request.Request(base_url + params, headers=headers)


response = urllib.request.urlopen(req,context=context)

html = response.read().decode('utf-8')

print(html)

