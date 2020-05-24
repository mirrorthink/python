# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from b import settings
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
class BPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        category = item['category']
        urls = item['urls']
        category_path = os.path.join(self.path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            imagename = url.split('_')[-1]
            imgpath = os.path.join(category_path, imagename)
            request.urlretrieve(url, imgpath)
        return item


class BMWImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs = super(BMWImagePipeline, self).get_media_requests(item,info)
        #发送下载请求前调用
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        # 再被存储前调用
        path = super(BMWImagePipeline, self).file_path(request, response, info)
        catagory = request.item.get('category')
        images_path = settings.IMAGES_STORE
        catagory_path = os.path.join(images_path, catagory)
        if not os.path.exists(catagory_path):
            os.mkdir(catagory_path)
        image_name = path.replace('full/','')
        image_path = os.path.join(catagory_path, image_name)
        return image_path
