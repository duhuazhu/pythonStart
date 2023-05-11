# _*_ coding : utf-8 _*_
# @Time :2023/5/4 09:45
# Author : 花猪
# @File : 爬虫urllib_代理
# @Project : python学习
import ssl
import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)


proxies = {
    'http': 'http://aafrtp.fxr.9qjfo.hasyaf.cn:39304'
}

# 模拟游览器 访问服务器

# 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


# handler build_opener open
handler = urllib.request.ProxyHandler(proxies =proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)


#response =  urllib.request.urlopen(request, context =context)

context = response.read().decode('utf-8')

with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(context)

