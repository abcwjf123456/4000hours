name = 'hhhh'


def foo():
    name = 'ffff'

    def bar():
        name = 'ggg'
        print(name)

    return bar


"""拿到bar内存地址"""
res = foo()
res()

# ggg
