# py_str = 'hello world'

# res = '{} is {} years old'.format('bob',23)
# print(res)
# res = '{1} is {0} years old'.format('bob',23)
# print(res)
res = '{:<10}{:^10}{:>8}'.format('id','name','age')
print(res)

# res = '%s is %s years old' % ('bob',23)
# print(res)
# res = '%s is %d years old' % ('bob',23.45)
# print(res)
# res = '%s is %.2f years old' % ('bob',23.45)
# print(res)

# #将字符串按空格分割 将分割的结果放入列表 返回列表
# res = py_str.split()
# print(res)
# res = 'day01.tar.gz'.split('.')
# print(res)
#
# #join 拼接字符串
# print('.'.join(res))
#
# py_str.islower()#是否为全部小写
# py_str.isupper()#是否为全部大写
# py_str.isdigit()#都是数字么？
# py_str.isalpha()#都是字母么？
# py_str.isalnum()#都是数字或字母么？

#以...开始吗？
# res = py_str.startswith('n')
# print(res)
#以...结尾吗？
# res = py_str.endswith('d')
# print(res)

#统计字符出现的次数
# res = py_str.count('nihao')
# print(res)


# res = py_str.capitalize()
# print(res)
#首字母大写
# res = py_str.title()
# print(res)

#让字符串在指定范围内居中
# res = py_str.center(50,'*')
# print(res)
# res = py_str.ljust(50,'*')
# print(res)
# res = py_str.rjust(50,'*')
# print(res)

