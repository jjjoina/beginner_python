def palindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    print(s == s[::-1])

palindrome('AnNa')
