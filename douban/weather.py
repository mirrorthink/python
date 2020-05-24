import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
ALL_DATA = []

def parse_page(url):
    HEADERS = {
        'Referer': 'https://c.02kdid.com/b/1/1754/22432/960X90/960X90.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            city = {}
            if index == 0 :
                city_td = tds[1]
            city["city"] = list(city_td.stripped_strings)[0]
            city["temp_low"] = int(list(tds[-2].stripped_strings)[0])
            ALL_DATA.append(city)
def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml'
       # 'http://www.weather.com.cn/textFC/hn.shtml',
       # 'http://www.weather.com.cn/textFC/hz.shtml',
       # 'http://www.weather.com.cn/textFC/hb.shtml',
       # 'http://www.weather.com.cn/textFC/xb.shtml',
       # 'http://www.weather.com.cn/textFC/gat.shtml',
           ]
    for url in urls:
        parse_page(url)
    ALL_DATA.sort(key=lambda data:data['temp_low'])

    cities = []
    for city_temp in ALL_DATA:
        city = city_temp['city']
        cities.append(city)
    cities = list(map(lambda x: x['city'], ALL_DATA))
    temp = list(map(lambda x: x['temp_low'], ALL_DATA))
    print(cities)
    print(temp)
    chart = Bar("天气")
    chart.add('城市', cities, temp)
    chart.render('test.html')

if __name__ == '__main__':
    main()