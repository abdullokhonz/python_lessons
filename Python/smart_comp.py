import random
a = {}
list1 = [
    'Real Madrid',
    'Barcelona',
    'Manchester City',
    'Bayern',
    'Dortmund',
    'PSG',
    'Atletico Madrid',
    'Arsenal'
]
s = 0
m = 100
for i in list1:
    s = round(random.uniform(1, m), 2) if m > 0 else 1
    a[i] = s
    m -= s
a = dict(reversed(sorted(a.items(), key=lambda item: item[1])))
n = 0
for i in a.keys():
    n += 1
    print(f'{n}. {i}: {a[i]}%')
