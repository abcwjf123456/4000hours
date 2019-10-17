def foo(fun):
    def func():
        res=fun()
        print('执行装饰器')
        return res

    return func



@foo
def test():
    print('执行函数')
    return '123'


hh=test()
print(hh)


