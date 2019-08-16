# seek
# seek默认从0开始,1为顺序但再次seek时相对位置是前一光标位置，2为倒序之后和1一样
with open('seek.txt','rb') as hh:
    f=hh.seek(3,1)
    print(f)


