import time
import datetime

# 1. 时间戳
print(time.time())

# 2. 结构化时间
print(time.localtime())     # 默认参数 time.time()
print(time.gmtime())        # UTC时间

t=time.localtime()
print(t.tm_year)
print(t.tm_wday)

# 3. 字符串时间



# 结构化时间 --> 时间戳
print(time.mktime(time.localtime()))

# 结构化时间 --> 字符串时间
print(time.strftime("%Y-%m-%d %X", time.localtime()))

# 字符串时间 --> 结构化时间
print(time.strptime('2018-05-05 08:06:05', '%Y-%m-%d %X'))


print(time.asctime(time.localtime()))
print(time.ctime(time.time()))

time.sleep(1)

print(datetime.datetime.now())