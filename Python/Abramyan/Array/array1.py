def n_first_oddNumbers(n):
    num = 0
    odd = []
    while num != n + n:
        if num % 2 != 0:
            odd.append(num)
        num += 1
    return odd


print(n_first_oddNumbers(int(input('>>>'))))
print([i for i in range(0, int(input('>>>')) * 2) if i % 2 != 0])
print([i for i in range(1, int(input('>>>')) * 2, 2)])
