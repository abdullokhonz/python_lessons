a, b, c, d = list(map(int, input().split()))
if a == b == c or a == b == d or a == c == d or b == c == d:
    x = [a, b, c, d]
    x.sort()
    print(x)
else:
    raise ValueError('Три цыфры должны быть одинаковыми!')
