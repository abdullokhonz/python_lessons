# a = [i for i in range(5)]
# print(a)

# list1 = [5, 10, 33, 0, 46, -7, -10]
# a = [i for i in list1 if i % 2 == 0 and i > 0]
# print(a)

# n, m = int(input('>>>')), int(input('>>>'))
# matrix = [[0] * m for i in range(n)]
# print(matrix)

# n, m = int(input('>>>')), int(input('>>>'))
# matrix = [[j for j in range(m)] for i in range(n)]
# for i in matrix:
#     print(i)
# print(*matrix, sep="\n")

# list1 = [1, 2, 3]
# a = iter(list1)
# print(a.__next__())

# print([i for i in range(10, 0, -1)])
# print([i for i in range(1, 11) if i % 2 == 0])

# a = input('>>>')
# print([i for i in a if 100 <= ord(i) >= 110])

# a = map(int, input('>>>').split())
# print([i for i in a if i ** 2 <= 50 and i not in [5, 7, 1]])
