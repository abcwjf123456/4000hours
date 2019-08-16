# next方法
l = [1, 2, 3]
h = l.__iter__()
print(next(h))  # 其实next就是调用了__iter__()-->__next__()
