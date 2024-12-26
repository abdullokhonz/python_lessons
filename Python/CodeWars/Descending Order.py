# def descending_order(num):
#     list1 = []
#     for i in str(num):
#         list1.append(i)
#     list1.sort()
#     list1.reverse()
#     result = ''
#     for i in list1:
#         result += i
#     result = int(result)
#     a = print(result)
#     return a


def descending_order(num):
    num = str(num)
    num = num[::-1]
    num = int(num)
    return num


descending_order(1234567890)
