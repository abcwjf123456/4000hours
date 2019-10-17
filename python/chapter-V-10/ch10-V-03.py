# 函数的嵌套
# 闭包包含在函数嵌套里面比如包包裹一层包一层
def foo(name):
    print(name)

    def gg():
        print(name)

        def hh():
            print(name)

        hh()

    gg()


foo('hh')
