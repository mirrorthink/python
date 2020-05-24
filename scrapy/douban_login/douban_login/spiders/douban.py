# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from POL import Image


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login/']
    login_url = 'https://accounts.douban.com/login/'
    proflie_url = 'https://www.douban.com/people/172019085/'
    editsignature_url = 'https://www.douban.com/j/people/172019085/edit_signature'

    def parse(self, response):
        fromdata = {
            'source': 'None',
            'redir': 'https://www.douban.com/',
            'form_email': '15626467577',
            'form_password': '123456789q',
            'remember': 'on',
            'login': '登录',
        }
        captcha_img = response.css('img@captcha_image::attr(src)').get()
        if captcha_img:
            captcha = self.regonize_captcha(captcha_img)
            fromdata['captcha-solution'] = captcha
            captcha_id = response.xpath('//input[@name="captcha-id"]/@value').get()
            fromdata['captcha_id'] = captcha_id
        yield scrapy.FormRequest(url=self.login_url, fromdata=fromdata,callback=self.parse_after_login)

    def regonize_captcha(self, image_url):
        request.urlretrieve(image_url, 'captcha.png')
        image = Image.open('captcha.png')
        image.show()
        captcha = input('请输入验证码')
        return captcha

    def parse_after_login(self, respense):
        if respense.url == 'https://www.douban.com/':

            yield scrapy.Request(self.proflie_url,
                                 callback=self.parse_profile)
            print('success')
        else:
            print('fail')

    def parse_profile(self, response):
        if response.url == 'https://www.douban.com/people/172019085/':
            print('进入个人主页')
            ck = response.xpath('//input[@name="ck"]/@value').get()
            formdata = {
                'ck': ck,
                'signature': '五月天'
            }
            yield scrapy.FormRequest(self.editsignature_url, formdata=formdata)


        else:
            print('没有进入')









#
# ck:
# name: 15626467577
# password: 123456789
# remember: false
# ticket: H1CxPLe4Fuq5WNdaIOLYehFcn0sxxsBDS-6WSe8gScDfzGz6NhYHPOG5VUW6KTqqCPwrRmf7VAM*