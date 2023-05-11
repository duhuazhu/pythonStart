# _*_ coding : utf-8 _*_
# @Time :2023/4/24 15:59
# Author : 花猪
# @File : ajax请求豆瓣电影
# @Project : python学习

import urllib.request
import urllib.parse
import ssl

import requests as requests

#
# # 创建一个默认的 SSL 上下文对象，并禁用 SSL 证书验证
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
#


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'image.baidu.com',
    'Referer': 'https://image.baidu.com/search/albumslist?tn=albumslist&word=%E4%BA%BA%E7%89%A9&album_tab=%E4%BA%BA%E7%89%A9&rn=15&fr=searchindex_album',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

import json

if __name__ == '__main__':
    start_page = int(input('起始的页码'))
    end_page = int(input('请输入结束的页面'))

    for page in range(start_page, end_page):
        data = {
            'pn': str(12 * page),  # 改变12*n
            'rn': '12',
            'tn': 'albumslist',
            'word': '美女',
            'album_tab': '人物',
        }
        data = urllib.parse.urlencode(data)
        print(data)
        url = 'https://image.baidu.com/search/albumsresult?'+data
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request, context=context)
        text = response.read().decode('utf-8')
        obj = json.loads(text)
        linkData = obj['albumdata']['linkData']
        for item in linkData:
            # urllib.request.urlretrieve(item['thumbnailUrl'], '/img'+str(item['setId'])+'.jpg')
            path = 'img/' + str(item['setId']) + ".jpg"
            _url = item['thumbnailUrl']
            req = requests.get(_url)
            with open(path, 'wb') as f:
                f.write(req.content)
# request = urllib.request.Request(url=url, data=data, headers=headers)
#
# response = urllib.request.urlopen(request, context=context)
# #
# content = response.read().decode('utf-8')
# #
# fp = open('百度图片urllist.json','w',encoding='utf-8')
# #
# # with open('百度图片.json','w',encoding='utf-8') as fp:
# #     fp.write(content)
# #
# fp.write(content)
# #
# fp.close()
