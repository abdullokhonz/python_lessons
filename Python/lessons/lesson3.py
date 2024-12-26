
#! break
#! continue
#! pass
#! last



#! 0 1 2 3 4 5 || 6 7 8
# n = 0;
# while n < 6:
#     print(n);
#     n += 1;

# n = int(input());
# print(n//10, n%10)



n = int(input());
k = 0;
c = 0;
nc = 0;
m = 0;
mi = 9;
while n > 0:
    k += 1;
    last = n % 10;
    if last > m:
        m = last;
    if last < mi:
        mi = last;
    if last % 2 == 0:
        c += 1;
    else:
        nc += 1;
    print(last);
    n //= 10;
print('k = ', k);
print('c = ', c);
print('nc = ', nc);
print('m = ', m);
print('mi = ', mi);