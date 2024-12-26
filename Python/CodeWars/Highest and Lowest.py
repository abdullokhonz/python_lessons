def high_and_low(numbers):
    a = list(map(int, numbers.split()))
    a = f'{max(a)} {min(a)}'
    return a


print(high_and_low("1 2 3 4 5"))
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
