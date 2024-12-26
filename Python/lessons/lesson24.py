# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# [print(i) for i in a if i < 5]

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)

# d = {
#     1: 3,
#     2: 2,
#     3: 10,
#     4: 1,
#     5: 25,
# }
# print(sorted(d.values()))

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print([i for i in b if i in a])
# print(list({i for i in a if i in b}))

# my_dict = {
#     'a': 500,
#     'b': 5874,
#     'c': 560,
#     'd': 400,
#     'e': 5874,
#     'f': 20,
# }
# new_dict = {}
# for i in range(3):
#     maximum = 'a'
#     for j in my_dict:
#         if my_dict[maximum] < my_dict[j]:
#             maximum = j
#     new_dict[maximum] = my_dict[maximum]
#     print(maximum, my_dict[maximum])
#     del my_dict[maximum]
# print(new_dict)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print(a[0], a[-1])

# n = int(input('>>>'))
# print(n + int(str(n) * 2) + int(str(n) * 3))
# print(n + (n * 11) + (n * 111))

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print([i for i in b if i not in a])

# a = int(input('>>>'))
# s = 0
# bool1 = bool
# for i in list(str(a)):
#     s = str(a).count(i)
#     if s != 1:
#         bool1 = False
#         break
#     else:
#         bool1 = True
# print(bool1)
# print(len(str(a)) == len(set(str(a))))

# a = input('>>>').split('.')
# print(a[1] if len(a) == 2 else None)

n = int(input('>>>'))
k = 1
while n >= k ** 2:
    k += 1
print(k)
