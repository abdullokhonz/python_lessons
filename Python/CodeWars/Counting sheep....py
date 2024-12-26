def count_sheeps(sheep):
    array1 = sheep
    s = 0
    for i in sheep:
        if i == True:
            s += 1
    return f"There are {s} sheeps in total, not {len(array1)}"


print(count_sheeps([True, True, True, False,
                    True, True, True, True,
                    True, False, True, False,
                    True, False, False, True,
                    True, True, True, True,
                    False, False, True, True]))

# def count_sheeps(arrayOfSheeps):
#   return arrayOfSheeps.count(True)
