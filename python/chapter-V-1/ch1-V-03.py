# 不管嵌套的有多深使用global后改变的变量还是最外层全局变量及global代指的是全局变量
# 函数在执行时只编译不运行

name = '小黄'


def xiaoyang():
    name = '小杨'

    def xiaoliu():
        global name  # 改变的是小黄
        name = '小刘'

    xiaoliu()  # 3改变的是全局变量的值
    print(name)  # 4


print(name)  # 1
xiaoyang()  # 2
print(name)  # 5拿的是改变的值

# 小黄
# 小杨
# 小刘
