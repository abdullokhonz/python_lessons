n = int(input('n = '))
m = int(input('m = '))
matrix = []
for i in range(n):
    matrix.append([0] * m)
for i in range(n):
    for j in range(m):
        matrix[i][j] = j * 10
for i in matrix:
    print(*i)
