import requests
from lxml import etree

BASE_DOMIN = 'https://ygdy8.net'
URL = []
HEADERS = {
    'Referer': 'https://c.02kdid.com/b/1/1754/22432/960X90/960X90.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}


def get_detail_url(url):
    response = requests.get(url, headers=HEADERS)
    text = response.content
    html = etree.HTML(text)
    detail_url = html.xpath('//table[@class="tbspan"]//a/@href')
    detail_url = map(lambda url: BASE_DOMIN + url, detail_url)
    return detail_url


def parse_detail_page(url):
    response = requests.get(url, headers=HEADERS)
    text = response.content
    html = etree.HTML(text)
    movie = {}
    movie['title'] = html.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')
    zoom = html.xpath('//div[@id="Zoom"]')[0]
    imgs = html.xpath('//img/@src')
    movie['cover'] = imgs[0]
    infos = zoom.xpath('.//text()')
    def info_parse(text, rule):
        return text.replace(rule, '').strip()

    for index, info in enumerate(infos):
        if info.startswith('◎年　　代'):
            info = info_parse(info, '◎年　　代')
            movie['year'] = info
        elif info.startswith('◎产　　地'):
            info = info_parse(info, '◎产　　地')
            movie['plase'] = info
        elif info.startswith('◎类　　别'):
            info = info_parse(info, '◎类　　别')
            movie['catergory'] = info
        elif info.startswith('◎主　　演'):
            info = info_parse(info, '◎主　　演')
            actors = [info]
            for x in range(index+1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith('◎'):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith('◎简　　介'):
            info = info_parse(info, '◎简　　介')
            proflie = ''
            for x in range(index+1, len(infos)):
                proflie += infos[x].strip()
                if infos[x+1].startswith('【下载地址】'):
                    break
            movie['proflie'] = proflie
    downloadurl = html.xpath('//td[@bgcolor="#fdfddf"]/a/@href')[0]
    movie['downloadurl'] = downloadurl
    return movie


def spider():
    base_url = "https://ygdy8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1, 2):
        url = base_url.format(x)
        detail_urls = get_detail_url(url)
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)


if __name__ == '__main__':
    spider()
