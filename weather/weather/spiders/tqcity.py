import scrapy

from weather.items import WeatherItem


class TqcitySpider(scrapy.Spider):
    name = "tqcity"
    allowed_domains = ["richurimo.bmcx.com"]
    start_urls = ["https://richurimo.bmcx.com/"]

    def parse(self, response):
        a_list = response.xpath('//div[@id="main_content"]/ul/li/a')
        for i in a_list:
            href = i.xpath('.//@href').extract_first()
            text = i.xpath('.//text()').extract_first()
            item = WeatherItem(href=href, text=text)
            yield item
        pass
