# print('*' * 17)
# print('*' + ' ' * 15 + '*')
# print('*' + ' ' * 15 + '*')
# print('*' * 17)

# a, b, c, d = map(float, input('>>>').split())
# print(a ** c + b ** d)

# num = int(input('1 - 9 >>>'))
# print(num + int(str(num) + str(num)) + int(str(num) + str(num) + str(num)))
# print(num + num * 11 + num * 111)

# year = list(map(int, input('>>>')))
# print(year[-1] == 0 and year[-2] == 0)
# print('Yes' if year[-1] == 0 and year[-2] == 0 else 'No')
# print('Yes' if int(input('>>>')) % 100 == 0 else 'No'))

# gender, age = input('F or M: '), int(input('Age 10 - 15: '))
# print('Вы прошли!' if input('F or M: ') == 'f' and 10 <= int(input('Age 10 - 15: ')) <= 15 else 'Вы не прошли!')

# x1, y1, x2, y2 = map(int, input('>>>').split())
# if x1 % 2 != 0 and y1 % 2 != 0 and x2 % 2 != 0 and y2 % 2 != 0:
#     print('Yes, black')
# elif x1 % 2 == 0 and y1 % 2 == 0 and x2 % 2 == 0 and y2 % 2 == 0:
#     print('Yes, white')
# else:
#     print('No, different color')

# x1, y1, x2, y2 = map(int, input('>>>').split())
# if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
#     print('Yes, black')
# elif (x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0:
#     print('Yes, white')
# else:
#     print('No, different color')

# print('Yes!' if (int(input('x1: ')) + int(input('y1: '))) % 2 == 0 and (int(input('x2: ')) + int(input('y2: '))) % 2 == 0 else 'No!')
# print('Yes!' if (int(input('x1: ')) + int(input('y1: '))) % 2 == (int(input('x2: ')) + int(input('y2: '))) % 2 else 'No!')



# a = ['hello world']
# print(a[0][::-1])

# mat = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         print(mat[i][j], end=' ')
#     print()

# list1 = [10, 20, 10, 20, 30, 30]
# print(*set(list1))

# a = int(input('>>>'))
# s = ''
# for i in range(1, a + 1):
#     s += str(i)
#     print(s)

# n, m = map(int, input('>>>').split())
# spisok = []
# for i in range(n):
#     spisok.append([0] * m)
# for i in range(n):
#     for j in range(m):
#         if i % 2 != 0:
#             if j % 2 != 0:
#                 spisok[i][j] = '*'
#             else:
#                 spisok[i][j] = '.'
# for i in spisok:
#     print(*i)

# n, m = [int(i) for i in input().split()]
# a = []
# for i in range(n):
#     a.append([])
#     for j in range(m):
#         if (i + j) % 2 == 0:
#             a[i].append('.')
#         else:
#             a[i].append('*')
# for row in a:
#     print(' '.join(row))
