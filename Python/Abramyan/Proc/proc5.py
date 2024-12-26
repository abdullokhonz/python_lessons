def proc(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    p = (a + b) * 2
    s = a * b
    return p, s


print(proc(2, 3, 4, 5))
