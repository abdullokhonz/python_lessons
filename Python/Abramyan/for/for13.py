# n = int(input('n = '));
# x = 0;
# s = 1;
# for i in range(11, n + 1):
#     x += i * 0.1 * s;
#     s *= -1;
# print(x);




n = int(input('n = '));
s = 0;
a = -1;
for i in range(11, n * 10 + 1):
    a *= -1;
    s += (i * 0.1 * a);
print(a);