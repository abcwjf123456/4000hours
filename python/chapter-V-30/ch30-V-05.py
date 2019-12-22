
class Myproperty():
    def __init__(self, fun):
        # print("执行Myproperty类的构造方法")   #调用Myproperty类时会首先运行它
        self.fun = fun

    def __get__(self, instance, owner):
        """
        :param instance: 代表school实例本身
        :param owner:  代表类School本身
        :return:
        """
        # print('调用Myproperty的属性时将执行此方法')
        return self.fun(instance)


class School():
    """
    @name:学校名字
    @addr:学校地址
    @price:学费
    @num:招生人数
    """

    def __init__(self, name, addr, price, num):
        self.name = name
        self.addr = addr
        self.price = price
        self.num = num

    # @property
    @Myproperty  # 等价于-->>total=Myproperty(total)
    def total(self):
        "求总的学费"
        return self.price * self.num


school = School('浙江大学', '浙江省杭州市', 12000, 6000)
print(school.total)
