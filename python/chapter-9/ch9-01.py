# 创建与使用类
class Dog():
    """第一次模拟小狗简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗坐下"""
        print(self.name.title())

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title())


# 实例化
my_dog = Dog('fff', 6)
"""调用属性"""
print(my_dog.name)
print(str(my_dog.age))
"""调用方法"""
my_dog.sit()
my_dog.roll_over()
