def invert(lst):
    lst2 = []
    for i in list(lst):
        if i >= 0:
            lst2.append(-i)
        if i < 0:
            lst2.append(i * -1)
    return lst2


print(invert([1, -1, 0, 34823, -23482394]))
