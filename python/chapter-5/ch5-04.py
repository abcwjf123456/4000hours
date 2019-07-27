# 字典修改一个有趣的例子
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住

alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(str(alien['x_position']))
alien['speed'] = 'lower'
if alien['speed'] == 'lower':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
print("new speed" + " " + str(alien['x_position'] + x_increment))



# 0
# new speed 1

