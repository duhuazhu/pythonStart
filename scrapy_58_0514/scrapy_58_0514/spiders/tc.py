import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["wh.58.com"]
    start_urls = ["https://wh.58.com"]

    def parse(self, response):
        print('================')
        # 字符串
        # print(response.text)
        # 二进制
        # print(response.body)
        ul_list =  response.xpath('//div[@id="headerWrap"]/div/ul/li')[0]
        # 提出seletor 对象data 的属性值
        # print(ul_list.extract())
        # 提出seletor列表的第一个数据
        print(ul_list.extract_first())
        # print(ul_list)

        print('================')
        pass
