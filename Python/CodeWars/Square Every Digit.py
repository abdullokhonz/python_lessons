# def square_digits(num):
#     return int(''.join(str(int(d)**2) for d in str(num)))

def square_digits(num):
    num_str = str(num)
    result = ''
    for digit in num_str:
        squared_digit = str(int(digit) ** 2)
        result += squared_digit
    return int(result)


print(square_digits(9119))
print(square_digits(0))
