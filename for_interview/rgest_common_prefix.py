"""
Нужно написать функцию longest_common_prefix(strs), которая вернет самый большой общий префикс
для массива строк, переданного в качестве аргумента.В случае, если у переданных слов нет общего 
префикса, функция должна вернуть пустую строку.
"""

def longest_common_prefix(strs):
    a, b, c = strs
    
    lst = []
    for x, y, z in zip(a, b, c):
        if x == y == z:
            lst.append(x)
        else:
            break
    
    return "".join(lst)