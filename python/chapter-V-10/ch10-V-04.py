# 装饰器的架子
def foo(fun):
    def fee():
        print(fun)
        fun()

    return fee
