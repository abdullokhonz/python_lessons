import random
print('Добро пожаловать в игру!')
randoms = random.randint(int(input('Начальное число: ')), int(input('Последнее число: ')))
p = 0
po = int(input('Попытка: '))
enter = int(input('Введите число: '))
while p <= po - 1:
    p += 1
    if enter == randoms:
        print(f'Вы потратили {p} попыток. Победа!')
        break
    else:
        if enter < randoms:
            print('Мало!')
        if enter > randoms:
            print('Много!')
        print(f'Неыерное число, поыторие попытку. Попыток осталось {po - p}')
        enter = int(input('Введите число: '))
else:
    print('Все попытки исчерпаны. Поражение!')
