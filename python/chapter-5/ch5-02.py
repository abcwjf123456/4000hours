# 添加键值对，字典是一种动态结构。python不关心键值对的添加顺序，而只关心键和值之间的关联。


alien_0 = {'color': 'green', 'points': 4}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# {'color': 'green', 'points': 4}
# {'color': 'green', 'points': 4, 'x_position': 0, 'y_position': 25}
