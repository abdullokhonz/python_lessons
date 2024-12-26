def for19(n):
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a


x = float(input('x = '))
n = int(input('n = '))
s = 0
for i in range(n + 1):
    s = x ** i / for19(i)
print(s)
