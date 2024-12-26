a = int(input('a: '));
b = int(input('b: '));
sk = 0;
for i in range(a, b + 1):
    sk += i ** 2;
print(sk);