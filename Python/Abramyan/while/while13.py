a = int(input('a = '));
k = 1;
s = k;
while s < a:
    k += 1;
    s += 1 / k;
print(k);
print(s);