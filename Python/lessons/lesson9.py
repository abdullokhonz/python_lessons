# def func(a, b):
#     a = 1
#     b = 2
#     print(a, b)
#
#
# c = 5
# d = 10
# func(c, d)

# def func():
#     a, b, c = 1, 2, 3
#     print(a, b, c)
#
#
# a = 5
# b = 10
# c = 15
# func()

# a, b = map(int, input().split())
# print(type(a), b)

# d = ['1', '2', '3']
# e = list(map(int, d))
# a, b, c = map(int, e)
# print(type(a), b, c)

# a, b, c = map(int, input('>>>').split())
# print(a + b + c)

# a, b, c, d, e = map(int, input().split())
# print(a > 0 and b > 0 and c > 0 and d > 0 and e > 0)

# def fact(a):
#     s = 1
#     for i in range(1, a + 1):
#         s *= i
#     return s
#
#
# print(fact(int(input('a = '))))

# p = input('Enter password: ')
# while p == 'abc':
#     print('Правыльный пароль!')
#     break
# else:
#     print('Неправыльный пароль!')
#     p = input('Enter password: ')
#     if p == 'abc':
#         print('Правыльный пароль!')
#     else:
#         print('Неправыльный пароль!')

# p = input('Enter password: ')
# a = input('qwerty: ')
# while a == p:
#     print('Правыльный пароль!')
#     break
# else:
#     print('Неправыльный пароль!')
#     p = input('Enter password: ')
#     if p == 'abc':
#         print('Правыльный пароль!')
#     else:
#         print('Неправыльный пароль!')

# p = 'abc'
# while True:
#     a = input('Enter password: ')
#     if a != p:
#         print('Вы ввели неправильный пароль! \nПовторите попытку!')
#         a = input('Enter password: ')
#     else:
#         print('Nice!')

# p = input('Enter password: ')
# quess = input()
# counter = 0
# while p != quess:
#     counter += 1
#     print('Вы ввели неправильный пароль! \nПовторите попытку!')
#     quess = input()
# else:
#     print('Вы молодец!', 'Вы потратили', counter, 'попыток.')

a = input(">>>").lower()
s = 0
while a != 'stop':
    s += int(a)
    a = input('>>>')
else:
    print(s)
    print('Stop!')
