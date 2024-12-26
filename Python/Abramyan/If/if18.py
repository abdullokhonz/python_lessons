a, b, c = list(map(int, input().split()))
if a == b or a == c or b == c:
    x = [a, b, c]
    x.sort()
    print(x)
else:
    raise ValueError('Две цыфры должны быть одинаковыми!')
