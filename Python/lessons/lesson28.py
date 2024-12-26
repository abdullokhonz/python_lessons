# a, b = [3, 4, 5], list(map(int, input().split()))
# print(sorted(a + list(b)))

# import math
# import pprint
# pprint.pprint(locals())
# print(math.ceil(5.1))
# print(round(4.6, 0))

# from math import e, factorial

# from random import random as r

# STROKA = 'abc'
#
#
# def func1(x):
#     print('func1:', x)

# a = input()
# list1 = [a[i] if i % 2 == 1 else a[i].upper() for i in range(len(a))]
# print(*list1, sep='')

# def more_than_five(lst):
#     # new_lst = [i for i in lst if 5 < abs(i)]
#     # for i in lst:
#     #     if 5 < abs(i):
#     #         new_lst.append(i)
#     # return new_lst
#     return [i for i in lst if 5 < abs(i)]

# letters = 'UYUYguhbuhbewuyvYUvygevwd'
# for letter in letters:
#     if letter.upper() == letter:
#         letters = letters.replace(letter, '')
# print(letters)

# abc = []
# qwerty = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# s = 0
# for i in range(11):
#     abc.append([''] * 3)
# for i in range(11):
#     for j in range(3):
#         abc[i][j] = qwerty[s].upper() + qwerty[s]
#         s += 1
# for i in abc:
#     print('^^^^^^^^^^^^^^^^^^')
#     print('| ', end='')
#     print(*i, sep=' || ', end='')
#     print(' |')
# print('^^^^^^^^^^^^^^^^^^')

# rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# for position in range(11):
#     print('^' * 27)
#     for letter in rus_lower:
#         if rus_lower.index(letter) % 11 == position:
#             print('| ', letter.upper(), letter, ' |', end='')
#     print()
# print('^' * 27)

# def change(lst):
#     x = lst[0]
#     lst[0] = lst[-1]
#     lst[-1] = x
#     return lst
#
#
# print(change(['a', 'b', 'c']))

# def change(lst):
#     new_start = lst.pop()
#     new_end = lst.pop(0)
#     lst.append(new_end)
#     lst.insert(0, new_start)
#     return lst

# def to_list(*args):
#     return list(args)
#
#
# print(to_list(1, 'a', ['a', 2], True))

# def useless(s):
#     return max(s) / len(s)
#
#
# print(useless([1, 2, 3, 4, 5, 6, 7, 8, 123]))

# def list_sort(lst):
#     return list(reversed(sorted(set(lst))))
#
#
# print(list_sort([1, 1, 2, 2, 3, 3]))

# def list_sort(lst):
#     lst.sort(key=lambda x: abs(x), reverse=True)
#     return lst

# from sys import getsizeof as gso
# print(gso(3 ** 9090001) / (1024 ** 2))
