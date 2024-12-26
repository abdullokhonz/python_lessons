# def func():
#     counter = 0
#
#     def inside():
#         nonlocal counter
#         counter += 1
#         print('Вы нажали', counter, 'раз!')
#
#     return inside
#
#
# count1 = func()
# count1()
# count1()
# count1()
# count1()
# count2 = func()
# count2()

# def func(name, age):
#     def inside():
#         print(f'Name: {name}\nAge: {age}')
#     return inside
#
#
# a = func('Alice', 18)
# a()

# def inside(max_num):
#     print(max_num)
#
#
# def func(list_of_numbers, fun):
#     maximum = max(list_of_numbers)
#     fun(maximum)
#
#
# func([1, 2, 3, 4, 5], inside)

# def func(list1, num):
#     s = 0
#     for i in range(1, len(list1), 2):
#         s += list1[i]
#     num(s)
#
#
# def inside(n):
#     print(n)
#
#
# func([1, 2, 3, 4, 5], inside)

# def decorator(func):
#     def inside():
#         print('hi')
#         func()
#         print('Bye')
#
#     return inside
#
#
# @decorator
# def fun():
#     print('hello world!!!')
#
#
# fun()
# # decorator(fun)
# # a = decorator(fun)
# # a()
