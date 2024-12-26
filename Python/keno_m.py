# from random import sample
#
#
# class Keno:
#     # Свойства класса
#     __MIN_BET = 0.5
#     __MAX_BET = 5
#     __money = 100
#     __list_of_nums = [i for i in range(1, 81)]
#     __count_of_guess = 10
#
#     # Метод для ввода ставки
#     def __to_bet(self) -> float:
#
#         # Проверка на валидность
#         while True:
#             bet = input(f'Делайте ставку!(мин: {self.__MIN_BET}, макс: {self.__MAX_BET}) -> ')
#             if not bet.replace('.', '').isnumeric():
#                 print("Введённые данные не являются числом! Повторите попытку")
#             elif float(bet) < self.__MIN_BET:
#                 print(f"Введённое число не должно быть меньше {self.__MIN_BET}")
#             elif float(bet) > self.__MAX_BET:
#                 print(f"Введённое число не должно быть больше {self.__MAX_BET}")
#             else:
#                 break
#         self.__money -= float(bet)
#         return float(bet)
#
#     @classmethod
#     # Метод для генерации рандомных чисел
#     def __get_random_nums(cls) -> list[int]:
#         list_of_random_nums = sample(cls.__list_of_nums, 20)
#         return list_of_random_nums
#
#     # Метод для ввода чисел
#     def __entering_nums(self) -> list[int]:
#         # Список введённых чисел
#         entered_nums = []
#         for i in range(self.__count_of_guess):
#             # Проверка на валидность
#             while True:
#                 elem = input('Введите ваше число(от 1 до 80 включительно) -> ')
#                 if not elem.isnumeric():
#                     print("Введённые данные не являются числом! Повторите попытку")
#                 elif int(elem) < 1:
#                     print("Введённое число не должно быть меньше 1")
#                 elif int(elem) > 80:
#                     print("Введённое число не должно быть больше 80")
#                 elif int(elem) in entered_nums:
#                     print("Введённое число уже содержится в списке")
#                 else:
#                     break
#             entered_nums.append(int(elem))
#             print(f'Текущие введённые числа: {entered_nums}')
#         return entered_nums
#
#     @staticmethod
#     # Метод для поиска совпадений
#     def __matching_choices(random_nums: list, guessed_nums: list) -> list[int]:
#         matches = list(set(random_nums) & set(guessed_nums))
#         return matches
#
#     @staticmethod
#     # Метод для определения вознаграждения
#     def __award(bet, matches) -> int:
#         # Количество совпадений
#         amount_of_matches = len(matches)
#         match amount_of_matches:
#             case 5:
#                 return bet
#             case 6:
#                 return bet * 24
#             case 7:
#                 return bet * 142
#             case 8:
#                 return bet * 1000
#             case 9:
#                 return bet * 4500
#             case 10:
#                 return bet * 10000
#             case _:
#                 return 0
#
#     @property
#     # Функция для просмотра баланса
#     def money(self):
#         return self.__money
#
#     # Процесс игры
#     def start_game(self):
#         print('Welcome to game')
#
#         # Ставка
#         bet = self.__to_bet()
#         print(f'Ваша ставка: {bet}')
#
#         # Введённые числа
#         entered_nums = self.__entering_nums()
#         print(f'Введённые числа: {entered_nums}')
#
#         # Рандомные числа
#         nums = self.__get_random_nums()
#         print(f'Все рандомные числа: {nums}')
#
#         # Совпадения
#         matched = self.__matching_choices(nums, entered_nums)
#         print(f'Угаданные числа: {matched}')
#
#         # Выигрыш
#         win = self.__award(bet, matched)
#         self.__money += win
#         print(f'Ваш выигрыш состовляет: {win}')
#         print(f'Ваш текущий баланс: {self.__money}')


# if __name__ == '__main__':
#
#     kn = Keno()
#     kn.start_game()
#     while True:
#         if kn.money < 0:
#             print('Недостаточно денег')
#             break
#         answer = input('Хотите продолжить игру?(Y/N) -> ').upper()
#         if answer == 'N':
#             break
#         elif answer == 'Y':
#             kn.start_game()
#         else:
#             print('Неизвестная комманда. Повторите попытку')
