from python.chapterV23 import brd

r1=brd.Da("gg")

if hasattr(r1,"put"):
    fun=getattr(r1,"put")
    fun()
else:
    print("没有该函数")