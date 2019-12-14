# 接口继承
import abc


class All(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dd(self):
        pass

    @abc.abstractmethod
    def gg(self):
        pass


class Gf(All):
    def hh(self):
        print("hh")

    def dd(self):
        print('dd')

    def gg(self):
        print("dd")


r1 = Gf()
r1.dd()
