import random

c = open('ch06/color.txt', 'r', encoding="UTF-8")
color = c.readlines()

f = open('ch06/food.txt', 'r', encoding="UTF-8")
food = f.readlines()

print(random.choice(color)[0:-1], end=' ')
print(random.choice(food)[0:-1])