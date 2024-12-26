n = int(input());
while n > 0:
    last = n % 10;
    print(last, end = '');
    n //= 10;