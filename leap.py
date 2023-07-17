year = int(input())
leap = 'n'
if year % 4 == 0:
    leap = 'y'
if year % 100 == 0:
    leap = 'n'
if year % 400 == 0:
    leap = 'y'

if leap == 'y':
    print(f'{year}년은 윤년입니다.')
elif leap == 'n':
    print(f'{year}년은 평년입니다.')
