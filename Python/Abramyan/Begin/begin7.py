print ("Begin7◦. Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R ** 2. В качестве значения π использовать 3.14.")

r = int (input ("Введите радиус: "))
p = 3.14
l = 2 * p * r
s = p * r ** 2
print ("Длина окружности: " + str(l))
print ("Площадь круга: " + str(s))