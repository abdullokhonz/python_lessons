a = float(input("A = "))
b = float(input("B = "))
if a > b :
    x = a; a = b; b = x
    print("A = {0}; B = {1};".format(a, b))
elif a < b :
    print("A = {0}; B = {1};".format(a, b))
else :
    print("A = B :", a, "=", b)