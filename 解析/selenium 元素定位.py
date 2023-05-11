# _*_ coding : utf-8 _*_
# @Time :2023/5/6 11:43
# Author : 花猪
# @File : selenium 元素定位
# @Project : python学习

from selenium import webdriver
from selenium.webdriver.common.by import By

path = '../chromedriver_mac_arm64/chromedriver'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

# 根据标签属性的属性值
# button = browser.find_elements(By.ID, 'su')
# inputBD = browser.find_elements(By.ID, 'kw')
# inputWD = browser.find_elements(By.NAME, 'wd')

# print(inputWD)


# Xpath选择器
# buttonXpath = browser.find_elements(By.XPATH,'//input[@id="su"]')
# print(buttonXpath)

# bs4 语法
# button = browser.find_elements(By.CSS_SELECTOR, '#su')
# print(button)

button = browser.find_elements(By.LINK_TEXT,'新闻')
print(button)
browser.quit()