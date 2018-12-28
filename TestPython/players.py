players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

#遍历切片
for player in players[:3]:
    print(player)

# 复制列表
copy_players = players[:]
print(copy_players)