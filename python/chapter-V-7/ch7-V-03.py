# 生成器函数01


def test():
    yield 1
    yield 2
    yield 3


res = test()
print(res)
# <generator object test at 0x00B70EF0>
print(res.__next__())
print(res.__next__())
print(res.__next__())
