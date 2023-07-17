score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]

stem_leaf = [[], [], []]

# ex1
for s in score:
    q, r = divmod(s, 10)
    stem_leaf[q].append(r)

print(stem_leaf)

# ex2
for i in range(len(stem_leaf)):
    print(f'{i}:', stem_leaf[i])
