f_file = open('hee.txt', 'a')
t_file = open('wee.txt', 'r+')
f_file.write('\n' + t_file.read())
