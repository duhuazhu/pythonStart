# _*_ coding : utf-8 _*_
# @Time :2023/4/23 19:08
# Author : 花猪
# @File : 列表
# @Project : python学习


a_list = [1, 3, 4, 56]
# a_list.remove(3)
# del a_list[0]
# print(a_list)


# for i in a_list:
#     if i == 3:
#         a_list.remove(i)

for i in range(len(a_list)-1):
    # print(a_list[i])
    if a_list[i] == 3:
    # if a_list[i] == 3:
        del a_list[i]

print(a_list)

a_list.pop()
print(a_list)