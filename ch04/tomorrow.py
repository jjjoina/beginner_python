year, month, day = tuple(map(int, input().split(' ')))
print("%02d/%02d/%04d" % (month, day, year))

caution_list = [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30)]

if (month, day) in caution_list:
    month += 1
    day = 1
elif (month, day)  == (12, 31):
    year += 1
    month, day = 1, 1
else:
    day += 1

print("%02d/%02d/%04d" % (month, day, year))
