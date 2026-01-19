def number_to_words(number):
    d = {
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять',
        '0': 'ноль'
    }

    lst = list()

    for el in str(number):
        if el in d:
            lst.append(d[el])

    return " ".join(lst)

print(number_to_words(987654321))
print(number_to_words(000))