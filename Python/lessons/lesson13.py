# a = float(input('$: '))
# print('TJS: ', a * 10.92)

# a = [1, 2, 3]
# print(a, *a)

# *a, b, c = [10, 20, 30, 40, 50]
# print(a, b, c)

# *a, b, c = [10, 20]
# print(a, b, c)

# def func(a, b, c, d):
#     print(a, b, c, d)
#
#
# a = [True, 'abc', 78, 5.2]
# func(*a)

# def func(*args):
#     print(*args, args[1])
#
#
# func(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# def func(*args, **kwargs):
#     print(args, kwargs)
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# func(1, 23, 'ad', a=1, b=4)

# def func(*args):
#     p = 1
#     for i in args:
#         p *= i
#     return p
#
#
# print(func(*map(int, input('>>>').split())))

# def func_abs(x1, x2):
#     return abs(x2 - x1)
#
#
# print(func_abs(2, 4))

# def func_int10(a):
#     last = a % 10
#     mid = (a // 10) % 10
#     first = a // 100
#     return last, mid, first
#
#
# print(func_int10(123))

# def func(x):
#     x = str(x)
#     list_of_digits = list(map(int, list(x)))
#     list_of_digits.reverse()
#     return list_of_digits
#
#
# print(*func(123))

# def if11(a, b):
#     if a != b:
#         c = [a, b]
#         a = max(c)
#         b = max(c)
#     else:
#         a = 0
#         b = 0
#     return a, b
#
#
# print(if11(4, 5))

# match (int(input('>>>'))):
#     case 1:
#         print('Winter')
#     case 2:
#         print('Spring')
#     case 3:
#         print('Summer')
#     case 4:
#         print('Autumn')
#     case _:
#         raise ValueError('ERROR!!!')

# for i in range(10, 0, -1):
#     print(i)
