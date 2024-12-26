a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
if a < b and a < c :
    print("A = ", a)
if a > b and b < c :
    print("B = ", b)
if a > c and b > c :
    print("C = ", c)