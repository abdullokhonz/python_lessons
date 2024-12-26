n = int(input('n = '));
x = 1;
s = 0;
while n > x:
    x *= 2;
    s += 1;
print(n == x);
print('s =', s);