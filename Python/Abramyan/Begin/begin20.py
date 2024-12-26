import math
x1 = float(input("X1 = "))
y1 = float(input("Y1 = "))
x2 = float(input("X2 = "))
y2 = float(input("Y2 = "))
result = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print("Расстояние: ", result)