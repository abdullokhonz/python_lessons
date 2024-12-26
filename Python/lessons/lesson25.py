# def func(x):
#     return x ** 2
#
#
# print(func(10))
#
# var1 = lambda x, y, z: (x, y, z)
# print(var1(5, 10, 15))

# q = lambda x: x.isdigit()
# print(q(input('>>>')))


# def func(x):
#     return x % 2 == 0
#
#
# list1 = [10, 2, -7, 18, 20, 35, 9]
# list1 = list(filter(func, list1))
# list1 = list(filter(lambda x: x % 2 == 0, list1))
# print(list1)

# print(list(filter(lambda x: len(x) == 6, ['hello', 'world', 'qwerty'])))
# print(list(filter(lambda x: x // 2 if x % 2 == 0 or x <= 47 else None, list(map(int, input('>>>').split())))))
# numbers = [1, 45, 46, 49, 232913, 123, 32]
# print(*map(lambda y: y >> (~y & 1), filter(lambda x: ~x & 1 or x < 48, numbers)))

# def func(x):
#     if x < 47 and x % 2 != 0:
#         return bool
#     elif x % 2 == 0:
#         x //= 2
#         return bool
#     else:
#         return bool
#
#
# print(*list(filter(func, list(map(int, input('>>>').split())))))

# a = [('John', 35), ('Anna', 25), ('Mike', 40)]
# b = lambda x: sorted(x)
# print(b(a))

# numbers = [-10, -7, 2, 3, 11, -2, 0]
# print(list(filter(lambda x: x > 0, numbers)))

# names = ['one', 'two', 'three']
# numbers = [1, 2, 3]
# a = lambda x, y: [tuple((x[i], y[i])) for i in range(len(names))]
# print(*a(names, numbers))

# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# print(reduce(lambda x, y: x * y, numbers))

# numbers = [10, 20, 30, 40, 50]
# print(list(map(lambda x: x + 10, numbers)))
