n = int(input('n = '));
while n > 0:
    last = n % 10;
    print(last % 2 != 0);
    n //= 10;