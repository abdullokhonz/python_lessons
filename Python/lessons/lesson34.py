# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
#     def show_info(self):
#         print(self._x, self._y)
#
#
# pt = Point(10, 20)
# print(pt._x, pt._y)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def show_info(self):
#         return self.__x, self.__y

# def get_x(self):
#     return self.__x
#
# def set_x(self, new_x):
#     self.__x = new_x

# @property
# def x(self):
#     return self.__x
#
# @x.setter
# def x(self, new_x):
#     self.__x = new_x
#
# @x.deleter
# def x(self):
#     print(f'Свойство {self.__x} была удалена!')


# pt = Point(10, 20)
# print(pt._x, pt._y)
# pt.__y = 0
# pt.show_info()
# info = pt.show_info()
# print(info)
# print(pt._Point__y, pt.__y)
# pt.set_x(0)
# print(pt.get_x())
# print(pt.x)
# pt.x = 200
# print(pt.x)
# del pt.x

from math import pi

# class Cicrle:
#     def __init__(self, radius):
#         self.r = radius
#         # self.plo = pi * self.r ** 2
#         # self.per = 2 * pi * self.r
#
#     # def perimetr(self):
#     #     self.per = f'Периметр вашего круга {2 * pi * self.r}.'
#     #
#     # def area(self):
#     #     self.plo = f'Площадь вашего круга {pi * self.r ** 2}.'
#
#     def show_info(self):
#         return self.__dict__
#
#
# circle1 = Cicrle(90)
# # circle1.perimetr()
# # circle1.area()
# print(circle1.show_info())
# # print(pi)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(a) // 2):
    # print(a[0] + a[-1])
    # a.pop()
    # a.reverse()
    # a.pop()
    # print(a[i] + a[-(i + 1)])
    print(a[0] + a[-1])
    a = a[1:-1]

# [print(a[i] + a[-(i + 1)]) for i in range(len(a) // 2)]
