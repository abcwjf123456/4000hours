class Mj:
    tag = 1

    def __init__(self, height, width):
        self.width = width
        self.height = height

    # @property
    # def cal(self):
    #     return self.height * self.width

    def cal2(self):
        return self.tag


rr = Mj(100, 100)
print(Mj.cal2(rr))  # 类方法
