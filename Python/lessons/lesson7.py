# a = {'hi', 'abc', 'a', 'hi'}
# b = set('hello')
# b.add(9)
# b.update([1, 2, 4])
# b.remove(9)
# c = b.copy()
# e = {}
# print(a, type(a))
# print(b, type(b))
# print(c)
# print(a & b & c)
# print(a | b | c)
# print(e, type(e))

# a = int(input('a = '))
# b = int(input('b = '))
# print(max(a, b))

# name = input('Your name: ')
# print('Hello', name)

# def say_hi(name):
#     print('hi', name)


# say_hi('Yeeee')

# def calc(a, b):
#     print('Summa:', a + b)
#     print('Vichetaniye:', a - b)
#     print('Umnojheniye:', a * b)
#     print('Deleniye:', a / b)
#
#
# calc(4, 2)

n = int(input('n = '))
m = int(input('m = '))
matrix = []
for i in range(n):
    matrix.append([0] * m)
for i in range(n):
    for j in range(m):
        matrix[i][j] = j * 10
for i in range(n):
    for j in range(m):
        print(matrix[i][j])
