a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
if a < b < c:
    a *= 2; b *= 2; c *= 2
    print("A = {0}; B = {1}; C = {2};".format(a, b, c))
else:
    a =  -a; b = -b; c = -c
    print("A = {0}; B = {1}; C = {2};".format(a, b, c))