import time
# 有截图表示
# 将结构体转换成时间戳
print(time.mktime(time.localtime()))

# 将结构化时间转换成字符串时间
print(time.strftime("%Y-%m-%d %X", time.localtime()))
# 2019-10-24 20:14:15

# 将字符串转换成结构化时间
print(time.strptime("2019:10:24:20:14:15", "%Y:%m:%d:%X"))
# time.struct_time(tm_year=2019, tm_mon=10, tm_mday=24, tm_hour=20, tm_min=14, tm_sec=15, tm_wday=3, tm_yday=297, tm_isdst=-1)

print(time.ctime())
print(time.asctime())
# Thu Oct 24 20:28:39 2019
# Thu Oct 24 20:28:39 2019