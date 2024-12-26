b = 10;
p = float(input('p = '));
k = 0;
while b <= 200:
    k += 1;
    b += b * p / 100;
print(k, "=", b);