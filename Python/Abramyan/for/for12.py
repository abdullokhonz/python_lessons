n = int(input('x = '));
p = 1;
for i in range(11, n + 1):
    i *= 0.1;
    p *= i;
    print(i);
print(p);