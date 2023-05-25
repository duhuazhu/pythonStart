# _*_ coding : utf-8 _*_
# @Time :2023/5/17 16:29
# Author : 花猪
# @File : weatherDemo
# @Project : python学习
import json
import time
import requests
from lxml import etree

data = open("city.json", "r", encoding='utf-8')
dictionary = json.load(data)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
    'Cookie': '__bid_n=18827c4e6de57a0f7f4207; Hm_lvt_bd706f26d2267b54fd3543ceaea48e96=1684294396; FPTOKEN=+JLCaaT49KA6lt86nDTgWENnDgaVatKucz7BJnbX4+IHCt5JMeZQsVYmpLBnGJ5OV0x1zvlD8ShE3qjGJSCXbM6pH3nMZies32BjuziXQvNnLv0jbLlieVaX36m/noriKlmUMkWOmRxDV+L3AKuLGDXi5tv/5M5t4wRz/tGOUX79VqdMer0CnUlIXcCIVyvQcxWgvpd3LGPpt9GWWDOpJ9PkJCnnTAZ0opEgTJHxA2XSclY+nFq2gFRpfd4NjBDvyQvLZ1w8Zc5XRfpZ9rlHfHkvxGkm/N2QKgABPc6nXGd0EH3kgcLt+6w/JkI10Gc60/oOvlZklVrdavDzcuiLVJ/edCpjmKniLRxoGDwlkYWBGnGJ2xI7i8fldCmSEyDX7Oh5dUr8hq74tGHuv/BoIA==|EqvrBPtpK26/s6+88+Ly2MHfgK8kFKe7oiHg221sRpI=|10|ee560550b24d8f90489f999d96a89b0e; __gads=ID=adf2de1f8d466811-225c1214dfe0001b:T=1684294398:RT=1684294398:S=ALNI_MZsaR4PSAO4Mlk9FMXS5sAJtYMRIQ; __gpi=UID=00000bfa89dd3d28:T=1684294398:RT=1684294398:S=ALNI_MYxS5TYf8MkJJJ9L04qetq5hRJJGg; Hm_lvt_1d8a25469002bfac254500395ce9ec69=1684311109; Hm_lpvt_1d8a25469002bfac254500395ce9ec69=1684311109; c_y_g_j=richurimo; Hm_lpvt_bd706f26d2267b54fd3543ceaea48e96=1684311111',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}


def download(tq):
    json_str = json.dumps(tq, ensure_ascii=False)
    with open('SunriseAndSunsetWatch.json', 'a', encoding='utf-8') as fp:
        fp.write(json_str)
        fp.write(',')


def request_with_retry(url, max_retries=3, retry_interval=5):
    while True:
        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()  # 如果请求失败，会抛出异常
            print(response.status_code)
            return etree.HTML(response.text)  # 请求成功，返回响应头信息
        except Exception as e:
            print(f"Request failed: {e}")
            max_retries -= 1
            if max_retries == 0:
                print("Max retries reached, giving up.")
                return None  # 最大重试次数达到，返回 None
            print(f"Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)


def request_tq(data_time, obj, callback):
    for month in range(1, 13):
        resultMonth = ''
        if month < 10:
            resultMonth = '0' + str(month)
        else:
            resultMonth = str(month)
        result = data_time[0] + '__time__2023_' + resultMonth + '__' + data_time[1]
        url = 'https://richurimo.bmcx.com' + result
        html = request_with_retry(url)
        rDate = html.xpath('//table[@id="richurimo_table"]//tr[position() > 1]//td[1]/text()')
        sunrise = html.xpath('//table[@id="richurimo_table"]//tr[position() > 1]//td[2]/text()')
        sunset = html.xpath('//table[@id="richurimo_table"]//tr[position() > 1]//td[4]/text()')
        obj['children'].append({
            "date": rDate,
            "sunrise": sunrise,
            "sunset": sunset
        })
        if month == 12 and len(obj['children']) == 12:
            callback(obj)


for item in dictionary:
    href = item.get('href')
    text = item.get('text')
    data_time = href.split('__')
    obj = {'city': text, 'children': []}
    request_tq(data_time=data_time, obj=obj, callback=download)




