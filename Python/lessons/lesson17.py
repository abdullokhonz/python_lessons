# n = int(input('n: '))
# m = int(input('m: '))
# s = 0
# mat = [[s] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         mat[i][j] += s
#         s += 1
# p = [print(i) for i in mat]
# [p for i in range(n) for j in range(m)]

# list1 = list(map(int, input('>>>').split()))
# list1 = [int(i) for i in input('>>>').split()]
# min1 = list1.index(min(list1))
# max1 = list1.index(max(list1))
# list1[min1], list1[max1] = max(list1), min(list1)
# print(list1)

# list1 = sorted(list(map(int, input('>>>').split()))); print(list1, list1[::-1], sep='\n')

# [print(i ** 2, end='\n') for i in range(1, int(input('>>>')) + 1)]

# print(*[i ** 2 for i in range(1, int(input('>>>')) + 1)], sep='\n')

# class Cat():
#     weight = 10
#
#     def say_meow(self):
#         print('meow')
#
#
# b = Cat()
# b.say_meow()
# print(b.weight)
