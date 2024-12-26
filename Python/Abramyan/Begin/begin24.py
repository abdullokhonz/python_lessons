a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
x = a; a = b; b = c; c = x
print("A = {0}; B = {1}; C = {2};".format(a, b, c))