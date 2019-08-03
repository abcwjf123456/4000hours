# 局部变量与全局变量
# 嵌套

NAME = '小黄'


def xiaoyang():
    name = '小杨'
    print(name)

    def xiaogou():
        name = '小狗'
        print(name)

        def xiaomao():
            name = '小猫'
            print(name)

        xiaomao()

    xiaogou()


xiaoyang()
print(NAME)
