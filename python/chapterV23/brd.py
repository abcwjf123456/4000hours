class Da:
    def __init__(self,name):
        self.name=name
        # print("调用了%S" %self.name)
        pass
    def put(self):
        print("有该函数")
        print(self.name)