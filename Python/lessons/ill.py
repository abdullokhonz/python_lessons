# dict = {'apple': 'red', 'banana': 'yellow', 'limon': 'yellow'}
# print(dict)
# dict['banana'] = 'green'
# print(dict)

# class A():
#     def __init__(self, N_Nasab, N_kitob, R_kitob):
#         self.N_Nasab = N_Nasab
#         self.N_kitob = N_kitob
#         self.R_kitob = R_kitob
#
#     def ucheniki(self):
#         # print("Uchenik" + self.N_Nasab + "vzyal knigu" + self.N_kitob + "pod nomerom" + self.R_kitob)
#         print("Uchenik", self.N_Nasab, "vzyal knigu", self.N_kitob, "pod nomerom", self.R_kitob)
#
#
# A1 = A("Aliev_Ali", "Alifbo", 2526)
# A2 = A("Valiev_Vali", "Matematika", 2527)
#
# A1.ucheniki()
# A2.ucheniki()

# import re
# s = 'AN\ANOM\ANOM\ANOM\OM'
# result = re.match('A', s)
# print(result)

# def get_days(month):
#     months = [
#         ['January', 31],
#         ['February', 28],
#         ['March', 31],
#         ['April', 30],
#         ['May', 31],
#         ['June', 30],
#         ['July', 31],
#         ['August', 31],
#         ['September', 30],
#         ['October', 31],
#         ['November', 30],
#         ['December', 31]
#     ]
#     for i in range(len(months)):
#         if i == month:
#             print(*months[i])
#
#
# get_days(int(input('Month: ')) - 1)

def get_factors(num):
    nums = []
    for i in range(1, num + 1):
        if num % i == 0:
            nums.append(i)
    return nums


print((get_factors(int(input('Enter the number: ')))))
