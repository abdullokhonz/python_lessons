# class Dog:
#     name = 'Bobik'
#     age = 1
#
#     # @staticmethod
#     # def bark():
#     #     print('Собaка полаяла!')
#
#     def change_name(self, new_name):
#         self.name = new_name


# dog1 = Dog()
# dog2 = Dog()
# Dog.age = 2
# dog2.name = 'Reks'
# print(dog1.name, dog2.name)
# dog1.change_name('Reks')
# dog2.change_name('Tuzik')
# print(dog2.name)

# class Cat:
#     name = None
#     age = None
#
#     def change_info(self, new_name, new_age):
#         self.name = new_name
#         self.age = new_age
#
#     def miao(self):
#         print(f'Кошка {self.name} говорит МЯУ!')
#
#     def show_info(self):
#         print(f'Имя кошки: {self.name},\nВозраст кошки: {self.age}.')
#
#
# cat1 = Cat()
# cat1.change_info('Markis', 2)
# cat1.miao()
# cat1.show_info()

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         # try:
#         #     self.none
#         # except AttributeError:
#         #     return None
#         return f'Имя пса {self.name}, возраст {self.age}'
#
#
# dog1 = Dog('Reks', 200)
# dog2 = Dog('Tuzik', 8)
# print(dog1.info())
# print(dog2.info())

class Soda:
    def __init__(self, add=None):
        self.add = add.strip() if isinstance(add, str) else None

    def show_my_drink(self):
        return f'Газировка и {self.add}' if self.add else 'Обычная газировка!'


soda1 = Soda('Сахар')
print(soda1.show_my_drink())
