# 给每个类添加一个可变的数据属性
def Decorator(**kwargs):
    def add(obj):
        "添加数据属性"
        # print('调用外部函数的**kwargs',kwargs)
        for key, val in kwargs.items():
            # 添加数据属性
            setattr(obj, key, val)
        return obj

    # print("外部传入的参数为:",kwargs)
    return add


@Decorator(addr="浙江省杭州市", name="浙江大学")  # 执行顺序:1.运行Decorator函数，先打印外部的传入的参数，返回add函数名；2.再执行School = add(School)
class School():
    def __init__(self, price):
        self.price = price


@Decorator(addr="湖北省", price=12000)
class School1():
    pass
