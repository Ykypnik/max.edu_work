s = input('ВВОД: ')

def palindrom(s):
    rev_s = s[::-1]
    if rev_s == s:
        return True
    return False


print(palindrom(s))