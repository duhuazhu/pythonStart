# _*_ coding : utf-8 _*_
# @Time :2023/5/11 20:09
# Author : 花猪
# @File : get请求
# @Project : python学习
import requests

url = 'https://www.baidu.com/s'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.3'}

data= {
    'wd':'北京'
}

response = requests.get(url=url,params=data,headers=headers)

content = response.text

print(content)