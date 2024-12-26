# file = open('text.txt', 'r+', encoding='UTF-8')
# text = file.read()
# text = file.readline()
# print(text)
# text = file.readline()
# print(text)
# text = file.readline()
# print(text)
# print(file.readlines())

# file.seek(3)
# text = file.readline()
# print(text)

# text = file.readlines()
# for i in file.read():
#     print(i)

# file.write(input('>>>'))

# print(*sorted(map(int, file.read())))
# print(file.read().count('.'))

# try:
#     print(len(open('text.txt', 'r+', encoding='UTF-8').read()))
# except FileNotFoundError:
#     print('No File')

# s = 0
# for i in file.read():
#     if i.isdigit():
#         s += 1
# print(s)

# text = file.read()
# file = open('text.txt', 'w', encoding='UTF-8')
# file.write(text[::-1])


# def isValildBrackets(s):
#     brackets = {'(': ')', '[': ']'}
#     stack = []
#     for char in s:
#         if char in brackets:
#             stack.append(char)
#         else:
#             if not stack or brackets[stack.pop()] != char:
#                 return False
#     return not stack
#
#
# print(isValildBrackets("([])()[]"))
# print(isValildBrackets("(]("))
# print(isValildBrackets(")("))
# print(isValildBrackets(""))
