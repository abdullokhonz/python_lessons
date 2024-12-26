import random
# print(f'Добро пожаловать в игру!\n1. Камень\n2. Ножница\n3. Бумага')
# victory = int(input('Введите количество раундов, чтобы выиграть: '))
# people_s = 0
# comp_s = 0
# rounds = 0
# while people_s <= victory - 1 and comp_s <= victory - 1:
#     rounds += 1
#     print(f'\n1. Камень\n2. Ножница\n3. Бумага')
#     people = int(input('Введите число (1, 2, 3): '))
#     comp = random.randint(1, 3)
#     if people == comp:
#         if people == 1 and comp == 1:
#             print('Вы > 1. Камень : 1. Камень < Соперник')
#         if people == 2 and comp == 2:
#             print('Вы > 2. Ножница : 2. Ножница < Соперник')
#         if people == 3 and comp == 3:
#             print('Вы > 3. Бумага : 3. Бумага < Соперник')
#         print(f'Ничья! Счёт: {people_s} : {comp_s}.')
#     if people == 1 and comp == 2:
#         people_s += 1
#         print('Вы > 1. Камень : 2. Ножница < Соперник')
#         print(f'Вы победили {rounds} раунд! Счёт: {people_s} : {comp_s}.')
#     if people == 1 and comp == 3:
#         comp_s += 1
#         print('Вы > 1. Камень : 3. Бумага < Соперник')
#         print(f'Вы проиграли {rounds} раунд! Счёт: {people_s} : {comp_s}.')
#     if people == 2 and comp == 3:
#         people_s += 1
#         print('Вы > 2. Ножница : 3. Бумага < Соперник')
#         print(f'Вы победили {rounds} раунд! Счёт: {people_s} : {comp_s}.')
#     if people == 2 and comp == 1:
#         comp_s += 1
#         print('Вы > 2. Ножница : 1. Камень < Соперник')
#         print(f'Вы проиграли {rounds} раунд! Счёт: {people_s} : {comp_s}.')
#     if people == 3 and comp == 1:
#         people_s += 1
#         print('Вы > 3. Бумага : 1. Камень < Соперник')
#         print(f'Вы победили {rounds} раунд! Счёт: {people_s} : {comp_s}.')
#     if people == 3 and comp == 2:
#         comp_s += 1
#         print('Вы > 3. Бумага : 2. Ножница < Соперник')
#         print(f'Вы проиграли {rounds} раунд! Счёт: {people_s} : {comp_s}.')
# else:
#     if people_s > comp_s:
#         print(f'\nИгра закончена, вы победили со счётом {people_s} : {comp_s}!')
#     if people_s < comp_s:
#         print(f'\nИгра закончена, вы проиграли со счётом {people_s} : {comp_s}!')

print(f'Добро пожаловать в игру!\n1. Камень\n2. Ножница\n3. Бумага')
victory = int(input('Введите количество раундов, чтобы выиграть: '))
people_s = 0
comp_s = 0
rounds = 0
game_objects: list = ['1. Камень', '2. Ножницы', '3. Бумага']
while people_s <= victory - 1 and comp_s <= victory - 1:
    rounds += 1
    print(f'\n1. Камень\n2. Ножница\n3. Бумага')
    people = int(input('Введите число (1, 2, 3): '))
    comp = random.randint(1, 3)
    if people == comp:
        print(f'Вы > {game_objects[people - 1]} : {game_objects[comp - 1]} < Соперник')
        print(f'Ничья! Счёт: {people_s} : {comp_s}.')
    elif (people == 1 and comp == 2) or \
            (people == 2 and comp == 3) or \
            (people == 3 and comp == 1):
        print(f'Вы > {game_objects[people - 1]} : {game_objects[comp - 1]} < Соперник')
        print(f'Вы победили {rounds} раунд! Счёт: {people_s} : {comp_s}.')
    else:
        print(f'Вы > {game_objects[people - 1]} : {game_objects[comp - 1]} < Соперник')
        print(f'Вы проиграли {rounds} раунд! Счёт: {people_s} : {comp_s}.')
else:
    if people_s > comp_s:
        print(f'\nИгра закончена, вы победили со счётом {people_s} : {comp_s}!')
    elif people_s < comp_s:
        print(f'\nИгра закончена, вы проиграли со счётом {people_s} : {comp_s}!')
    else:
        print(f'\nИгра закончена, ничья со счётом {people_s} : {comp_s}!')
