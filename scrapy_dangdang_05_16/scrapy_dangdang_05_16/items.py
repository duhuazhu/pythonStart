# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang0516Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 通俗的说 要下载的数据都有什么
    # 图片
    src = scrapy.Field()
    # // div[ @ id = "12810"] // ul // img / @ src
    # 名字
    name = scrapy.Field()
    # title = response.xpath('//div[@id="12810"]//ul/li/p/a/@title')

    # 价格
    price = scrapy.Field()
    # // div//ul/li/p[ @class ="price"] /span[@ class ="search_now_price"]
    pass
