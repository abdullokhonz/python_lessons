from os import system

while True:
    try:
        time = int(input('Time: '))

        if time < 0:
            print('ОШИБКА!')
        else:
            if time == 0:
                system('shutdown -a')
                print('Автоотключение отменено!')
                break
            else:
                system(f'shutdown /s /t {time}')
                print(f'Ваш комьпютер отключится через {time} минут!')
                break
    except ValueError:
        print('Введите число!')
