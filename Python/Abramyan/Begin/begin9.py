print ("Begin9◦. Даны два неотрицательных числа a и b. Найти их среднее геометрическое, то есть квадратный корень из их произведения: √a·b.")

from math import sqrt

a = int (input ("Введите неотрицательное число: "))
b = int (input ("Введите второе неотрицательное число: "))
result = sqrt(a * b)
print ("Результат: " + str(result))