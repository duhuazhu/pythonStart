# _*_ coding : utf-8 _*_
# @Time :2023/5/11 18:45
# Author : 花猪
# @File : selenium交互
# @Project : python学习

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

path = '../chromedriver_mac_arm64/chromedriver'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

import time

time.sleep(2)

inputKW = browser.find_element(By.ID, "kw")

inputKW.send_keys('周杰伦')

time.sleep(2)

buttonBd = browser.find_element(By.ID, "su")

buttonBd.click()

time.sleep(2)

js_bottom = 'document.documentElement.scrollTop=100000'

browser.execute_script(js_bottom)

time.sleep(2)

nextClick = browser.find_element(By.CLASS_NAME, "n")

nextClick.click()

time.sleep(2)


browser.back()

time.sleep(2)

browser.forward()


time.sleep(5)

browser.quit()
