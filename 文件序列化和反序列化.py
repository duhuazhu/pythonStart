# _*_ coding : utf-8 _*_
# @Time :2023/4/24 09:09
# Author : 花猪
# @File : 文件序列化和反序列化
# @Project : python学习
# from json import dumps
import json

# fp = open('file/test1.txt','w')
# # 默认只能写入字符串
# fp.write('nihaoaaaa')
# fp.close()


# fp = open('file/test1.txt','w')
# name_list = ['zhangsan','list']
# names = json.dumps(name_list)
# fp.write(names)
# # 字符串
# print(type(names))
# fp.close()


# fp = open('file/test1.txt', 'w')
# name_list = ['zhangsan','list']
# # 转换字符串同时,指定一个文件的对象 然后把转换的字符串写入到这个文件
# json.dump(name_list,fp)
# fp.close()

#反序列化 json 字符串 变成python 对象
# fp = open('file/test1.txt','r')
# content = fp.read()
# # print(json.load(content,fp))
# print(type(json.loads(content)))
# fp.close()


fp= open('file/test1.txt','r')
result = json.load(fp)
print(type(result))
fp.close()