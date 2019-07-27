# 检查特殊元素

requested_toppings = ['mushroom', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        # 检查是否有辣椒
        print('sorry,we are out of green peppers right now')
    else:
        print('Adding' + ' ' + requested_topping)
print('Finished')
