new_file = open(input('>>>') + '.txt', 'w')
alphabet = 'abcdefjhijklmnopqrstuvwxyz'.upper()
n = int(input('>>>'))
for i in range(n):
    for j in range(i):
        new_file.write(alphabet[j])
    new_file.write(alphabet[i] + '*' * (n - i - 1) + '\n')
