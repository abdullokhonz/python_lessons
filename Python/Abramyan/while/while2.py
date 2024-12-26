a, b = int(input('a = ')), int(input('b = '));
s = 0;
while a >= b:
    a -= b;
    s += 1;
print(s);