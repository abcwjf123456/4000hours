# 简写
# foo()()等价于前面的赋值操作
name = 'hhhh'


def foo():
    name = 'ffff'

    def bar():
        name = 'ggg'
        print(name)

    return bar


foo()()

# ggg
