# 确定列表不是空的

requested_toppings = []
# 判断是否为空为空时返回false
if requested_toppings:
    for requested_topping in requested_toppings:
        print('adding' + requested_topping)
    print('finised')
else:
    print('sorry')
