# _*_ coding : utf-8 _*_
# @Time :2023/4/23 16:30
# Author : 花猪
# @File : 添加
# @Project : python学习

#append
food_list = ['铁锅炖大鹅','酸菜五花肉']

food_list.append('123')

food_list.insert(0,'1233')

print(food_list)


num_list = [12,3,434,3]
num_list.extend(food_list)
#插入后面数组
print(num_list)
