# while continue 与 break区别
count = 1
while count <= 4:
    count += 1
    print(count)
    if count == 4:
        continue

    print('continue运行了')
    # 2
    # continue运行了
    # 3
    # continue运行了
    # 4
    # 5
    # continue运行了

count = 1
while count <= 4:
    count += 1
    print(count)
    if count == 4:
        break

    print('break运行了')
    # 2
    # break运行了
    # 3
    # break运行了
    # 4

