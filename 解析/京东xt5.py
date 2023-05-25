# _*_ coding : utf-8 _*_
# @Time :2023/5/23 15:03
# Author : 花猪
# @File : 京东xt5
# @Project : python学习

from selenium import webdriver

from selenium.webdriver.common.by import By

path = '../chromedriver_mac_arm64/chromedriver'

browser = webdriver.Chrome(path)

url = 'https://item.jd.com/100040213692.html?bbtf=1#crumb-wrap'

browser.get(url)

a_list = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='yushou yyp cat-1-652 cat-2-654 cat-3-5012 cat-4- item-100040213692 JD JD-1']/div[@class='w'][2]/div[@class='product-intro clearfix']/div[@class='itemInfo-wrap']/div[@class='summary p-choose-wrap']/div[@id='choose-attrs']//div[@class='dd']/div/a"

aList = browser.find_element(By.XPATH, a_list)

print(aList)