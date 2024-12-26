def quizz(a, b):
    c = ''
    while b != c:
        print(a)
        c = input('>>>').lower().replace(' ', '')
        if b != c:
            print(False)
    return True


print(quizz('HTML', 'hypertextmarkuplanguage'))
print(quizz('CSS', 'cascadingstylesheets'))
print(quizz('JS', 'javascript'))
