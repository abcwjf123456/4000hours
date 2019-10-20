def z():
    print('增加')


def d():
    pass


def g():
    pass


def c():
    pass


if __name__ == '__main__':
    msg = '1:增加\n2:删除\n3:修改\n4:查找'
    gg = {
        '1': z,
        '2': d,
        '3': g,
        '4': c

    }
    print(msg)
    cho = input('请输入数字来实现功能')
    gg[cho]()
