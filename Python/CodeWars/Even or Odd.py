import random
def even_or_odd(number):
    if number % 2 == 0: return number, 'Even'
    if number % 2 != 0: return number, 'Odd'


print(*even_or_odd(random.randint(0, 100)))
