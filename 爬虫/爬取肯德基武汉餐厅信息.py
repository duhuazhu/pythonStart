# _*_ coding : utf-8 _*_
# @Time :2023/4/25 08:46
# Author : 花猪
# @File : 爬取肯德基武汉餐厅信息
# @Project : python学习

import urllib.request
import requests
import ssl


base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

data = {
'op': 'cname'
}


headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
'Content-Length': '53',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': 'www.kfc.com.cn',
'Origin': 'http://www.kfc.com.cn',
'Proxy-Connection': 'keep-alive',
'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
}

# 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
import json

for i in range(1,11):
    params = {
        'cname': '武汉',
        'pid': '',
        'pageIndex': i,
        'pageSize': '10',
    }
    req =  requests.post(url = base_url , data = data , params = params)

    text = req.text

    with open('肯德基.json', 'a', encoding='utf-8') as fp:
        if i ==1:
            fp.write('[')
        fp.write(text)
        if i != 10:
            fp.write(',')
        fp.write('\n')
        if i == 10:
            fp.write(']')




