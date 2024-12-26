x = map(int, input('Enter 10 digits: ').split())
s = 0
p = 0
for i in x:
    s += i
    p += 1
print(s / p)
