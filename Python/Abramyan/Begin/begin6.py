print ("Begin6◦. Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c).")

a = int (input ("Введите длину ребра прямоугольного параллелепипеда: "))
b = int (input ("Введите вторую длину ребра прямоугольного параллелепипеда: "))
c = int (input ("Введите третью длину ребра прямоугольного параллелепипеда: "))
v = a * b * c
s = 2 * (a * b + b * c + a * c)
print ("Объём прямоугольного параллелепипеда: " + str(v))
print ("Площадь поверхности прямоугольного параллелепипеда: " + str(s))