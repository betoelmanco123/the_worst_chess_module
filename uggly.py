positioons = []
p = 0
for y in range(1, 9):
    for x in range(1, 9):
        if y == 7 or y == 2:
            p = 'p'
        else:
            p = 0
        
        positioons.append({(x, y): p})

print(positioons)