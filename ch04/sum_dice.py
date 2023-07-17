dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)

s = set()

for a in dice1:
    for b in dice2:
        s.add(a + b)

print(s)
