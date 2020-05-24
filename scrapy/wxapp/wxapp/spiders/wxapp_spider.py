# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['www.wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=%d'),
             # callback='parse_item',
             # 是否需要跟进
             follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'),
             callback='parse_detail',
             follow=False)
    )

    def parse_detail(self, response):
        title = response.xpath('//h1[@class="ph"]/text()').get()
        authors = response.xpath('//p[@class="authors"]')
        author = authors.xpath('.//a/text()').get()
        pub_time = authors.xpath('.//span/text()').get()
        content =  response.xpath('//td[@id="article_content"]//text()').getall()
        content = ''.join(content).strip()
        # print('author:%s/pub_time:%s' % (author, pub_time))
        # print(content)
        item = WxappItem(title=title,
                         author=author,
                         pub_time=pub_time,
                         content=content
                         )
        # 等同return
        yield item


