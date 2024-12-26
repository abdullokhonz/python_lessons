def find_needle(haystack):
    array = 0
    for i in haystack:
        if i == 'needle':
            return f'found the needle at position {array}'
        array += 1


print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
