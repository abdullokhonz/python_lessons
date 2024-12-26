# class Person:
#     name = 'Ivan'
#     age = 30
#     x = 0
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#     @classmethod
#     def change_age(cls):
#         cls.age = 20


# chel1 = Person()
# chel2 = Person()
# chel1.name = 'Firdavs'
# chel1.age = 25
# print(Person.__dict__)
# print(chel1.__dict__)
# print(chel2.__dict__)
# Person.y = 'hello'
# print(chel2.y)
# del Person.x
# print(Person.__dict__)
# chel1.y = 3
# print(Person.__dict__)
# print(chel1.__dict__)
# print(chel2.__dict__)
# chel1.set_name('Firdavs')

# class Cat:
#     name = None
#     age = None
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#     def set_age(self, new_age):
#         self.age = new_age
#
#
# cat1 = Cat()
# cat1.set_name('Lorry')
# cat1.set_age(2)
#
# cat2 = Cat()
# cat2.set_name('Markis')
# cat2.set_age(1)
#
# print(cat1.__dict__)
# print(cat2.__dict__)
