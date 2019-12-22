# 给每个类添加一个数据属性和一个函数属性
def Decorator(obj):  # print(School.__dict__)
    # 添加数据属性
    obj.addr = "浙江省杭州市"

    def price():
        pass

    # 添加函数属性
    obj.price = price
    return obj


@Decorator  # 相当于执行 School = Decorator(School)
class School():
    def __init__(self, name, price):
        self.name = name
        self.price = price


# 打印类的属性字典
# r1=School("ee",2)
# print(r1.__dict__)
print(School.__dict__)
