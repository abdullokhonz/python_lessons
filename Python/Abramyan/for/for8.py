a = int(input('a: '));
b = int(input('b: '));
p = 1;
for i in range(a, b + 1):
    p *= i;
print(p);