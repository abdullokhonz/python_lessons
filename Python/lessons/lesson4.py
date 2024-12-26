# i = 1;
# while i > 0:
#     print('===', i);
#     i += 1;
#     if i == 10:
#         #! break;
#         continue;
#         print('abc');
# print('abc');



# i = 1;
# while i <= 10:
#     print('===', i);
#     i += 1;
#     if i == 10:
#         break;
# else:
#     print('else');



a = [14, 29, 30, 50, 365];
#! Yes;
#! No;
while len(a) > 0:
    last = a.pop();
    if last % 2 != 0:
        print('No');
        break;
else:
    print('Yes');
print(a);