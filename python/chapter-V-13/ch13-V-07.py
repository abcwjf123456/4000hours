# 随机验证码
import random


def ff():
    ret = ""
    for i in range(0, 9):
        num = str(random.randint(0, 8))
        ret += num
    return ret


hh = ff()
print(hh)
