N = int(input('N = '));

if N%2 == 0:
    L = 2
else:
    L = 1

F = 1

while N >= L:
    F *= N
    N -= 2

print("Двойной факториал: ", F)