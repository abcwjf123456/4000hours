class A:
    def __init__(self, name):
        self.name = name

    @property
    def sett(self):
        print("sett")

    @sett.setter
    def sett(self, vale):
        print("seet", vale)


f1 = A(1)
f1.sett = "aa"
