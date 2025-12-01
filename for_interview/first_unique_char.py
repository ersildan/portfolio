"""
Напишите функцию get_first_unique_index(str), которая принимает строку и возвращает
индекс первого уникального символа в ней или -1, если такой символ отсутствует.
"""

def get_first_unique_index(str):
    s = str
    for el in s:
        if s.count(el) == 1:
            return s.find(el)
    return -1
