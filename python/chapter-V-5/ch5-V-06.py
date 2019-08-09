# abs() 函数返回数字的绝对值。
print(abs(-40))


# 40

# all()
# 列表list，存在一个为0的元素,列表list，存在一个为空的元素为false，空列表空元组为True
# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
#
# 元素除了是 0、空、None、False 外都算 True。
#
# 函数等价于：
#
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
# Python 2.5 以上版本可用。
#
# 语法
# 以下是 all() 方法的语法:
#
# all(iterable)
# ascii不能编码中文

