#
class Da:
    def __init__(self):
        pass

    def run(self):
        print("run")


class Di(Da):
    def __init__(self, age):
        self.age=age
        super().__init__()
        super().run()
        print(self.run())


r1 = Di(1)
r1.run()
