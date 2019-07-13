# for....in循环

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# alice
# david
# carolina


# 在for循环后面，没有缩进的代码都只执行一次
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ',that was a great trick')
    print("I can't wait to see your next trick," + magician.title() + "\n")
print("thank you")

# Alice,that was a great trick
# I can't wait to see your next trick,Alice
#
# David,that was a great trick
# I can't wait to see your next trick,David
#
# Carolina,that was a great trick
# I can't wait to see your next trick,Carolina
#
# thank you
