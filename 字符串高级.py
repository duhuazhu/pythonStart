# _*_ coding : utf-8 _*_
# @Time :2023/4/23 15:49
# Author : 花猪
# @File : 字符串高级
# @Project : python学习


# - 获取长度 len
# - 查找内容 find
# - 判断 startswith , endswith
# - 计算出现次数 count
# - 替换内容 replace
# - 切割字符串 split
# - 修改大小写 upper lower
# - 空格处理 strip
# - 字符串拼接 join

s ='china'
print(len(s))

s1 = 'china'
print(s1.find('c'))

s2='china'

print(s2.startswith('c'))


print(s2.endswith('a'))

s3= 'aabb'
print(s3.count('a'))


s4 = 'ccdd'
print(s4.replace('c', 'd'))  #旧的 , 新的


s5 = '1#2#3#4'
print(s5.split('#'))

s6 = 'china'
print(s6.upper())


s7= 'CHINA'
print(s7.lower())

s8 = '  a  '
print(len(s8.strip()))

s9 = 'a'
print(s9.join('asdf'))