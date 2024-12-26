from math import factorial

n = int(input('n = '));
s = 0;
for i in range(1, n + 1):
    s += factorial(i);
print(s)