# 通过方法修改属性的值
# 给属性指定默认值
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

    def update_odometer(self, mileage):
        """将里程读数设定为指定值"""
        """禁止将函数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(10)
my_new_car.red_odometer()
