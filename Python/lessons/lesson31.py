# def func(x):
#     print(x)
#     func(x)
#
#
# func(3)

# def func(x):
#     if x < 4:
#         print(x)
#         func(x + 1)
#         print(x)
#
#
# func(0)

# f[n] = f[n - 1] + f[n - 2]

# def fib(x):
#     if x <= 1:
#         return x
#     return fib(x - 1) + fib(x - 2)
#
#
# print((fib(7)))

# def func(x):
#     lst = [0, 1]
#     for i in range(1, x + 1):
#         lst.append(lst[-1] + lst[-2])
#     return lst[-1]
#
#
# print(func(5))

# lst = []
# for i in range(10):
#     lst.append(int(input('>>>')))
# print(lst)
# for i in reversed(lst):
#     if lst[0] < i < lst[-1]:
#         print(i)
#         break
# else:
#     print(0)

# n, k, l = int(input('>>>')), int(input('>>>')), int(input('>>>'))
# lst = []
# for i in range(n):
#     lst.append(int(input('>>>')))
# print(lst)
# s = 0
# for i in range(len(lst)):
#     if k <= i <= l:
#         s += lst[i]
# print(s)

# def func(x):
#     s = 0
#     s += 1
#     if s <= x:
#         func(x - 1)
#         print(x)
#
#
# func(10)

# def func(a, b):
#     if a < b:
#         print(a)
#         return func(a + 1, b)
#     elif a > b:
#         print(a)
#         return func(a - 1, b)
#     return a
#
#
# print(func(int(input('>>>')), int(input('>>>'))))

# ____________________________ Не зовершено ____________________________________
# def a(m, n):
#     if m > 0 and n == 0:
#         n += 1
#         return a(m - 1, 1)
#     elif m > 0 and n > 0:
#         n += 1
#         return a(m - 1, a(m, n - 1))
#
#
# print(a(int(input('>>>')), int(input('>>>'))))

def func(n):
    pass


print(func(int(input('>>>'))))
