# def is_isogram(string):
#     for i in string:
#         if string.count(i) == 1:
#             return True
#         else:
#             return False

def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True


print(is_isogram(input('>>>')))
