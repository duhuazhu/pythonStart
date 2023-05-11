# _*_ coding : utf-8 _*_
# @Time :2023/4/25 09:28
# Author : 花猪
# @File : 异常
# @Project : python学习
import urllib.request
import ssl
import urllib.error
# url = 'https://csdnnews.blog.csdn.net/article1/details/130299380?spm=1000.2115.3001.5926'
url = 'https://www.dadsadas.com'


headers ={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    # 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    response = urllib.request.urlopen(url, context=context)

    print(response.read().decode('utf-8'))

except urllib.error.HTTPError:
    print('系统正在升级')

except urllib.error.URLError:
    print('地址错了')