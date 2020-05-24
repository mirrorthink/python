from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
from lxml import etree
import re


#
#
# driver = webdriver.Chrome(executable_path=driver_path)
#
# driver.get('https://www.lagou.com/')

class LagouSpider(object):



    def __init__(self):
        self.driver_path = r'E:\data_Learn\chromedriver_win32\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.position = []
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

    def run(self):
        i = 0
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver, timeout=10).until(ec.presence_of_element_located([By.XPATH, '//div[@class="pager_container"]/span[last()]']) )
            #self.parse_list_page(source)
            if i == 0:
                pop_btn = self.driver.find_elements_by_xpath('//div[@class="body-box"]//div[@class="body-btn"]')
                print(pop_btn)
                if len(pop_btn) > 0:
                    pop_btn[0].click()
            i = i + 1
            next_btn = self.driver.find_elements_by_xpath('//div[@class="pager_container"]/span[last()]')[0]

            if 'pager_next_disabled' in next_btn.get_attribute("class"):
                break
            else:
                print(42)
                next_btn.click()
            time.sleep(2)
    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath('//a[@class="position_link"]/@href')
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self, url):
        # self.driver.get(url)
        self.driver.execute_script('window.open("%s")' % url)
        self.driver.switch_to_window(self.driver.window_handles[1])

        WebDriverWait(driver=self.driver, timeout=10).until(
            ec.presence_of_element_located([By.XPATH, '//span[@class="name"]']))

        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        pisition_name = html.xpath('//span[@class="name"]/text()')[0]
        job_request_spans = html.xpath('//dd[@class="job_request"]//span')
        salary = job_request_spans[0].xpath('.//text()')[0].strip()
        city = job_request_spans[1].xpath('.//text()')[0].strip()
        city = re.sub(r'[\s/]', '', city)
        work_years = job_request_spans[2].xpath('.//text()')[0].strip()
        work_years = re.sub(r'[\s/]', '', work_years)
        education = job_request_spans[3].xpath('.//text()')[0].strip()
        education = re.sub(r'[\s/]', '', education)
        desc = ''.join(html.xpath('//dd[@class="job_bt"]//text()')[0].strip())
        compony = html.xpath('//h2[@class="fl"]/text()')[0].strip()
        position = {
            'pisition_name': pisition_name,
            'compony':compony,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': education
        }
        print(position)
        self.position.append(position)



def main():
    spider = LagouSpider()
    spider.run()


if __name__ == '__main__':
    main()