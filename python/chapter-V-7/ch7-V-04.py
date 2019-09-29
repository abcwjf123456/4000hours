# 生成器函数02
# 效率高不占内存,一次返回一个结果,状态挂起

def test():
    for i in range(10):
        yield i


res = test()
print(res.__next__())
