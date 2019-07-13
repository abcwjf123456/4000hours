# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:2])
print(players[2:4])
print(players[1:])
print(players[-3:])
for play in players[1:]:
    print(play)

# ['charles', 'martina']
# ['michael', 'florence']
# ['martina', 'michael', 'florence', 'eli']
# ['michael', 'florence', 'eli']
# martina
# michael
# florence
# eli
