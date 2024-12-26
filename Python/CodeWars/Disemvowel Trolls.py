def disemvowel(string_):
    vowel = 'aoeiuAOEIU'
    for i in vowel:
        string_ = string_.replace(i, '')
    return string_


def disemvowel2(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


print(disemvowel("This website is for losers LOL!"))
print(disemvowel2("This website is for losers LOL!"))
