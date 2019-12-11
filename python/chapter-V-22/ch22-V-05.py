class Mj:
    def __init__(self, height, width):
        self.width = width
        self.height = height

    @property
    def cal(self):
        return self.height * self.width


rr = Mj(100, 100)
print(rr.width)
print(rr.cal)  # 静态属性
