# class Animal:
#     def __init__(self, name: str, age: int, paroda: str):
#         self.name, self.age, self.paroda = name, age, paroda
#
#     def show_info(self):
#         print(f'Имя: {self.name}\nВозраст: {self.age}\nПарода: {self.paroda}')
#
#
# class Cat(Animal):
#     def voice(self):
#         print(f'{self.name} говорит гав!')
#
#
# class Dog(Animal):
#     def voice(self):
#         print(f'{self.name} говорит мяу!')
#
#
# c1 = Cat('Барсик', 3, 'Египетская')
# c1.voice()
# c1.show_info()
#
# d1 = Dog('Шарик', 5, "Хаски")
# d1.voice()
# d1.show_info()

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def display(self):
        pass


class Circle(Shape):
    def __init__(self, color, radius):
        self.color, self.radius = color, radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def display(self):
        _ = 'круг'
        return f'Цвет {_}а: {self.color}\nПлощадь {_}а: {self.area()}\nПериметр {_}а: {self.perimeter()}'


class Rectangle(Shape):
    def __init__(self, color, width, height):
        self.color, self.width, self.height = color, width, height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width + self.height

    def display(self):
        _ = 'прямоугольник'
        return f'Цвет {_}а: {self.color}\nПлощадь {_}а: {self.area()}\nПериметр {_}а: {self.perimeter()}'


c1 = Circle('Red', 90)
print(c1.display())
print()
r1 = Rectangle('Yellow', 200, 200)
print(r1.display())

# class Vehicle(ABC):
#     @staticmethod
#     def start():
#         return "Транспортное средство заведено!"
#
#     @staticmethod
#     def stop():
#         return "Транспортное средство заглушено!"
#
#     @abstractmethod
#     def show_info(self):
#         pass
#
#
# class Car(Vehicle):
#     def __init__(self, color, brand, model):
#         self.color, self.brand, self.model = color, brand, model
#
#     @staticmethod
#     def drive():
#         return 'Автомобиль едет!'
#
#     def show_info(self):
#         _ = "автомобил"
#         return f'Цвет {_}a: {self.color}\nБредн {_}a: {self.brand}\nМодель {_}a: {self.model}'
#
#
# class Bike(Vehicle):
#     def __init__(self, typee, brand, model):
#         self.typee, self.brand, self.model = typee, brand, model
#
#     @staticmethod
#     def ride():
#         return 'Велосипед едет!'
#
#     def show_info(self):
#         _ = "велосипед"
#         return f'Тип {_}a: {self.typee}\nБредн {_}a: {self.brand}\nМодель {_}a: {self.model}'
#
#
# c1 = Car('Red', 'BMW', 'M4')
# b1 = Bike('Racing', 'Opel', 'Astra G')
# print(c1.start())
# print(c1.stop())
# print(c1.drive())
# print(c1.show_info())
#
# print()
#
# print(b1.start())
# print(b1.stop())
# print(b1.ride())
# print(b1.show_info())
