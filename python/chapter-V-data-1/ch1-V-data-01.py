# 如果a+b+c=1000且a^2+b^2=c^2 (a,b,c为自然数)如何求出所有a,b,c的组合
# 枚举法
# 优化见ch1-V-data-02
import time
"""测试需要多少时间"""
start_time = time.time()
"""利用for循环挨个尝试"""
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print("a;,b:,c:%d %d %d" % (a, b, c))
end_time = time.time()
"""打印出需要的时间"""
print("结束时间:%d" % (end_time - start_time))


# a;,b:,c:0 500 500
# a;,b:,c:200 375 425
# a;,b:,c:375 200 425
# a;,b:,c:500 0 500
# # 结束时间:216
