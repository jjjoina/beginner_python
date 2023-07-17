n = int(input())
l = []

while True:
    n, r = divmod(n, 2)
    l.insert(0, r)
    if n == 0:
        break

print(l)
