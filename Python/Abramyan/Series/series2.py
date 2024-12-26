x = map(int, input('Enter 10 digits: ').split())
s = 1
for i in x:
    s *= i
print(s)
