# 局部变量与全局变量
# nonlocal指的是他上一级的值

name = '小黄'


def xiaoyang():
    name = '小杨'

    def xiaoliu():
        nonlocal name  # 改变的是小杨
        name = '小刘'

    xiaoliu()  # 3
    print(name)  # 4


print(name)  # 1
xiaoyang()  # 2
print(name)  # 5

# 小黄
# 小刘
# 小黄
