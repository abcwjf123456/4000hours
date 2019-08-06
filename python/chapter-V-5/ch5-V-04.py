# reduce
# 返回计算结果
# 使用reduce需要导入包
from functools import reduce

num_1 = [1, 4, 3, 2]


# csz为初始值
def reduce_test(func, array, csz=None):
    if csz is None:
        ret = array.pop(0)
    else:
        ret = csz
    for i in num_1:
        ret = func(ret, i)
    return ret


print(reduce_test(lambda x, y: x * y, num_1))
# 24
print(reduce(lambda x, y: x * y, num_1))
