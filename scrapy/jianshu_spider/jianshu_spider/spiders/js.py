# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import ArticleItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/p/f5c5ede490be']
    rules = (
        Rule(LinkExtractor(allow=r'.*p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/h1/text()').get()
        avatar = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/div[1]/div/a[@class="_1OhGeD"]/img/@src').get()
        author = response.xpath('///*[@id="__next"]/div[1]/div/div/section[1]/div[1]/div/div/div[1]/span[@class="FxYr8x"]/a/text()').get()
        pub_time = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/div[1]/div/div/div[2]/time/text()').get()
        url = response.url
        url1 = url.split('?')[0]
        article_id = url1.split('/')[-1]
        content = ''.join(response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/article//text()').getall())

        item = ArticleItem(title=title,
                           avatar=avatar,
                           author=author,
                           pub_time=pub_time,
                           origin_url=url,
                           article_id=article_id,
                           content=content
                           )
        yield item


