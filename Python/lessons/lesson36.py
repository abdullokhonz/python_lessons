# class Person:
#     def __init__(self, fullName, age):
#         self.fullName = fullName
#         self.age = age
#
#     def move(self):
#         return f'Такой-то {self.fullName} говорит!'
#
#     def talk(self):
#         return f'Такой-то {self.fullName} двигается!'
#
#
# chel1 = Person('Miky', 16)
# print(chel1.move())
# print(chel1.talk())

# class Calculate:
#     def __init__(self, num1, num2):
#         self.num1, self.num2 = num1, num2
#
#     def add(self):
#         return self.num1 + self.num2
#
#     def subtract(self):
#         return self.num1 - self.num2
#
#     def multiply(self):
#         return self.num1 * self.num2
#
#     def divide(self):
#         try:
#             return self.num1 / self.num2
#         except ZeroDivisionError:
#             return 'ERROR!!!'
#
#
# calc = Calculate(2, 0)
# print(calc.add())
# print(calc.subtract())
# print(calc.multiply())
# print(calc.divide())

# class Book:
#     def __init__(self, title, author, pages):
#         self.title, self.author, self.pages = title, author, pages
#
#     def read(self):
#         print(f'Читаю книгу {self.title}, {self.author}, {self.pages}.')
#
#
# dog = Book('How to catch a kitten?', 'Mr.Dogger', 1)
# dog.read()
# cat = Book('How to catch a dog?', 'Mr.Catter', 1)
# cat.read()


# class Car:
#     def __init__(self, brand: str, model: str, color: str):
#         self.brand, self.model, self.color = brand, model, color
#
#     def start(self):
#         print(f"Машина {self.brand}, {self.model}, {self.color} заведена.")
#
#     def stop(self):
#         print(f"Машина {self.brand}, {self.model}, {self.color} заглушена.")
#
#     def drive(self):
#         print(f"Машина {self.brand}, {self.model}, {self.color} едет.")
#
#
# car1 = Car('Audi', 'CLS63', 'Black')
# car1.start()
# car1.drive()
# car1.stop()

# class Person:
#     def __init__(self, name: str, age: int):
#         self.name, self.age = name, age
#
#     def introduce(self):
#         print(f"Меня зовут {self.name}, мне {self.age} лет.")
#
#
# chel1 = Person('Azam', -15)
# chel1.introduce()

# class Animal:
#     def __init__(self, name: str, type: str):
#         self.name, self.type = name, type
#
#     def speak(self):
#         print(f"Животное {self.name}({self.type}) издает звуки.")
#
#     def eat(self):
#         print(f"Животное {self.name}({self.type}) ест.")
#
#
# cat = Animal('Markis', 'Cat')
# cat.speak()
# cat.eat()

class Phone:
    def __init__(self, number=None, model=None, weight=None):
        self._number = number
        self._model = model
        self._weight = weight

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @staticmethod
    def receiveCall(name, caller_number=None):
        if caller_number:
            print(f"Звонит {name} с номера {caller_number}")
        else:
            print(f"Звонит {name}")

    def getNumber(self):
        return self._number

    @staticmethod
    def sendMessage(*numbers):
        print("Сообщение будет отправлено на номера:", ", ".join(numbers))


phone1 = Phone("123-456-7890", "ModelX", 150)
phone2 = Phone("987-654-3210", "ModelY", 200)
phone3 = Phone()

print(f"Phone 1 - Number: {phone1.number}, Model: {phone1.model}, Weight: {phone1.weight}")
print(f"Phone 2 - Number: {phone2.number}, Model: {phone2.model}, Weight: {phone2.weight}")

phone1.receiveCall("Алексей")
print(f"Номер телефона 1: {phone1.getNumber()}")

phone2.receiveCall("Мария")
print(f"Номер телефона 2: {phone2.getNumber()}")

phone1.receiveCall("Дмитрий", "111-222-3333")

phone1.sendMessage("123-456-7890", "234-567-8901", "345-678-9012")
