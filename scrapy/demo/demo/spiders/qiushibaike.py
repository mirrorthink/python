# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from demo.items import DemoItem

class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['yicommunity.com']
    start_urls = ['http://www.yicommunity.com/remen/']
    base_domin = 'http://www.yicommunity.com/'

    def parse(self, response):
        contents = response.xpath('//div[@class="content-block"]/div[@class="col1"]/div')
        for duanzidiv in contents:
            author = duanzidiv.xpath('.//div[@class="author"]//text()').get()
            content = duanzidiv.xpath('.//div[@class="content"]//text()').getall()
            content = ''.join(content)
            item = DemoItem(author=author,content=content )

            yield item
        next_url = response.xpath('//div[@class="pagebar"]/a[last()]/@href').get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domin+next_url, callback=self.parse)




