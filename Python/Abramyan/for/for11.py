# n = int(input('n: '));
# summa = 0;
# for i in range(n, 2 * n + 1):
#     a = i ** 2;
#     summa += a;
#     print(i, '=', a);
# print(summa);




n = int(input('n: '));
summa = 0;
for i in range(0, 2 * n + 1):
    a = (n + i) ** 2;
    summa += a;
    print(i, '=', a);
print(summa);