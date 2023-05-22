# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDangdang0516Pipeline:
    # 在爬虫文件之前执行
    def open_spider(self, spider):
        print('--------')
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))

        # print(item)
        # with open('book.json','a',encoding='utf-8') as fp:
        #     fp.write(str(item))

        return item

    # 爬虫文件执行之后执行的方法
    def close_spider(self, spider):
        self.fp.close()
        print('++++++')


# 多条管道同事开启
import urllib.request


# 开启
# "scrapy_dangdang_05_16.pipelines.DangDangDownloadPipeLine": 301,
class DangDangDownloadPipeLine:

    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        # print(url,'1233333')
        filename = './book/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
