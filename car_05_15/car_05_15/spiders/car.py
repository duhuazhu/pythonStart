import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    # html 结尾不能加 /
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        print('===================================1')
        nameList = response.xpath('//div[@class="main-title"]/a/text()')
        priceList = response.xpath('//span[@class="lever-price red"]/span/text()')
        # print(nameList)
        # for name in nameList:
        #     print(name.extract())
        for i in range(len(nameList)):
            # print(i)
            print(nameList[i].extract())
            print(priceList[i].extract())
        print('===================================2')
        pass
