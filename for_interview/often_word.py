"""
Напишите функцию frequent_word(string), которая принимает на вход строку string
и определяет самое часто встречающееся слово в ней. В случае наличия нескольких таких слов,
функция должна вернуть слово, которое идет первым в лексикографическом порядке.
"""

def frequent_word(string):
    # Напишите код здесь

    lst = string.lower().split()
    d = dict()
    for k in set(lst):
        d[k] = lst.count(k)

    return sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0]
