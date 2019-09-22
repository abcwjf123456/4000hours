# 生成器就是迭代器，生成器自动实现了迭代器协议(其他对象需要调用自己内置__iter__()方法)所以生成器就是迭代器
# 函数内部包含有yield关键字
# yield相当于return但yield能return多次yield会将函数挂起
# 生成器演示
def test():
    yield 1


gg = test()
print(gg)
print(gg.__next__())

# <generator object test at 0x03481EF0>
# 1
