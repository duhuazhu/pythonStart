# _*_ coding : utf-8 _*_
# @Time :2023/4/23 19:33
# Author : 花猪
# @File : 字典
# @Project : python学习


a = {'name': '吴', 'age': 20}

print(a['age'])

# 要么get  要么 ['']
print(a.get('name'))
# 返回 None 不会报错
print(a.get('key'))

# 修改
# a['age'] =30
#
# print(a)

a['sex'] = '男'

print(a)

del a['sex']

print(a)

# 对象没有保留
del a

# 保留了对象
# a.clear()


# print(a)
