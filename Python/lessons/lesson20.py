# def firts_func(a):
#     s = 0
#     for _ in a:
#         s += 1
#     return s
#
#
# print(firts_func([2, 4, 1, 3, 5, 6, 7, 9]))

# a = 'python'
# print(a[2:4:11])

# a = 'алфавит'
# s = 0
# p = 0
# for i in a:
#     if i == 'а':
#         p += 1
#     s += 1
# res = s / 100 * p
# print(s, p, res)
# t = input('>>>')
# b = list(a)
# s = 0
# for i in range(len(a)):
#     if a[i] == t:
#         s += 1
# print(s)

# def count_(text):
#     s = 0
#     for _ in text:
#         s += 1
#     return s
#
#
# print(count_('abdullokhon'))

# def odd(list_):
#     s = 0
#     for i in list_:
#         if i % 2 != 0:
#             s += i
#     return s
#
#
# print(odd([1, 2, 3, 4, 5]))

# a = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0],
# ]
# c, d = map(int, input('>>>'))
# a[c - 1][d - 1] = input('>>>')
# for i in a:
#     print(i)

# a = int(input('>>>'))
# s = 0
# while a > 0:
#     s += a
#     a = int(input('>>>'))
# print(s)

# def yes_or_no(num):
#     if num % 2 != 0:
#         return 'Yes'
#     elif num % 2 == 0:
#         if 2 <= num <= 5:
#             return 'No'
#         elif 6 <= num <= 20:
#             return 'Yes'
#         elif num > 20:
#             return 'No'
#     return None
#
#
# print((yes_or_no(int(input('>>>')))))

# def roman_numerals(num):
#     match num:
#         case 1:
#             return 'I'
#         case 2:
#             return 'II'
#         case 3:
#             return 'III'
#         case 4:
#             return 'IV'
#         case 5:
#             return 'V'
#         case 6:
#             return 'VI'
#         case 7:
#             return 'VII'
#         case 8:
#             return 'VIII'
#         case 9:
#             return 'XI'
#         case 10:
#             return 'X'
#         case _:
#             return None
#
#
# print(roman_numerals(int(input('>>>'))))
