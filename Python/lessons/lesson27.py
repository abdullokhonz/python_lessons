# def h1(func):
#     def inner(*args, **kwargs):
#         print('<h1>')
#         func(*args, **kwargs)
#         print('</h1>')
import math


#     return inner


# def table(func):
#     def inner(*args, **kwargs):
#         print('<table>')
#         func(*args, **kwargs)
#         print('</table>')

#     return inner


# @table
# @h1
# def say(name, surname, age):
#     print('hello', name, surname, age)


# # a = table(h1(say))
# say('Zam', 'Bajzaeva', 41)


# def decorator(func):
#     def sum_list(x):
#         return func(x) ** 2
#     return sum_list


# @decorator
# def say(x):
#     return sum(x)


# print(say([2, 2, 2, 4]))

# def decorator(func):
#     def inner(x):
#         return math.sqrt(func(x))
#
#     return inner
#
#
# @decorator
# def say(x):
#     return max(x)
#
#
# print(say([1, 2, 3, 5, 7, 9]))

# def decorator(func):
#     def inner(x):
#         return func(x).upper()
#
#     return inner
#
#
# @decorator
# def say(x):
#     return x[::-1]
#
#
# print(say('qwerty'))

