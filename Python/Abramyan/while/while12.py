n = int(input('n = '));
k = 0;
s = 0;
while s <= n:
    k += 1;
    s += k;
print(k - 1);
print(s - k);