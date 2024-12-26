def proc(a):
    b = a ** 3
    c = a ** 4
    d = a ** 5
    return b, c, d


print(*proc(2))
