n = int(input());
k = 0;
s = 0;
while n > 0:
    k += 1;
    last = n % 10;
    s += last;
    print(last);
    n //= 10;
print('k = ', k);
print('s = ', s);