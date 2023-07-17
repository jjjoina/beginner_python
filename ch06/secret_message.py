p = open('ch06/postcard.txt', 'r', encoding="UTF-8")

read = p.readlines()

# 개행문자 제거
for i in range(len(read)):
    read[i] = read[i].replace('\n', '')

# Q1
for i in range(len(read)):
    print(read[i])
print('-----------------------------------')

# Q2
for i in range(3, 9):
    print(read[i])
print('-----------------------------------')

# Q3
for i in range(3, 9):
    read[i] = read[i].replace(',', '')
    read[i] = read[i].replace('.', '')
    read[i] = read[i].replace(':', '')
    print(read[i])
print('-----------------------------------')

# Q4
for i in range(3, 9):
    read[i] = read[i].upper()
    print(read[i])
print('-----------------------------------')

# Q5
for i in range(3, 9):
    print(read[i].split()[0], read[i].split()[1], end=' ')