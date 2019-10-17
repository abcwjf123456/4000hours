def foo(fun):
    def func(name,age):
        fun(name,age)
        print('执行装饰器')  # 可以在里面加入需要功能代码

    return func


# 被修饰函数
# 当被修饰函数有返回值时
@foo  # @语法糖相当于test=foo(test)
def test(name,age):
    print('执行函数')
    print(name)
    print(age)


test('gg',12)

# foo(test)()
