# def all_eq(lst):
#     max_str = len(lst[0])
#     for i in lst:
#         if len(i) > max_str:
#             max_str = i
#     s = 0
#     for i in lst:
#         lst[s] += '_' * (max_str - len(i))
#         s += 1
#     return lst


# print(all_eq(['abcbash', 'asd', '2']))

# def sum_range(start, end):
#     return sum(range(start, end + 1)) if start < end else sum(range(end, start + 1))


# print(sum_range(int(input('Enter first number: ')), int(input('Enter second number: '))))

# def three_args(elem1=None, elem2=None, elem3=None):
#     s = 1
#     for i in [elem1, elem2, elem3]:
#         if i is None or i == '':
#             pass
#         else:
#             print(f'var{s} = {i}')
#         s += 1
#
#
# three_args(input('>>>'), input('>>>'), input('>>>'))

# def is_alive(health):
#     if health <= 0:
#         return False
#     else:
#         return True
#
#
# print(is_alive(1))

# def season_events(number_of_month):
#     months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
#     match(number_of_month):
#         case 12 | 1 | 2:
#             return f'Вы родились в {months[number_of_month - 1]}.\nЗа окном падал белый снег.'
#         case 3 | 4 | 5:
#             return f'Вы родились в {months[number_of_month - 1]}.\nПтицы пели прекрасные песни.'
#         case 6 | 7 | 8:
#             return f'Вы родились в {months[number_of_month - 1]}.\nСолнце светило ярче чем когда-либо.'
#         case 9 | 10 | 11:
#             return f'Вы родились в {months[number_of_month - 1]}.\nУрожай был невероятным.'
#         case _:
#             return 'Неизвестный месяц!'


# print(season_events(int(input('Введите номер месяца: '))))

# def check_pass(pswd):
#     err = {
#         'length': 'Длина – 8 символов (если меньше – то проще взломать, а если длиннее – то сложно запомнить)',
#         'capital_letters': 'заглавные буквы',
#         'lowercase_characters': 'строчные символы',
#         'numbers': 'числа',
#         'special_signs': 'специальные знаки (из перечня *-#; другие спецсимволы недопустимы, так как Анатолий их не может запомнить)',
#     }
#     err_length = 0
#     err_capital_letters = 0
#     err_lowercase_characters = 0
#     err_numbers = 0
#     err_special_signs = 0
#     s = 0
#     for i in pswd:
#         err_length += 1
#         if i == i.upper() and not i.isdigit():
#             err_capital_letters += 1
#         if i == i.lower() and not i.isdigit():
#             err_lowercase_characters += 1
#         if i.isdigit():
#             err_numbers += 1
#         if i == '*' or i == '-' or i == '#':
#             err_special_signs += 1
#     if err_length != 8:
#         s += 1
#         print(f'{s}. {err['length']}')
#     if err_capital_letters == 0:
#         s += 1
#         print(f'{s}. {err['capital_letters']}')
#     if err_lowercase_characters == 0:
#         s += 1
#         print(f'{s}. {err['lowercase_characters']}')
#     if err_numbers == 0:
#         s += 1
#         print(f'{s}. {err['numbers']}')
#     if err_special_signs == 0:
#         s += 1
#         print(f'{s}. {err['special_signs']}')
#     return 'Пароль идеален!' if s == 0 else 'Повторите попытку!'
#
#
# print(check_pass(input('Enter password: ')))

# def is_divisible_by_6(number):
#     if int(str(number)[-1]) % 2 == 0 or sum(list(map(int, str(number)))) % 3 == 0:
#         return f'Число {number} делится на 6'
#     return f'Число {number} неделимо на 6'
#
#
# print(is_divisible_by_6(int(input('Enter number: '))))
