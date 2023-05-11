# _*_ coding : utf-8 _*_
# @Time :2023/4/24 20:56
# Author : 花猪
# @File : obj
# @Project : python学习
headers='''
activityId: _ksTS: 1683268100551_108
jsoncallback: jsonp109
action: cityAction
n_s: new
event_submit_doGetAllRegion: true
'''
import  re

pattern = '^(.*?):[\s]*(.*?)$'
bstr = ""
for line in headers.splitlines():
    bstr += (re.sub(pattern,'\'\\1\': \'\\2\',',line)) + '\n'
print(bstr)
