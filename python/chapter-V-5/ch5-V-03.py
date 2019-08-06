# map函数
# map函数展开
num_1 = [1, 2, 3, 4, 5]


def map_test(func, array):
    res = []
    for i in array:
        ret = func(i)
        res.append(ret)
    return res


# [2, 3, 4, 5, 6]


print(map_test(lambda x: x + 1, num_1))
# map函数等价于上述代码
print(map(lambda x: x + 1, num_1))
# <map object at 0x039A0A50>
# map函数返回的是一个可迭代对象,是一个迭代器
print(list(map(lambda x: x + 1, num_1)))
# [2, 3, 4, 5, 6]


