new_file = open(input('>>>') + '.txt', 'w')
alphabet = 'abcdefjhijklmnopqrstuvwxyz'
n = int(input('>>>'))
while n < 27:
    for i in range(n):
        new_file.write(alphabet[i])
    new_file.write('\n')
    n += 1
