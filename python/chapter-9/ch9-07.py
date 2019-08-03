# 继承
# 将实例做属性
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def red_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has" + str(self.odometer_reading) + "miles on it")

    def update_odometer(self, mileage):
        """将里程读数设定为指定值"""
        """禁止将函数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self, mil):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mil

    def fill_gas_tank(self):
        print('有油箱')


class Battery():
    """一次模拟电动车汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def decribe_battery(self):
        """打印描述电瓶容量的消息"""
        print(str(self.battery_size))


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类与电车属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
        # self.battery_size = 70

    # def describle_battery(self):
    #     """"""
    #     print(str(self.battery_size))

    """重写父类"""

    def fill_gas_tank(self):
        print("没有油箱")


my_tesla = ElectricCar('tesla', 'model', 2016)
print(my_tesla.get_descriptive_name())
# my_tesla.describle_battery()
# my_tesla.fill_gas_tank()
my_tesla.battery.decribe_battery()
