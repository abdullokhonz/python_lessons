n = int(input('n = '));
a = 1;
s = 0;
for i in range(1, n + 1):
    i *= i;
    a /= i;
    s += a;
    print(a);
print(s);