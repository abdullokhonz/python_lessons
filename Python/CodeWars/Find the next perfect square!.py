from math import sqrt


def find_next_square(sq):
    if sqrt(sq).is_integer():
        return (sqrt(sq) + 1) ** 2
    else:
        return -1


print(find_next_square(121))

# import math
#
#
# def find_next_square(sq):
#     return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1
