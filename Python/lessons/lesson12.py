# a = (1, 2, 3, 1.2, True, 'abc', [10, 20, 30])
# print(a.count(2))
# print(a.index(1))

# b = [10, 7, 20, 1]
# mins = b[0]
# for i in b:
#     if i < mins:
#         mins = i
# print(mins)

# def mini(b):
#     mins = b[0]
#     for i in b:
#         if i < mins:
#             mins = i
#     return mins
#
#
# print(mini([10, 5, 1]))

# def maxi(b):
#     maxs = b[0]
#     for i in b:
#         if i > maxs:
#             maxs = i
#     return maxs
#
#
# print(maxi([10, 5, 1]))

# def minmax(a):
#     mins = a[0]
#     maxs = a[0]
#     for i in range(len(a)):
#         if a[i] < mins:
#             mins = i
#         if a[i] > maxs:
#             maxs = i
#     return mins, maxs
#
#
# print(minmax([5, 10, 1]))

# def minmax(a):
#     b = []
#     for i in range(len(a) - 1, -1, -1):
#         b.append(a[i])
#     return a, b
#
#
# print(minmax([1, 2, 3]))

# list = [10, 7, 20, 3, 100, -1, 69, -20, 0]
# minimum_value = list[0]
# maximum_value = list[0]
# minimum_index = 0
# maximum_index = 0
# for i in range(len(list)):
#     if list[i] < minimum_value:
#         minimum_value = list[i]
#         minimum_index = i
#     if list[i] > maximum_value:
#         maximum_value = list[i]
#         maximum_index = i
# print(minimum_value, minimum_index)
# print(maximum_value, maximum_index)
