file = open('hee.txt', 'r+', encoding='UTF-8')
k = int(input('>>>'))
for i in range(file.read().count('\n')):
    if i == k:
        file = open('hee.txt', 'a', encoding='UTF-8')
        file.seek(i)
        file.write('\n')
        break
