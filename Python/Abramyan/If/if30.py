# def registrationPage():
#     print('Hello, please enter your name!')
#     name = input('Your name: ')
#     print(name, 'please enter your surname!')
#     surname = input('Your surname: ')
#     print(name, surname, ', plaese enter your age!')
#     age = int(input('Your age: '))
#     print('Successfull registration, You:', name, surname, age)
#
#
# registrationPage()

a = int(input('a: '))

if 1 <= a < 10:
    if a % 2 == 0:
        print('Чётное однозначное!')
    else:
        print('Нечётное однозначное!')
elif 10 <= a < 100:
    if a % 2 == 0:
        print('Чётное двухзначное!')
    else:
        print('Нечётное двухзначное!')
elif 100 <= a < 1000:
    if a % 2 == 0:
        print('Чётное трёхзначное!')
    else:
        print('Нечётное трёхзначное!')
else:
    print('Диапазон не подходит!')
