# _*_ coding : utf-8 _*_
# @Time :2023/4/24 20:56
# Author : 花猪
# @File : obj
# @Project : python学习
headers='''
pn: 12
rn: 12
tn: albumslist
word: 人物
album_tab: 人物
'''
import  re

pattern = '^(.*?):[\s]*(.*?)$'
bstr = ""
for line in headers.splitlines():
    bstr += (re.sub(pattern,'\'\\1\': \'\\2\',',line)) + '\n'
print(bstr)
