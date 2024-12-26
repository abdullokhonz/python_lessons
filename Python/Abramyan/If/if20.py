a, b, c = map(int, input('>>>').split())
ab = abs(b - a)
ac = abs(c - a)
if ab < ac:
    print('Точка B ближе к точке A')
else:
    print('Точка C ближе к точке A')
