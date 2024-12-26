a = int(input());
b = int(input());
n = 0;
for i in range(b - 1, a, -1):
    n += 1;
    print(i);
print(n)