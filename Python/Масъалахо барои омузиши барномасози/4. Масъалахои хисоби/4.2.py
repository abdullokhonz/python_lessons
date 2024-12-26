import math
x = 2; y = 5; z = 7
a = (3 + math.e ** (y - 1)) / (1 + x ** 2 * math.fabs(y - math.tan(z)))
b = 1 + math.fabs(y - x) + (((y - x) ** 3) / 2 + (math.fabs(y - x) ** 3) / 3)
print(a)
print(b)