a = float(input("A = "))
b = float(input("B = "))
if a != b :
    if a > b :
        b = a
        print("A = {0}; B = {1};".format(a, b))
    if a < b :
        a = b
        print("A = {0}; B = {1};".format(a, b))
if a == b :
    a = 0; b = 0
    print("A = {0}; B = {1};".format(a, b))