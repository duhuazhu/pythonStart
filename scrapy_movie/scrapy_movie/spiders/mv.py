import scrapy

from scrapy_movie.items import ScrapyMovieItem


class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["www.ygdy8.net"]
    start_urls = ["https://www.ygdy8.net/html/gndy/china/index.html"]

    def parse(self, response):
        # 第一页名字 第二页的图
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')
        for a in a_list:
            # name 和要点击的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            url = 'https://www.ygdy8.net/' + href
            # 对第二页的链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second, meta={
                'name': name,
            })
            # print(url)

    def parse_second(self, response):
        # 注意 拿不到数据的情况下 一定要检查xpath语法是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name']
        moive  = ScrapyMovieItem(src=src,name=name)
        yield moive
        pass
