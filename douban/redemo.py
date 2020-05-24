import requests
import re


def parse_page(url):
    HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    response = requests.get(url, HEADERS)
    text = response.text
    #print(text)
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    caotais = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    contents = re.findall(r'<div\sclass="contson".*?>(.*?)</div>', text, re.DOTALL)
    peoms = []
    for content in contents:
        x = re.sub(r'<.*?>', '', content)
        peoms.append(x.strip())
    ALL_PEOMS = []
    for value in zip(titles, caotais, authors, contents):
        title, caotai, author, content = value
        peom = {
            'title': title,
            'caotai': caotai,
            'author': author,
            'content': content
        }
        ALL_PEOMS.append(peom)
    for peom in ALL_PEOMS:
        print(peom)





def main():
    for x in range(1, 3):
        url = 'https://www.gushiwen.org/default_%s.aspx'% x
        parse_page(url)




if __name__ == '__main__':
    main()

