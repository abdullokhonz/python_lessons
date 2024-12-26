print ("Begin10◦. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.")

a = int (input ("Введите ненулевое число: "))
b = int (input ("Введите второе ненулевое число: "))

a = a ** 2 ; b = b ** 2
summa = a + b
raznost = a - b
proizvedenie = a * b
chastnoe = a / b

print ("Сумма квадратов чисел: " + str(summa))
print ("Разность квадратов чисел: " + str(raznost))
print ("Произведение квадратов чисел: " + str(proizvedenie))
print ("Частное квадратов чисел: " + str(chastnoe))