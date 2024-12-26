# try:
#     file = open('name', 'r', encoding='UTF-8')
#     print(True)
# except FileNotFoundError:
#     print(False)

# try:
#     a = int(input('>>>'))
#     b = int(input('>>>'))
#     print(a / b)
#     print(True)
# except:
#     print(False)

# try:
#     a = int(input('>>>'))
#     b = int(input('>>>'))
#     print(a / b)
#     print(True)
# except ZeroDivisionError:
#     print(False)
# except ArithmeticError:
#     print(False)

# n = 0
# k = 0
# while n < 2:
#     n += 1
#     print(n)
#     while k < 3:
#         k += 1
#         print('\t', k)
#     k = 0

# a = int(input('>>>'))
# print(isinstance(a, int))

# a = [1, 2, 3, 4, 9]
# b = [5, 6, 7, 8]
# print(list(zip(a, b)))

# s = 0
# k = 1
# for i in range(1, 11):
#     s += i * k
#     k *= -1
#     print(s)

# a = input('>>>')
# print(list(enumerate(a)))

# print(open('text.txt', 'r+', encoding='UTF-8').read().count('\n') + 1)
# print(len(open('text.txt', 'r+', encoding='UTF-8').readlines()))

# file = open('text.txt', 'r', encoding='UTF-8')
# s = 0
# for i in file.read():
#     s += 1
# print(s)

# print(len([i for i in file.read()]))
# print(len(file.read()))

# open('text.txt', 'w', encoding='UTF-8').write(input('>>>'))
# file = open('text.txt', 'w', encoding='utf-8')
# print(file.write('2'))
