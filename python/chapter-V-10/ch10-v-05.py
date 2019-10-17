def foo(fun):
    def func():
        fun()
        print('执行装饰器')  # 可以在里面加入需要功能代码

    return func


# 被修饰函数
@foo  # @语法糖相当于test=foo(test)
def test():
    print('执行函数')


test()

# foo(test)()
