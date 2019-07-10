# 删除
motorcycles = ['honda', 'yamaha', 'suzuli']
print(motorcycles)
del motorcycles[0]
del motorcycles[1]
print(motorcycles)

# ['honda', 'yamaha', 'suzuli']
# ['yamaha']
# del可以删除任何位置处的列表元素前提知道索引值并且删除后再也无法访问


# pop()删除
motorcycles = ['honda', 'yamaha', 'suzuli']
print(motorcycles)
pop_motorcycles = motorcycles.pop()
print(motorcycles)
print(pop_motorcycles)

# ['honda', 'yamaha', 'suzuli']
# ['honda', 'yamaha']
# suzuli


motorcycles = ['honda', 'yamaha', 'suzuli']
first_owned = motorcycles.pop(0)  # 每次使用pop()时，被弹出来的元素就不在列表中了
print(motorcycles)
print(first_owned)

# ['yamaha', 'suzuli']
# honda
# 怎么确定是使用del语句还是pop()方法如果你删除一个元素且不再以任何方式使用它就用del语句，
# 如果你要删除元素还能继续使用它就使用方法pop()


# remove() 没有返回值
# 有时你不知道要从列表中删除元素的位置只知道元素值开使用remove()方法
motorcycles = ['honda', 'yamaha', 'suzuli']
print(motorcycles)
motorcycles.remove('suzuli')
print(motorcycles)

# ['honda', 'yamaha', 'suzuli']
# ['honda', 'yamaha']

motorcycles = ['honda', 'yamaha', 'suzuli', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(too_expensive.title())  # 值ducati还在too_expensive中但从列表中已经删除了

# ['honda', 'yamaha', 'suzuli', 'ducati']
# ['honda', 'yamaha', 'suzuli']
# Ducati
