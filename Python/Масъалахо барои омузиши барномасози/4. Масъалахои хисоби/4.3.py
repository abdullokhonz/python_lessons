import math
x = 2; y = 5
a = (x + y / (x ** 2 + 4)) / ((math.exp(- x - 2) + 1 / (x ** 2 + 4)) * (1 + y))
print(a)