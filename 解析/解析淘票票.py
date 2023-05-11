# _*_ coding : utf-8 _*_
# @Time :2023/5/5 14:22
# Author : 花猪
# @File : 解析淘票票
# @Project : python学习
import ssl
import urllib.request
import requests
import json
import jsonpath

url = "https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1683268100551_108&jsoncallback=jsonp109&action" \
      "=cityAction&n_s=new&event_submit_doGetAllRegion=true"

headers = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
    'Bx-V': '2.2.3',
    'Cookie': 't=6bb5a5a5d7c8b8cf544c554226ff5c3b; cookie2=1cbc53673bc437f5bf4cc45180a298a9; v=0; _tb_token_=3e377f44a8b33; xlly_s=1; l=fBNsaUKVNi_YgktMBOfaFurza779TIRvsuPzaNbMi9fP_l1p59oNW1wJz1T9CnGNFsEp83R4Lnf6BeYBcsDjjqj4axom4zDmnmOk-Wf..; tfstk=cUVRB7vJMZL82ESngbBDYgB1Gdbca6j-DUiH95jNmOphA1O91s47s5B7OTgIb0QA.; isg=BLOzZMRe0w5TqJ_aD2GsMfHFQrHd6EeqvuBbuGVQXlIJZNMG7rpL-lWyGpyKa5-i',
    'Referer': 'https://dianying.taobao.com/',
    'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0Sec-Ch-Ua-Platform:"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

request = urllib.request.Request(url, headers=headers)

# 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

params = {
    'activityId': '_ksTS: 1683268100551_108',
    'jsoncallback': 'jsonp109',
    'action': 'cityAction',
    'n_s': 'new',
    'event_submit_doGetAllRegion': 'true',
}

req = requests.get(url, headers=headers,params=params)


response = urllib.request.urlopen(request,context=context)
#
# print(req.text)

text = req.text

context = text.split('(')[1].split(')')[0]
# print(context)

with open('淘票票.json','w',encoding='utf-8') as fp:
    fp.write(context)

obj = json.load(open('淘票票.json','r',encoding='utf-8'))

print(jsonpath.jsonpath(obj, '$..regionName'))

# print(response.read().decode(''))