# 传递任意数量的实参
# *toppings形参中的*号让python创建一个名为toppings的空元组

def make_pizza(*toppings):
    """打印所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushromm', 'green peppers', 'extra cheese')

# ('pepperoni',)
# ('mushromm', 'green peppers', 'extra cheese')
