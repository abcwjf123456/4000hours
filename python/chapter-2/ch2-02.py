# 修改
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'Ducati'
print(motorcycles)

# ['honda', 'yamaha', 'suzuki']
# ['Ducati', 'yamaha', 'suzuki']


# 添加
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')  # append()将元素附加到列表末尾
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 输出
# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha', 'suzuki', 'ducati']
# ['honda', 'yamaha', 'suzuki']


# 插入
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')  # insert()可在列表任何位置插入
print(motorcycles)
# 忘了层叠列表

# ['honda', 'yamaha', 'suzuki']
# ['ducati', 'honda', 'yamaha', 'suzuki']
