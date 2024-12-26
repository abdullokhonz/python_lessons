# def calc(num1, num2, oper):
#     if oper == '+':
#         return num1 + num2
#     if oper == '-':
#         return num1 - num2
#     if oper == '*':
#         return num1 * num2
#     if oper == '/':
#         if num1 == 0:
#             raise ValueError('ERROR! num1 != 0! ')
#         return num1 / num2
#
#
# print(calc(float(input('Введите первое число: ')), float(input('Введите второе число: ')),
#            input('Выберите оператор +, -, *, / : ')))

import random


# def func(size):
#     list_of_numbers = '12346790'
#     list_of_small_chars = 'qwertyuiopasdfghjklzxcvbnm'
#     list_of_big_chars = list_of_small_chars.upper()
#     list_of_symbols = list(list_of_small_chars + list_of_big_chars + list_of_numbers)
#     res = str(random.sample(list_of_symbols, size))
#     a = '[],\' '
#     for i in a:
#         res = res.replace(i, '')
#     return res
#
#
# print(func(10))
# print(func(10).replace(' ', '').replace('\'', '').replace(',', '').replace('[', '').replace(']', ''))

# def years(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: return True
#     else: return False
#
#
# print(years(int(input('>>>'))))

# def calc2(num1, num2, oper):
#     match oper:
#         case '+':
#             return num1 + num2
#         case '-':
#             return num1 - num2
#         case '*':
#             return num1 * num2
#         case '/':
#             if num1 == 0:
#                 raise ValueError('ERROR! num1 != 0! ')
#             return num1 / num2
#         case _:
#             raise ValueError('ERROR!???')
#
#
# print(calc2(float(input('Введите первое число: ')), float(input('Введите второе число: ')),
#             input('Выберите оператор +, -, *, / : ')))
