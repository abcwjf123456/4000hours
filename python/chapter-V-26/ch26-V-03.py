class Da:
    def __getattr__(self, item):
        print("gt")

    def __getattribute__(self, item):
        """大哥只有抛出异常时才会让小弟干活"""
        print("gb")
        raise AttributeError("抛出异常")


r1 = Da()
r1.x
