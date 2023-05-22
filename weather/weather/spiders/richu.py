import scrapy
import json


class RichuSpider(scrapy.Spider):
    name = "richu"
    allowed_domains = ["richurimo.bmcx.com"]
    data = open("city.json", "r", encoding='utf-8')
    dictionary = json.load(data)
    for item in dictionary:
        href = item.get('href')
        start_urls = ["https://richurimo.bmcx.com" + href]
        def parse(self, response):
            print(response.status,'123')
            pass
