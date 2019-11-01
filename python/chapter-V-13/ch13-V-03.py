import time

# 结构化时间
print(time.time())
print(time.localtime())
t = time.localtime()
print(t.tm_gmtoff)
print(t.tm_hour)
