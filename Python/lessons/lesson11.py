# def func(list1):
#     list2 = []
#     list3 = []
#     for i in list1:
#         if i % 2 == 0:
#             list2.append(i)
#         if i % 2 != 0:
#             list3.append(i)
#     return list2, list3
#
#
# print(func(list(map(int, input('>>>').split()))))

# def func(list):
#     s = 0
#     for i in list:
#         s += i
#     return s
#
#
# print(func(map(int, input('>>>').split())))

# a = list(map(int, input('>>>').split()))
# b = map(int, input('>>>').split())
# print(type(a), a, type(b), list(b))

# a = 1, 2, 3
#
# print(type(a), sum(a))

# def func(a):
#     s = 0
#     for i in a:
#         k += 1
#         s += i
#     return s / len(a)
#
#
# print(func(map(int, input('>>>').split())))

# n = int(input('n: '))
# a = []
# while len(a) != n:
#     a.append(int(input('a: ')))
# s = 0
# p = 1
# for i in a:
#     s += i
#     p *= i
# # print('Sum:', s, 'Pro:', p, sep='\n')
# print(f'Sum: {s}\nPro: {p}')

# n = int(input('n: '))
# a = []
# b = []
# while len(b) != n:
#     b.append(float(input('b: ')))
# s = 0
# for i in b:
#     if i % 1 == 0:
#         a.append(i)
# for i in a:
#     if i >= 0:
#         s += i
# a.sort()
# print(a, 'Summa: ', s)

# a = input('a: ')
# print(a[::-1] == a) # polindrom
