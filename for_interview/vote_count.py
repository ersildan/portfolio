"""
Реализуйте функцию get_vowels_count(str), принимающую единственным 
параметром строку, и возвращающую количество гласных букв в этой строке.
Строка всегда содержит кириллицу.
"""

def get_vowels_count(str):
    txt = 'уеыаоэяию'
    count = 0
    for l in str:
        if l.lower() in txt:
            count += 1
    return count
