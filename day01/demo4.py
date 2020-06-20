import time
from datetime import datetime

#将当前程序暂时挂起指定时间(秒)
# time.sleep(5)
# print('hhh')

#返回时间元组
# t = time.localtime()
# print(t)

#1970 1 1 8:00～现在的时间秒数 时间戳
# print(time.time())

#获取字符串形式的当前时间
# res = time.strftime("%Y-%m-%d %H:%M:%S")
# print(res)

#通过一个字符串的时间求对应的时间对象
res = time.strptime('2020-06-01',"%Y-%m-%d")
print(res)

#时间对象转时间戳
liuyi = time.mktime(res)
print(liuyi)
now = time.time()
print(liuyi-now)