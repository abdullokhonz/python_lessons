# n = 0
# l: list = []
# l_i: list = []
# while n != 'change':
#     n = input()
#     if n.isnumeric():
#         l.append(int(n))
# l.sort()
# while n != 'close':
#     n = input()
#     for i in range(len(l)):
#         if n.isnumeric():
#             if l[i] == int(n):
#                 l_i.append(i)
# print(*l_i, sep='\n')

# nums = []
# ind = []
# number = input()
# flag = False
# while number != 'close':
#     if number == 'change':
#         flag = True
#     elif not flag:
#         nums.append(int(number))
#     else:
#         ind.append(int(number))
#     number = input()
#
# nums.sort()
# for i in ind:
#     print(nums.index(i))

# ru = "йцукенгшщзхъфывапролджэячсмитьбюё"
# en = "qwertyuiop[]asdfghjkl;'zxcvbnm,.`"
# for i in input():
#     if i in ru:
#         print(en[ru.index(i)], end='')
#     else:
#         print(ru[en.index(i)], end='')

# print(*[en[ru.index(i)] if i in ru else ru[en.index(i)] for i in input()], sep='')

# a = dict(zip(ru, en))
# print(''.join(a[i] for i in input()))

# def group_by_second_word(n, pairs):
#     from collections import defaultdict
#
#     grouped = defaultdict(list)
#
#     for pair in pairs:
#         first, second = pair.split()
#         grouped[second].append(first)
#
#     sorted_keys = sorted(grouped.keys())
#
#     result = []
#
#     for key in sorted_keys:
#         grouped[key].sort()
#         group = [f"{key} {item}" for item in grouped[key]]
#         result.append("\n".join(group))
#
#     output = "\n<->\n".join(result)
#     return output
#
#
# if __name__ == "__main__":
#     n = int(input().strip())
#     pairs = []
#     for _ in range(n):
#         pairs.append(input().strip())
#
#     output = group_by_second_word(n, pairs)
#     print(output)

# count_of_lines: int = int(input('Enter count of lines: '))
# list_of_lines: list = sorted([input('Enter line: ').split()[::-1] for _ in range(count_of_lines)])
# list_of_first_letters: list = sorted(set([i[0][0] for i in list_of_lines]))
# [
#     [print(*j) for j in list_of_lines if letter.lower() == j[0][0].lower()]
#     and (print("< - >") if i < len(list_of_first_letters) - 1 else None)
#     for i, letter in enumerate(list_of_first_letters)
# ]
#
# for i, letter in enumerate(list_of_first_letters):
#     for j in list_of_lines:
#         if letter == j[0][0]:
#             print(*j)
#
#     if i < len(list_of_first_letters) - 1:
#         print('< - >')
