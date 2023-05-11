# _*_ coding : utf-8 _*_
# @Time :2023/5/6 10:55
# Author : 花猪
# @File : selenium学习之路
# @Project : python学习

from selenium import webdriver

# 驱动用上
path = '../chromedriver_mac_arm64/chromedriver'

browser = webdriver.Chrome(path)

url = 'https://www.jd.com'

# 访问网址
browser.get(url)

# 获取网页源码
content = browser.page_source
print(content)
