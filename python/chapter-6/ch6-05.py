# 删除包含特定值的列表元素
pets = ['dog', 'cat', 'goldfish', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# ['dog', 'goldfish']
