new_file = open(input('>>>') + '.txt', 'w')
n, k = map(int, input('>>>').split())
[new_file.write('*' * k + '\n') for _ in range(n)]
