# задание 3.
def thesaurus(*args):
    d = dict()
    for names in args:
        n = names[0]
        if n not in d:
            d[n] = []
        d[n].append(names)
    return d

print(thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Виктория', 'Владимир'))