# -*- coding: utf-8 -*-
import scrapy
from b.items import BItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
class Baoma5Spider(CrawlSpider):
    name = 'baoma5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']
    #如果要解析页面就要callback
    #元组只有一个必须后面家逗号
    rules = (
        Rule(LinkExtractor(allow='https://car.autohome.com.cn/pic/series/65.+'),
             callback='parse_page', follow=True),
    )

    def parse(self, response):
        category = response.xpath('//div[@class="uibox-title"]/div/text()').get()
        srcs = response.xpath('//div[contains(@class,"uibox-con")]/ul/li//img/@src').getall()
        srcs =list(map(lambda x: x.replace('t_', ''), srcs))
        srcs = list(map(lambda x: response.urljoin(x), srcs))
        yield BItem(category=category, image_urls=srcs)

    def dir_parse(self, response):
        uiboxs = response.xpath('//div[@class="uibox"]')[1:]
        for uibox in uiboxs:
            category = uibox.xpath('.//div[@class="uibox-title"]/a/text()').get()
            urls = uibox.xpath('.//ul/li/a/img/@src').getall()
            urls = list(map(lambda url:response.urljoin(url), urls))
            item = BItem(category=category, image_urls=urls)
            yield item

