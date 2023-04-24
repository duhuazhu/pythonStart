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
    'Cookie': 'BIDUPSID=E18BE886D96C2BC9F3B114B2076281C7; PSTM=1678761770; BAIDUID=E18BE886D96C2BC9245E90D67C55432B:FG=1; H_WISE_SIDS=219946_219563_216847_213363_214800_219942_213041_204911_230288_110085_227869_236308_243706_243878_244721_240590_244955_245412_246769_247632_248175_247585_249300_249910_250148_250738_243658_251127_252075_252562_249893_252580_247390_253170_234295_253066_253466_253480_253526_253704_249393_253516_253427_254323_254425_254472_254597_254261_254733_250606_248124_254747_251133_236540_253213_255290_253693_250390_255478_255450_254765_255645_252122_255940_255957_255891_251443_107313_250841_256096_256093_255679_248696_256128_253151_256083_255803_256152_253990_256010_256257_255660_256297_256315_256318_256024_256348_229154_255179_256392_245043_253900_256225_256440_256503; H_WISE_SIDS_BFESS=219946_219563_216847_213363_214800_219942_213041_204911_230288_110085_227869_236308_243706_243878_244721_240590_244955_245412_246769_247632_248175_247585_249300_249910_250148_250738_243658_251127_252075_252562_249893_252580_247390_253170_234295_253066_253466_253480_253526_253704_249393_253516_253427_254323_254425_254472_254597_254261_254733_250606_248124_254747_251133_236540_253213_255290_253693_250390_255478_255450_254765_255645_252122_255940_255957_255891_251443_107313_250841_256096_256093_255679_248696_256128_253151_256083_255803_256152_253990_256010_256257_255660_256297_256315_256318_256024_256348_229154_255179_256392_245043_253900_256225_256440_256503; newlogin=1; BAIDUID_BFESS=E18BE886D96C2BC9245E90D67C55432B:FG=1; ZFY=uTE3PX1pgpf7PQtRjarPAqX13aBsWhCKZRFDSTSU8Xk:C; RT="z=1&dm=baidu.com&si=a9124eb0-1e41-4af2-a9d2-cafcdd183b3d&ss=lgt657d3&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=26i&ul=164vh&hd=164xt"; __bid_n=187b10d6166e5d68854207; FPTOKEN=faiwZJgyLwAs4Mzny01xLE6VMsGSkG8VQGpiS9NCv1it7T7SRbqzH2LqWYVyp4dvWKe3ko+BdRDK5qGLCqcjnvP65g4yBtgVueTbLlTJwNEzzb5nD6JCT+URGu1KIAY6n3eL3wtE/tPGIJ6Eh36QbaoRun5PTsbzF4h2Cw+HtlExAxBG3sTSuOGFb3ssp+YjxeWYaCahdpgN2DOhUyqKd4vHuipWFPmmCioPBelq+eaXs15tA6at0w2Vmjyj2vGiS9J4EwtAQeSSdWLFILGIKN+jm1labsWo+O2uzGyTUjmZNjfh5tJTQ8GF9OzkqpQPUsozHY2BQWbKZ62Lo3p05ucy+FZNci73r0Mim9N1mqI3QDA0yItmZXBJYLaoGJw5Wg3LerjP7qMO2POIXE4XWQ==|TByNztUDJfEA5zoU9DPWP9VF48Z0jwDclxBylKnNfyM=|10|4964209f139478e0fe9b01855ec0d46d; BA_HECTOR=2k8g01810025018h80240hdd1i4c4e21n; H_PS_PSSID=38516_36547_38469_38468_36807_38486_37935_37709_38386_38356_26350_38545; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; delPer=0; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.baidu.com; ab_sr=1.0.1_YmEwNGY3NTliOWQ5YTM3OTA4MzZiNTRhZDhkMDA1ZTZlY2NkZjFiYWY5MGVjMGFiYTE5NGNhODE5MThiNjc5Njg5MGU1NDgyYWExODM1NzliMWM2NzgxNjZhZjkxMWM2MjNhNzdlZjk0Yzk1YjFkOTkyZTY5YTZmNzI0MzU3ZDQwYzY2ZTdiYTljMDgyMmEwM2JlNjQzMjY1NmQyMTc0Ng==; firstShowTip=1; BDRCVFR[0_FPWPLXdzb]=mk3SLVN4HKm',
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
#
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
