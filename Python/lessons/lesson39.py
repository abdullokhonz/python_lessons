# print(max([len(i) for i in input('>>>').split()]))

# from math import sqrt
#
# a, b = int(input('>>>')), int(input('>>>'))
# print(f'Сумма: {a + b}')
# print(f'Разность: {a - b}')
# print(f'Произведение: {a * b}')
# print(f'Частное: {a / b}')
# print(f'Целая часть от деления: {a // b}')
# print(f'Остаток от деления: {a % b}')
# print(f'корень квадратный из суммы их 1010-х степеней: {sqrt(a ** 10 + b ** 10)}')

# weight, height = float(input()), float(input())
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print('Недостаточная масса')
# elif bmi > 25:
#     print('Избыточная масса')
# else:
#     print('Оптимальная масса')

# text = len(input())
# print(f'{(text * 60) // 100} р. {(text * 60) % 100} коп.')

# print(len(list(input().split())))

# year, animals = int(input()), ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса',
#                                'Бык', 'Тигр', 'Заяц']
# print(animals[year % 10])

# print(['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца'][
#           int(input()) % 12])

# num = input()
# print(int(num[::-1])) if len(num) == 5 else print(int(num[0] + num[1:][::-1]))

# num = input()[::-1]
# res, s, comma = '', 0, len(num) // 3
# for i in num:
#     if comma != 0:
#         if s == 3:
#             s = 0
#             res += ','
#             comma -= 1
#     s += 1
#     res += i
# print(res[::-1])


