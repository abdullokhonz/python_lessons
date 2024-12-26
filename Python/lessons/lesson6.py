# print('hello world!')
# for i in range(60):
#     for j in range(60):
#         for k in range(60):
#             print(i, ':', j, ':', k)

# a = [[0, 2, 4, 6], [1, 3, 5, 7], [3, 5, [1, 2, 3], 8, 10]]
# # print(a[2][2][2])
# for i in a:
#     for j in i:
#         print(j, end=' ')
#     print()

# a = [1, 2, 3]
# for i in a:
#     print(i, end=' ')


# a = [
#     [0, 1, 2, 3],
#     [4, 5, 6, 7],
#     [8, 9, 10, 11],
#     [12, 13, 14, 15]
# ]
# for i in range(len(a)-1, -1, -1):
#     for j in range(len(a)-1, -1, -1):
#         print(a[i][j], end=' ')
#         # if i == j:
#         #     print(a[i][j], 'osnovnaya diagonal')
#         # elif i < j:
#         #     print(a[i][j], 'vishe osnovnoy diagonali')
#         # else:
#         #     print(a[i][j], 'nijhe osnovnoy diagonali')
#     print()

# a = [1, 2, 3]
# for i in range(len(a)-1, -1, -1):
#     print(a[i])

# for i in range(len(a)):
#     for j in range(len(a)):
#         print(a[j][i], end=' ')
#     print()


# n = int(input('n = '))
# m = int(input('m = '))
# a = []
# for i in range(n):
#     b = []
#     for j in range(m):
#         elem = int(input('c = '))
#         b.append(elem)
#     a.append(b)
# print(a)

# n = int(input('n = '))
# a = []
# for i in range(n):
#     a.append([0] * n)
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             a[i][j] = 0
#         elif i > j:
#             a[i][j] = 1
#         else:
#             a[i][j] = 2
#     #     print(a[i][j], end=' ')
#     # print()
# for i in a:
#     print(i)


# n = int(input('n = '))
# m = int(input('m = '))
# a = []
# s = 0
# for i in range(n):
#     a.append([0] * m)
# for i in range(n):
#     for j in range(m):
#         s += 1
#         a[i][j] = s
#     #     print(a[i][j], end=' ')
#     # print()
# for i in a:
#     print(i)
