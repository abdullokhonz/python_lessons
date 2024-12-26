def check_pass(pswd):
    err = {
        'length': 'Длина – 8 символов (если меньше – то проще взломать, а если длиннее – то сложно запомнить)',
        'capital_letters': 'заглавные буквы',
        'lowercase_characters': 'строчные символы',
        'numbers': 'числа',
        'special_signs': 'специальные знаки (из перечня *-#; другие спецсимволы недопустимы, так как Анатолий их не может запомнить)',
    }
    err_length = 0
    err_capital_letters = 0
    err_lowercase_characters = 0
    err_numbers = 0
    err_special_signs = 0
    s = 0
    for i in pswd:
        err_length += 1
        if i == i.upper() and not i.isdigit():
            err_capital_letters += 1
        if i == i.lower() and not i.isdigit():
            err_lowercase_characters += 1
        if i.isdigit():
            err_numbers += 1
        if i == '*' or i == '-' or i == '#':
            err_special_signs += 1
    if err_length != 8:
        s += 1
        print(f'{s}. {err['length']}')
    if err_capital_letters == 0:
        s += 1
        print(f'{s}. {err['capital_letters']}')
    if err_lowercase_characters == 0:
        s += 1
        print(f'{s}. {err['lowercase_characters']}')
    if err_numbers == 0:
        s += 1
        print(f'{s}. {err['numbers']}')
    if err_special_signs == 0:
        s += 1
        print(f'{s}. {err['special_signs']}')
    return 'Пароль идеален!' if s == 0 else 'Повторите попытку!'


print(check_pass(input('Enter password: ')))
