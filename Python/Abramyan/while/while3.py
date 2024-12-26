n, k = int(input('n = ')), int(input('k = '));
s = 0;
while n >= k:
    n -= k;
    s += 1;
print(n);
print(s);