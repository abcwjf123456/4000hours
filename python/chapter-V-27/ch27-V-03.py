f_dic = {
    "yym": "{0.value}"
}


class A:
    def __init__(self, value):
        self.value = value

    def __format__(self, format_spec):
        return {"0.value"}.format(format_spec)


r1 = A(2)
