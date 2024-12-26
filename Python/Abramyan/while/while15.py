d = 1000
p = float(input('p = '))
k = 0
while d <= 1100:
    k += 1
    d += d * p / 100
print('Month:', k, ';', 'Cost:', d)
