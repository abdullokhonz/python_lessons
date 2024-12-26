# import random
# a = {}
# list1 = [
#     'Barcelona',
#     'Real Madrid',
#     'Manchester City',
#     'Manchester United',
#     'Dortmund',
#     'Paris Saint Germain',
#     'Atletico Madrid'
# ]
# s = 0
# m = 101
# for i in list1:
#     s = random.randint(0, m)
#     a[i] = s
#     m -= s
# for i in a.items():
#     print(i)

# print(f'Длина вашего имени {len(input('>>>'))}.')
# print("Length of your name:", len(input("Enter your name: ")))

# def colors(c):
#     def print_1():
#         return 'red apple'
#
#     def print_2():
#         return 'white apple'
#
#     def print_3():
#         return 'green apple'
#
#     print(print_1()) if c == 'red' else None
#     print(print_2()) if c == 'white' else None
#     print(print_3()) if c == 'green' else None
#
#
# colors(input('>>>'))

# def calc(num1, num2, oper):
#     def plus():
#         return num1 + num2
#
#     def minus():
#         return num1 - num2
#
#     def multiply():
#         return num1 * num2
#
#     def divide():
#         return num1 / num2
#
#     print(plus()) if oper == '+' else None
#     print(minus()) if oper == '-' else None
#     print(multiply()) if oper == '*' else None
#     print(divide()) if oper == '/' else None
#
#
# calc(int(input('Введите первое число: ')), int(input('введите второе число: ')), input('Выберите операцию: '))

# num = 0
# s = 0
# while s < 100:
#     num = int(input('Введите число: '))
#     s += num
# print(s)

# name, surname = map(str, input('Введите имя и фамилию: ').split())
# a = {name}
# b = {surname}
# print(a, b)

# words = {
#     'Car': 'Машина',
#     'Bird': 'Птица',
#     'Dog': 'Собака',
#     'Cat': 'Кошка',
#     'Cow': 'Корова',
#     'Apple': 'Яблоко',
#     'World': 'Мир',
#     'Book': 'Книга',
#     'Pen': 'Ручка',
#     'Table': 'Стол'
# }

# english = input('>>>')
# for i in words.keys():
#     print(words[i]) if i.lower() == english else None

# for i in range(2, 11):
#     for j in range(1, 11):
#         if i != j:
#             print(i, '*', j, '=', i * j)
