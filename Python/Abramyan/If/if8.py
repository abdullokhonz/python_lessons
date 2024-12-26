a = float(input("A = "))
b = float(input("B = "))
if a > b :
    print("A = {0}; B = {1};".format(a, b))
elif a < b :
    print("B = {1}; A = {0};".format(a, b))
else :
    print("A = B :", a, "=", b)