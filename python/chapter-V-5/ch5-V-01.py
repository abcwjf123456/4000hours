# 高阶函数
# 1.返回值中包含函数
# 2.函数接收的参数是函数名

# 函数接收的参数是函数名

def foo(name):
    print(name)


def bar(n):
    print(n)


foo(bar("tft"))


# tft
# None

# 返回值中包含函数
def foo(name):
    print(name)


def bar(n):
    print(n)
    return foo('g')


bar("gy")

# gy
# g
