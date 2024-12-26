n = int(input('n = '))
k = 0
s = 0
while s <= n:
    k += 1
    s += k
print(k)
print(s)

while n >= sum(range(1, k)):
    k += 1
print(k - 1, sum(range(1, k)))
