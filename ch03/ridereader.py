def read(text):
    ridename, limit = map(str.strip, text.split(':'))

    cmmin = cmmax = None
    
    if '이상' in limit:
        cmmin = int(limit.split('cm')[0])

    elif '~' in limit:
        cmmin, cmmax = list(map(lambda x: x.replace('cm', ''), limit.split('~')))
    
    return ridename, cmmin, cmmax

if __name__ == '__main__':
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)
