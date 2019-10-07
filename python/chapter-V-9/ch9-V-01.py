def func(start, end, a=0, b=0):
    for i in start:
        if i % 3 == 0 and i % 7 == 0:
            a += 1
            b += i
            start + 1
    if start == end:
     return a, b


func(1, 7)
