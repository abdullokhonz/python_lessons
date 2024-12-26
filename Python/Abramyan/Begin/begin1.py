# print("Begin1◦. Дана сторона квадрата a. Найти его периметр P = 4·a.")
#
# a = int(input("Введите сторону квадрата: "))
# p = 4 * a
# print("Периметр квадрата: ", p)

def begin1(a):
    print("Периметр квадрата:", a * 4)
    return a * 4


print(begin1(int(input('a = '))))
