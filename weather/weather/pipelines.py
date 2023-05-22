# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WeatherPipeline:
    # def open_spider(self, ls):
        # self.fp = open('city.json', 'w', encoding='utf-8')
        # self.fp.write('[')
    def process_item(self, item, spider):
        # with open('city.json','a',encoding='utf-8') as fp:
        #     fp.write(str(item))
        #     fp.write(',')
        # self.fp.write(str(item))
        # self.fp.write(',')
        return item

    # def close_spider(self, spider):
        # self.fp.write('[')
        # self.fp.close()

