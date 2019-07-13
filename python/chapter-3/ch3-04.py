# 列表解析
spuares = []
for spuare in range(1, 11):
    spuares.append(spuare ** 2)
print(spuares)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

spuares = [spuare ** 2 for spuare in range(1, 11)]
print(spuares)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
