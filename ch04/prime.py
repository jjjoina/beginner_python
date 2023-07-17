maximum = int(input())

prime = list(range(2, maximum + 1))

for a in range(2, maximum + 1):
    for b in range(2 * a, maximum + 1, a):
        if b in prime:
            prime.remove(b)

print(prime)
