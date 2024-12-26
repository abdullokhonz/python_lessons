def series_sum(n):
    a = 0
    taq = 1
    s = 1.0
    while a <= n:
        s /= taq
        taq += 3
        a += 1
    return s


print(series_sum(2))
