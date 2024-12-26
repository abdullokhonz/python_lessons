a = float(input('a = '));
n = int(input('n = '));
b = int(a);
x = 0;
s = 1;
for i in range(0, (-1) ** n * b ** n):
    x = a ** i * s;
    s *= -1;
    print(x);