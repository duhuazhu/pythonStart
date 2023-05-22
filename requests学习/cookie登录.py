# _*_ coding : utf-8 _*_
# @Time :2023/5/12 10:20
# Author : 花猪
# @File : cookie登录
# @Project : python学习
import requests
from bs4 import BeautifulSoup

# __VIEWSTATE: b2YZdK6pcCSWK1SAgAh78Nfre7zU6d3WHg+KnYYjIs5k4LtWUv8k3F14cqw/Q0A/a9VMnByr5lXx9lmMcPLzrsf0VbdoBdO+ayxd/bJ0OlHTdIIDPc8sMY9c6eY3WBxJTxylSd01A2i73VtzhaTYA1miGfU=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 335921101@qq.com
# pwd: 1212121212121
# code: nyz1
# denglu: 登录

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Cookie': 'login=flase; Hm_lvt_9007fab6814e892d3020a64454da5a55=1683858262; ASP.NET_SessionId=fr4ofike12vi1hw02xuaas5c; login=flase; gswZhanghao=335921101%40qq.com; wsEmail=335921101%40qq.com; ticketStr=204637433%7cgQHv8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyR2kzN1JtbGVkN2kxei1NNXhBMTIAAgT_o11kAwQAjScA; codeyzgswso=3b82a4949f8c4635; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1683859269',
    'Referer': 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx',
    'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}
urlparse = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
response = requests.get(url=urlparse, headers=headers)
content = response.text

# 解析源码
soup = BeautifulSoup(content, 'lxml')
__VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs.get('value')
__VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码图片

code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'http://so.gushiwen.cn' + code

session = requests.session()

responseImg = session.get(url=code_url)

contentImg = responseImg.content
# wb 二进制写入文件
with open('code.jpg', 'wb') as fp:
    fp.write(contentImg)

code_name = input('请输入你的验证码')



url_post = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"

data_post = {
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '335921101@qq.com',
    'pwd': 'du963125',
    'code': code_name,
    'denglu': '登录',
}

response_post = session.post(url=url_post, headers=headers, data=data_post)

content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8') as f:
    f.write(content_post)
