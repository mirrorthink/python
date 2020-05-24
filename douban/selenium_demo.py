from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver_path = r'E:\data_Learn\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')
# driver.get('https://www.douban.com/')
driver.execute_script('window.open("https://www.douban.com/")')
# # print(driver.page_source)
# # # driver.close() 关闭 tab
# # # driver.quit() 关闭 整个页面
# # # 定位元素 find_element_by_id  find_elements_by_id
# # inputtag = driver.find_element_by_id('kw')
# # #inputtag = driver.find_element_by_xpath('//input[@id="kw"]')
# # #inputtag = driver.find_elements_by_css_selector('.dfsfsdf')
# # #inputtag = driver.find_elements(By.CSS_SELECTOR, '.dfsfsdf')
# # inputtag.send_keys('test')
# # # page_source =>etree 更快 如果只是获取数据 因为xml 底层用的是C语言
# # # 操作 selection
# # selectBtn = Select(driver.find_element_by_name('kw'))
# # selectBtn.select_by_index(1)
# 行为链
# inputtag = driver.find_element_by_id('kw')
# sumBtn = driver.find_element_by_id('su')
# actions = ActionChains(driver)
# actions.move_to_element(inputtag)
# actions.send_keys_to_element(inputtag, 'python')
# actions.move_to_element(sumBtn)
# actions.click(sumBtn)
# actions.perform()
# 操作cookies
# for cookies in driver.get_cookies():
#     print(cookies)
# value = driver.get_cookies(key)
#
# driver.delete_all_cookies()
#
# driver.delete_cookie(key)

# 页面等待 影视等待（等待XXX 显示等待（最多等待XXX
# driver.implicitly_wait(20)
# WebDriverWait(driver).until(
#     ec.presence_of_element_located([By.ID, 'test'])
# )

# 切换页面
# driver.switch_to_window(driver.window_handles[0])
# 代理IP
option = webdriver.ChromeOptions()
option.add_argument('--proxy-server=http://112312')
driver.path = ""
driver = webdriver.Chrome(executable_path=driver_path, Chrome_options=option)
