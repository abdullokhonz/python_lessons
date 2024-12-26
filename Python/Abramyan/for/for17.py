a = int(input('a = '));
n = int(input('n = '));
s = 0;
for i in range(0, n + 1):
    s += a ** i;
    print(a ** i);
print(s);