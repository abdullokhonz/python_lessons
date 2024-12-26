lst = []
for i in range(10):
    lst.append(int(input('>>>')))
print(lst)
for i in lst:
    if i < lst[-1]:
        print(i)
        break
else:
    print(0)
