import random

# a = random.random()
# a = random.randint(1, 5)
# a = random.uniform(1, 5)
# a = [i for i in range(random.randint(1, 10))]
# print(a)
# a = [random.randint(1, 10) for i in range(random.randint(1, 10))]

# a = [3, 2, 5, 5, 9, 8, 2, 4, 2, 10]
# random.shuffle(a)
# b = random.sample(a, 2)
# print(a, b, end='\n')
# print(set(a))

# print('Добро пожаловать в игру!')
# randoms = random.randint(int(input('Начальное число: ')), int(input('Последнее число: ')))
# p = 0
# po = int(input('Попытка: '))
# enter = int(input('Введите число: '))
# while p <= po - 1:
#     p += 1
#     if enter == randoms:
#         print(f'Вы потратили {p} попыток. Победа!')
#         break
#     else:
#         if enter < randoms:
#             print('Мало!')
#         if enter > randoms:
#             print('Много!')
#         print(f'Неыерное число, поыторие попытку. Попыток осталось {po - p}')
#         enter = int(input('Введите число: '))
# else:
#     print('Все попытки исчерпаны. Поражение!')

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
#         print(f'Игра закончена, вы победили со счётом {people_s} : {comp_s}!')
#     elif people_s < comp_s:
#         print(f'Игра закончена, вы проиграли со счётом {people_s} : {comp_s}!')
#     else:
#         print(f'Ничья со счётом {people_s} : {comp_s}!')
