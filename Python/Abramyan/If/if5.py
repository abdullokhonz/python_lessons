a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
x = 0; y = 0
if a > 0:
    x += 1
elif a < 0:
    y += 1
if b > 0:
    x += 1
elif b < 0:
    y += 1
if c > 0:
    x += 1
elif c < 0:
    y += 1
print("X = {0}; Y = {1}".format(x, y))