def proc(x, y):
    amean = (x + y) / 2
    gmean = (x * y) ** 0.5
    return amean, gmean


print(proc(2, 3))
