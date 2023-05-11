# _*_ coding : utf-8 _*_
# @Time :2023/5/5 08:57
# Author : 花猪
# @File : jsonpath解析
# @Project : python学习

# 本地资源
import json
import jsonpath

obj = json.load(open('book.json', 'r', encoding='utf-8'))

# 找到所有B开头的城市名称 $.XX[*]
# city = jsonpath.jsonpath(obj,'$.B[*].regionName')


# ..找到 所有regionName属性
# city = jsonpath.jsonpath(obj, '$..regionName')

# 找到所有A开头所有属性

# StartA = jsonpath.jsonpath(obj,'$.A.*')


# 找到最后一组数据
# lastCity = jsonpath.jsonpath(obj, '$..Z[(@.length-1)]')
# print(lastCity)


# 过滤所有包含属性

# hai  = jsonpath.jsonpath(obj, '$..Q[?(@.regionName)]')

# 过滤id小于400
# hai  = jsonpath.jsonpath(obj, '$..*[?(@.id<400)]')

suoypu = jsonpath.jsonpath(obj, '$..*')

print(suoypu)