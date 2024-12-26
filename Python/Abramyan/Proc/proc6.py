def proc(k):
    c = 0
    s = 0
    while k > 0:
        s += k % 10
        k //= 10
        c += 1
    return c, s


print(proc(123))
