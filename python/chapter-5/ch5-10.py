# 嵌套
aliens = []
for new_aliens in range(10):
    aliens_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(aliens_0)
print(aliens)

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
        print(alien)

for alien in aliens[:5]:
    print(alien)


