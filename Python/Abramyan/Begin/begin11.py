print ("Begin11◦. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.")

from math import fabs

a = int (input ("Введите ненулевое число: "))
b = int (input ("Введите второе ненулевое число: "))

a = fabs(a) ; b = fabs(b)
summa = a + b
raznost = a - b
proizvedenie = a * b
chastnoe = a / b

print ("Сумма модуля чисел: " + str(summa))
print ("Разность модуля чисел: " + str(raznost))
print ("Произведение модуля чисел: " + str(proizvedenie))
print ("Частное модуля чисел: " + str(chastnoe))