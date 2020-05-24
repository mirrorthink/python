from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Qiangpiao(object):
    def __init__(self):
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.init_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        self.order_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        self.driver = webdriver.Chrome(
            # 输入你自己的hromedriver 地址
            executable_path='E:\data_Learn\chromedriver_win32\chromedriver.exe')

    def _login(self):
        self.driver.get(self.login_url)
        # 显示等待
        # 影视等待
        WebDriverWait(self.driver, 1000).until(
            EC.url_to_be(self.init_url)
        )
        print('登录成功')



    def _order_ticket(self):
        # 1.跳转到查票的页面
        # 是否正确输入目的地
        self.driver.get(self.search_url)
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'toStationText'), self.toStationText)
        )

        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'fromStationText'), self.fromStationText)
        )
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'train_date'), self.startTime)
        )
        print('三个信息成功输入')
        # 等待查询按钮是否可用
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.ID, 'query_ticket'))
        )
        searBtn = self.driver.find_element_by_id('query_ticket')
        searBtn.click()
        print('点击按钮')
        # 等待车次信息出来
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, './/tbody[@id="queryLeftTable"]/tr'))
        )
        tr_list = self.driver.find_elements_by_xpath('.//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')
        # 遍历车次信息
        for tr in tr_list:
            train_number = tr.find_element_by_class_name('number').text
            if (train_number in self.train):
                left_ticket = tr.find_element_by_xpath('.//td[4]').text
                if left_ticket == '有' or left_ticket.isdigit:
                    print(train_number + '有票')
                    orderBtn = tr.find_element_by_class_name('btn72')
                    orderBtn.click()
                    # 来到确认订单页面
                    WebDriverWait(self.driver, 1000).until(
                        EC.url_to_be(self.order_url)
                    )
                    WebDriverWait(self.driver, 1000).until(
                        EC.element_to_be_clickable((By.XPATH, '//ul[@id="normal_passenger_id"]/li/input'))
                    )
                    passager_list = self.driver.find_elements_by_xpath('//ul[@id="normal_passenger_id"]/li')
                    print(passager_list)
                    for li in passager_list:
                        input = li.find_element_by_tag_name('input')
                        name = li.find_element_by_tag_name('label').text
                        if name in self.passagers:
                            input.click()
                    submit = self.driver.find_element_by_id('submitOrder_id')
                    submit.click()
                    WebDriverWait(self.driver, 1000).until(
                        EC.element_to_be_clickable((By.ID, 'qr_submit_id'))
                    )
                    ensureBtn = self.driver.find_element_by_id('qr_submit_id')
                    ensureBtn.click()
                    # 有一个车次满足 就停止执行了
                    break


    def wait_input(self):
        self.fromStationText = input('出发地:')
        self.toStationText = input('目的地:')
        self.startTime = input('出发时间:')
        self.passagers = input('乘客姓名(如有多个，用英文逗号分开):').split(',')
        self.train = input('车次(如有多个，用英文逗号分开):').split(',')

    def run(self):
        self.wait_input()
        self._login()
        self._order_ticket()


if __name__ == '__main__':

    spider = Qiangpiao()
    spider.run()



