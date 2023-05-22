# _*_ coding : utf-8 _*_
# @Time :2023/5/11 19:24
# Author : 花猪
# @File : 无界面游览器-phantomjs基本使用
# @Project : python学习

# 无界面的
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# options = Options()
# path= '/Applications/Google/ Chrome.app/Contents/MacOS/Google/ Chrome'
# options.add_argument("headless")
# options.add_argument("--start-minimized")
# driver = webdriver.Chrome(options=options,executable_path=path)
# driver.get('https://baidu.com')
# driver.save_screenshot('百度.png')


# 封装一下

def share_browser():
    options = Options()
    path = '/Applications/Google/ Chrome.app/Contents/MacOS/Google/ Chrome'
    options.add_argument("headless")
    options.add_argument("--start-minimized")
    driver = webdriver.Chrome(options=options, executable_path=path)
    return driver

browser = share_browser()

url = 'https://www.baidu.com'
browser.get(url)
