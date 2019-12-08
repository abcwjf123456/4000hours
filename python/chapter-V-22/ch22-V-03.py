# 类的增删改查
class People:
    cc = "ygyg"

    def __init__(self):
        pass

    def kk(self):
        print("国服台服")


print(People.cc)  # 查
People.cc = "gg"  # 改
p1 = People()
print(p1.cc)

# 增加
People.name = "南京"
print(p1.name)
print(People.name)

# 删除
del People.name


# print(p1.name)

# 函数的增加
def hh(self, food):
    print(food)


People.hh = hh
p1.hh("青菜")

print(People.__dict__)
