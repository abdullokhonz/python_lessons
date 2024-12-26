def smash(words):
    a = ''
    for i in words:
        a += ' ' + i
    return a.strip()


def smash2(words):
    return ' '.join(i for i in words)


def smash3(words):
    return " ".join(words)


print(smash(["hello", "world"]))
print(smash2(["hello", "world"]))
print(smash3(["hello", "world"]))
