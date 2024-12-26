# print('Hello, please enter your name, surname and age!')
#
#
# def registrationPage(name, surname, age):
#     print('Welcome', name)
#     print('Successfull registration:', name, surname, age)
#
#
# registrationPage(input('Your name: '), input('Your surname: '), int(input('Your age: ')))

# a = 123
# print((a // 10) % 10)

# a = 'hello'
# print(a[::-1])

# def say_hi():
#     print('hello')
#     print('hi')
#     print(123)
#
#
# say_hi()

# def square(x):
#     print(f'{x}^2', '=', x ** 2)
#     return x ** 3
#
#
# print(square(int(input('x = '))))

# def square(x):
#     if x % 2 == 0:
#         return "chetnoe"
#     # return "chetnoe"
#     # or
#     else:
#         return "nechetnoe"
#
#
# print(square(5))

# def www(a, b):
#     return a ** b
#
#
# print(www(2, 2))

# def ex(a, b):
#     if a > b:
#         return a
#     elif a < b:
#         return b
#     return a, b
#
#
# print(ex(4, 5))

# def fed(a, b):
#     s = 0
#     for i in range(a, b + 1):
#         s += i
#     return s
#
#
# print(fed(1, 5))

def pro(n, m):
    a = []
    s = 0
    for i in range(n):
        a.append([0] * m)
    for i in range(n):
        for j in range(m):
            s += 1
            a[i][j] = s
    for i in a:
        print(*i)


pro(3, 3)
