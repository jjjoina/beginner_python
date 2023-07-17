def sumOfDigits(n):
    templist = list(map(int, str(n)))
    print(sum(templist))

if __name__ == '__main__':
    sumOfDigits(47253)
    sumOfDigits(643)
