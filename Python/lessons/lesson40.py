# text = input().split()
# new_text = []
# res_text = ''
# for i in text:
#     for j in i:
#         if j in '.,"!?@-=)*+/%1234567890':
#             i = i.replace(j, '')
#     new_text.append(i)
# len_word = [len(i) for i in new_text]
# for i in range(0, len(text)):
#     for j in text[i]:
#         if 65 <= ord(j) + len_word[i] <= 90 or 97 <= ord(j) + len_word[i] <= 122:
#             if j not in ' .,"!?@-=)*+/%1234567890':
#                 res_text += chr(ord(j) + len_word[i])
#             else:
#                 res_text += j
#         else:
#             if j not in ' .,"!?@-=)*+/%1234567890':
#                 res_text += chr(ord(j) + len_word[i] - 26)
#             else:
#                 res_text += j
#     res_text += ' '
# print(res_text.strip())

# a = input()
# s = a
# for _ in s:
#     if _ in '*,.!@"-':
#         s = s.replace(_, '')
# x = [len(i) for i in s.split()]
# count = 0
# word = ''
# for i in a:
#     number = ord(i)
#     if i == ' ':
#         count += 1
#         word += i
#     elif 65 <= number <= 90:
#         if number + x[count] > 90:
#             word += chr(number + x[count] - 26)
#         else:
#             word += chr(number + x[count])
#     elif 97 <= number <= 122:
#         if number + x[count] > 122:
#             word += chr(number + x[count] - 26)
#         else:
#             word += chr(number + x[count])
#     else:
#         word += i
# print(word)

# num = int(input())
# print(bin(num)[2:])
# print(oct(num)[2:])
# print(hex(num)[2:].upper())

# print(*[input() for i in range(3)][::-1], sep="\n")

# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')

# print('БЕСКОНЕЧНОСТЬ', 'НЕ', 'ПРЕДЕЛ', '!', sep='_')
#
# print('БЕСКОНЕЧНОСТЬ_НЕ_ПРЕДЕЛ!')
#
# print('БЕСКОНЕЧНОСТЬ', 'НЕ', 'ПРЕДЕЛ!', sep='_', end='!')
#
# print('БЕСКОНЕЧНОСТЬ', 'НЕ', 'ПРЕДЕЛ', sep='_', end='')
# print('!')
#
# print('БЕСКОНЕЧНОСТЬ_НЕ_ПРЕДЕЛ', end='')
# print('!')
#
# print('БЕСКОНЕЧНОСТЬ_', 'НЕ_', 'ПРЕДЕЛ!', sep='', end='')

# num = int(input())
# [print(i) for i in range(num, num + 3)]

# comp1 = sum([int(input()) for _ in range(4)])
# comp2 = sum([int(input()) for _ in range(4)])
# comp3 = sum([int(input()) for _ in range(4)])
# print(comp1 + comp2 + comp3)
# print(comp1, comp2, comp3)

# comp1 = int(input()) + int(input()) + int(input()) + int(input())
# comp2 = int(input()) + int(input()) + int(input()) + int(input())
# comp3 = int(input()) + int(input()) + int(input()) + int(input())
# print(comp1 + comp2 + comp3)

# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)

# a = 82 // 3 ** 2 % 7
# print(a)
