from random import randint


class Keno:
    __key: str = ''
    __age: int = 0
    __bid: float = 0.0
    __validity_of_the_bet: bool = False
    __user_numbers: list = []
    __validity_of_the_user_numbers: bool = False
    __random_numbers: list = []
    __number_of_coincidences: int = 0
    __winning_amount: float = 0.0
    __balance: float = 100.0
    __transactions: list = [f'Баланс увеличился на {__balance}$ - Ваш баланс: {__balance}$']

    def age_verification(self):
        print('Это игра азартная, чтобы играть в неё укажите свой возраст!')
        try:
            self.__age = int(input('Введите свой возраст: '))
        except ValueError:
            print('Введите число!')
        if self.__age < 18:
            print('Вход несовершеннолетним запрешён!\nИди в школу.')
        else:
            def second_verification():
                print('Ты совершеннолетний?')
                self.__key = input('[Y - Да / N - Нет]: ')
                match self.__key.upper():
                    case 'Y':
                        print('Заходи!\n')
                    case 'N':
                        print('Уходи!')
                    case _:
                        second_verification()

            second_verification()

    @staticmethod
    def welcome():
        print(f'Добро пожаловать в игру Кено!\n')

    @staticmethod
    def rules_of_the_game():
        print('Правила игры:')
        print('1. Выбор чисел: Игрок выбирает от 1 до 10 чисел из 80 возможных.')
        print('2. Случайный выбор: Компьютер случайным образом выбирает 20 чисел из 80.')
        print('3. Сравнение:  Выигрышные числа игрока — это те, которые совпадают с числами, выбранными компьютером.')
        print('4. Выигрыш: Выигрыш зависит от количества совпадений и от суммы ставки. Чем больше совпадений, тем '
              'больше выигрыш.\n')

    def checking_the_validity_of_the_bet(self):
        if 0 < self.__bid < self.__balance:
            self.__validity_of_the_bet = True
            self.__balance -= self.__bid
            self.__transactions.append(f'Баланс уменьшился на {self.__bid}$ - Ваш баланс: {self.__balance}$')
            print('Ваша ставка принята!\n')
        else:
            self.__validity_of_the_bet = False
            print('Ваша ставка не принята!\n')

    def get_a_bet(self):
        while not self.__validity_of_the_bet:
            print(f'Ваш баланс: {self.__balance}')
            try:
                self.__bid = float(input('Сделайте ставку: '))
            except ValueError:
                print('Введите число!')
            self.checking_the_validity_of_the_bet()

    def winning_table(self):
        print(f'Ваш баланс: {self.__balance}\nВаша ставка: {self.__bid}\n| Количество совпадений | Выигрыш |')
        for i in range(10):
            print(f'| {i + 1} | {self.__bid * (i + 1)} |')

    def checking_the_validity_of_the_user__numbers(self):
        __check_number: int = 0
        try:
            __check_number = (int(input('Введите число от 1 до 80: ')))
        except ValueError:
            print('Введите число!')
        if 0 < __check_number <= 80:
            self.__user_numbers.append(__check_number)
        else:
            print('Ошибка. Повторите попытку!')

        if len(self.__user_numbers) == 10:
            self.__validity_of_the_user_numbers = True
            print('Ваши числа приняты!\n')
        else:
            self.__validity_of_the_user_numbers = False

    def get_user_numbers(self):
        while not self.__validity_of_the_user_numbers:
            print(f'\nВыбранные числа: {self.__user_numbers}')
            self.checking_the_validity_of_the_user__numbers()

    def get_random_numbers(self):
        self.__random_numbers = [randint(1, 80) for _ in range(10)]

    def comparison(self):
        print(f'Выбранные числа: {self.__user_numbers}')
        print(f'Рандомные числа: {self.__random_numbers}')
        for i in range(len(self.__user_numbers)):
            for j in range(len(self.__random_numbers)):
                if self.__user_numbers[i] == self.__random_numbers[j]:
                    self.__number_of_coincidences += 1
                else:
                    continue
        print(f'Ваша ставка: {self.__bid}\nКоличество совпадений: {self.__number_of_coincidences}')
        self.__winning_amount = self.__bid * self.__number_of_coincidences
        print(f'Ваш выигрыш: {self.__winning_amount}')
        if self.__winning_amount > 0:
            self.__balance += self.__winning_amount
            self.__transactions.append(f'Баланс увеличился на {self.__winning_amount}$ - Ваш баланс: {self.__balance}$')
        else:
            pass
        print(f'Ваш баланс: {self.__balance}\n\nИгры закончена!')

    def transaction(self):
        print('\nТранзакции:', *self.__transactions, sep='\n\t')

    def start_the_game(self):
        self.age_verification()
        if self.__age >= 18 and self.__key.upper() == 'Y':
            self.welcome()
            self.rules_of_the_game()
            self.get_a_bet()
            self.winning_table()
            self.get_user_numbers()
            self.get_random_numbers()
            self.comparison()
            self.transaction()
            self.clear()
            self.restart()
        else:
            pass

    def restart(self):
        self.__key = ''
        print('\nХотите играть снова?')
        self.__key = input('[Y - Да / N - Нет]: ')
        match self.__key.upper():
            case 'Y':
                print('\nПродолжаем!\n')
                self.start_the_game()
            case 'N':
                print('\nПока, всего хорошего!')
            case _:
                self.restart()

    def clear(self):
        self.__key: str = ''
        self.__age: int = 0
        self.__bid: float = 0.0
        self.__validity_of_the_bet: bool = False
        self.__user_numbers: list = []
        self.__validity_of_the_user_numbers: bool = False
        self.__random_numbers: list = []
        self.__number_of_coincidences: int = 0
        self.__winning_amount: float = 0.0


cat = Keno()
cat.start_the_game()
