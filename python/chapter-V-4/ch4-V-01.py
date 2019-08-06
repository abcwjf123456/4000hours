# 匿名函数
# lambda x:x+1
# x为形参 x+1为返回值和下面函数等价
def cale(x):
    return x + 1


print(cale(10))

# 11

print(lambda x: x + 1)
# <function <lambda> at 0x037E2108>
# 因为打印的为内存地址所以可以进行以下操作
fun = lambda x: x + 1
print(fun(10))
# 11

fun1 = lambda x, y: (x + 1, y + 1)
print(fun1(1, 2))
