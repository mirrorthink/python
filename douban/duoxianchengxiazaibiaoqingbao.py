import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading
import random
headers = {
    'Referer': 'http://www.doutula.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}
class Procuder(threading.Thread):
    print(13)
    def __init__(self, page_que, img_que, *args, **kwargs):
        super(Procuder, self).__init__(*args, **kwargs)
        self.page_que = page_que
        self.img_que = img_que

    def run(self):
        while True:
            if self.page_que.empty():
                print('page_que.empty')
                break
            url = self.page_que.get()
            self.parse_page(url)


    def parse_page(self, url):

        reponse = requests.get(url, headers=headers)
        print(reponse.status_code)
        text = reponse.text
        html = etree.HTML(text)
        imgs = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\?？\.\(\)（）。，！!]', '', alt)
            suffix = os.path.splitext(img_url)[1]
            filename = str(random.randint(0,9000000)) + suffix
            print(filename)
            self.img_que.put({img_url, filename})
            print(38)

class Comsumer(threading.Thread):
    print(14)
    def __init__(self, page_que, img_que, *args, **kwargs):
        super(Comsumer, self).__init__(*args, **kwargs)
        self.page_que = page_que
        self.img_que = img_que
    def run(self):
        while True:
            print('img_que', self.img_que.qsize())
            print('page_que', self.page_que.qsize())
            if self.img_que.empty() and self.page_que.empty():
                print(51)
                break
            img_url, filename = self.img_que.get()
            request.urlretrieve(img_url, 'images/' + filename)
            print(60)


def main():
    page_que = Queue(1)
    img_que = Queue(1000)
    for x in range(1, 2):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        page_que.put(url)
    print(page_que.qsize())



    for x in range(1):
        t = Procuder(page_que, img_que)
        t.start()
    for x in range(1):
        t = Comsumer(page_que, img_que)
        t.start()



if __name__ == '__main__':
    main()


