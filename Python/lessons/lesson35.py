# text1, text2, s = input('>>>'), input('>>>'), 0
# for i in range(len(text1 if text1 <= text2 else text2)):
#     if text1[i] == text2[i]:
#         s += 1
# print(s)

# from random import randint
#
# file = open('text.txt', 'w')
#
#
# def func(x):
#     s = 0
#     s += 1
#     if s <= x:
#         func(x - 1)
#         file.write(str(x) + '\n')
#
#
# func(randint(1, 10))

# class BankAccount:
#     __balance = 0
#     __interest_rate = 10
#     __transactions = []
#
#     @property
#     def balance(self):
#         return f'Ваш баланс: {self.__balance}.'
#
#     def deposit(self, amount):
#         self.__balance += amount
#         self.__transactions.append(f'Счёт увеличился на {amount}.')
#
#     def withdraw(self, amount):
#         self.__balance -= amount
#         self.__transactions.append(f'Счёт уменьшился на {amount}.')
#
#     def add_interest(self):
#         add_interest = (self.__balance / 100) * self.__interest_rate
#         self.__balance += add_interest
#         self.__transactions.append(f'Годовая ставка пополнилась на {add_interest}.')
#
#     def history(self):
#         print(*self.__transactions, sep='\n')
#
#
# cat = BankAccount()
# # cat.deposit(1000)
# # cat.deposit(1000)
# # cat.withdraw(500)
# # cat.add_interest()
# # cat.history()
# # print(cat.balance)
#
# cat.deposit(100)
# cat.withdraw(50)
# cat.add_interest()
# cat.history()
# print(cat.balance)

# def scrabble(word):
#     one_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
#     two_point = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
#     three_point = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
#     four_point = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
#     five_point = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
#     eight_point = ['J', 'X', 'Ш', 'Э', 'Ю']
#     ten_point = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
#     point = 0
#     for i in word.upper():
#         if i in one_point:
#             point += 1
#         elif i in two_point:
#             point += 2
#         elif i in three_point:
#             point += 3
#         elif i in four_point:
#             point += 4
#         elif i in five_point:
#             point += 5
#         elif i in eight_point:
#             point += 8
#         elif i in ten_point:
#             point += 10
#         else:
#             continue
#     return word, point
#
#
# print(*scrabble(input('>>>')), sep='\n')

# rich = [input('>>>') for i in range(4)]
# print('Вы прошли!' if rich.count('#') == 4 else 'Вы умерли!')

# print('Вы прошли!' if [input('>>>') for i in range(4)].count('#') == 4 else 'Вы умерли!')
