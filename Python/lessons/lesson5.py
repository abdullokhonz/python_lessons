# for i in range(60):
#     for j in range(60):
#         print(i, ':', j)

# for i in range(1, 10):
#     for j in range(1, 11):
#         print(j, '*', i, '=', i*j, end=';   ')
#     print()

# counter = 0
# for b1 in 'тыква':
#     for b2 in 'тыква':
#         for b3 in 'тыква':
#             for b4 in 'тыква':
#                 for b5 in 'тыква':
#                     for b6 in 'тыква':
#                         word = b1 + b2 + b3 + b4 + b5 + b6
#                         if word[0] in 'ткв' and word[-1] in 'ткв':
#                             if word.count('ы') + word.count('а') == 2:
#                                 counter += 1
# print(counter)

# n = int(input('n = '))
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print(s)

# n = int(input('n = '))
# # a = [0, 1, 3, 5, 8, 13]
# a = [0] * (n + 1)
# a[1] = 1
# for i in range(2, n):
#     a[i] = a[a - 1] + a[i - 2]
# print(a[n])

# for i in range(13, 345, 11):
#     n = i
#     s = 0
#     while n > 0:
#         s += n % 10
#         n //= 10
#     print('Сумма цифр', i, 'равняется', s)

# n = int(input('n = '))
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()

# n = int(input('n = '))
# for i in range(n):
#     for j in range(3):
#         print(i, end=' ')
#     print()

# n = int(input('n = '))
# for i in range(n):
#     for j in range(3):
#         print(j, end=' ')
#     print()

# n = int(input('n = '))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# n = int(input('n = '))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, j, end=' ')
#     print()

# n = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in n:
#     for j in i:
#         print(j, end=' ')
#     print()

# n = [1, 2, 3, 4, 5, 6, 6, 6]
# print(n)

# n = [1, 2, 3, 4, 5, 6, 6, 6]
# print(*n)

# n = {1, 2, 3, 4, 5, 6, 6, 6}
# print(n)

# n = {1, 2, 3, 4, 5, 6, 6, 6}
# print(*n)
