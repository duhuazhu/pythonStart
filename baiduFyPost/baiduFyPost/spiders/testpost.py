import json

import scrapy


class TestpostSpider(scrapy.Spider):
    name = "testpost"
    allowed_domains = ["fanyi.baidu.com"]


    # post 请求 如果没有参数 将没任何意义
    # start_urls = ["https://fanyi.baidu.com/sug"]
    #
    # def parse(self, response):
    #     pass

    def parse(self):
        url = 'https://fanyi.baidu.com/sug"'
        data = {
            'kw': 'final'
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        if response.status == 200:
            # 登录成功，可以进行后续操作
            # 在这里解析页面内容或者发送其他请求
            content = response.text
            print(content,'1212121')
            # obj = json.loads(content)
            # print(obj,'1111222')
            pass
        else:
            # 登录失败，处理失败情况
            pass

