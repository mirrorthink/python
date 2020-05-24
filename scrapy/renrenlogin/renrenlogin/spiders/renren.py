# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']
    # 从写start_requests

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do',
        data = {
            'email':
        }

        pass
