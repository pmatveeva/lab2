def rewrite (st):
    n = len(st) - 1
    str0 = ''
    while n != -1:
        str0 += st[n]
        n -= 1
    return str0

str1 = (input("Введите строку "))
print(rewrite(str1))
str1 = (input("Введите строку "))
print(rewrite(str1))
