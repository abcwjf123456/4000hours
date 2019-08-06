# 优化
# 当知道a,b的值时c的值可通过1000-a-b得到无须遍历得出
import time

"""测试需要多少时间"""
start_time = time.time()
"""利用for循环挨个尝试"""
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print("a;,b:,c:%d %d %d" % (a, b, c))
end_time = time.time()
"""打印出需要的时间"""
print("结束时间:%d" % (end_time - start_time))


# a;,b:,c:0 500 500
# a;,b:,c:200 375 425
# a;,b:,c:375 200 425
# a;,b:,c:500 0 500
# 结束时间:1