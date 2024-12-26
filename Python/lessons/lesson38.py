# class Parent:
#     __name = 'Vasya'
#     __age = 20
#
#     def info(self):
#         print(f'Name - {self.__name}; age - {self.__age}')
#
#
# class Child(Parent):
#     def func(self):
#         print(self.__age, self.__name)
#
#
# c = Child()
# c.info()


# class Shape:
#     def __init__(self, a):
#         self.a = a
#
#
# class Square(Shape):
#     pass
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.a, self.b = a, b
#
#
# s = Rectangle(2, 4)
# print(s.a, s.b)

class Emloyee:
    def __init__(self, name, salary):
        self.name, self.salary = name, salary

    @staticmethod
    def work():
        print('Сотрудник работает.')


class Manager(Emloyee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    @staticmethod
    def manage():
        print('Мененджер управляет отделом.')


class Salesperson(Emloyee):
    def __init__(self, name, salary, products):
        super().__init__(name, salary)
        self.products = products

    @staticmethod
    def sell():
        print('Продавец продает продукты.')


# m = Manager('Nastya', 0.50, 'School')
# s = Salesperson('Andrey', 0.25, ['apple', 'banana', 'cherry'])
# m.work()
# m.manage()
# s.work()
# s.sell()

# class Keno:
#     balance = 100
