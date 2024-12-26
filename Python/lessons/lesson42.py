# left_border = 0
# right_border = 0
# a1, b1 = int(input()), int(input())
# a2, b2 = int(input()), int(input())
# list1 = [a1, b1, a2, b2]
# list1.sort()
# if a1 < a2:
#     left_border = a2
# else:
#     left_border = a1
#
# if b1 < b2:
#     right_border = b1
# else:
#     right_border = b2
#
# if left_border > right_border:
#     print('пустое множество')
# elif left_border == right_border:
#     print(list1[1])
# else:
#     print(list1[1], list1[2])

# w = int(input())
# print('YES' if w != 2 and w % 2 == 0 else 'NO')

# word = input()
# print(f'{word[0]}{len(word[1:-1])}{word[-1]}' if len(word) >= 10 else word)

# count, s = int(input()), 0
# task = [[0] * 3 for i in range(count)]
# for i in range(count):
#     task[i] = list(map(int, input().split()))
# for i in task:
#     s += 1 if i.count(1) >= 2 else 0
# print(s)

# s = 0
# for i in range(int(input())): task = list(map(int, input().split())); s += 1 if task.count(1) > 1 else 0
# print(s)
