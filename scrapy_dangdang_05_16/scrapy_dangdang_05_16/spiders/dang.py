import scrapy

from scrapy_dangdang_05_16.items import ScrapyDangdang0516Item


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    baseUrl = "http://category.dangdang.com/pg"
    page = 1
    start_urls = ["http://category.dangdang.com/pg1-cp01.49.01.00.00.00.html"]

    def parse(self, response):
        # pipeline 下载数据
        # item 定义数据结构
        li_list = response.xpath('//div[@id="search_nature_rg"]//li')
        for i in li_list:
            src = i.xpath('.//img/@data-original').extract_first()
            if src is None:
                src = i.xpath('.//img/@src').extract_first()
            name = i.xpath('.//img/@alt').extract_first()
            price = i.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            book = ScrapyDangdang0516Item(name=name, src=src, price=price)
            yield book
            # print(name, src, price)
        # 爬取多页的数据  爬取多页数据
        if self.page < 5:
            self.page = self.page + 1
            url = self.baseUrl + str(self.page) + '-cp01.49.01.00.00.00.html'
            # scrapy.Request就是scrpay的get请求
            yield scrapy.Request(url = url, callback=self.parse)
        pass
