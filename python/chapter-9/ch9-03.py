# 修改属性的值
# 直接修改属性的值
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
        print("This car has" + " " + str(self.odometer_reading) + " " + "miles on it")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
"""直接修改属性"""
my_new_car.odometer_reading = 20
my_new_car.red_odometer()

# 2016 Audi A4
# This car has 20 miles on it
