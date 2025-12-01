"""
Необходимо написать функцию reverse_vowels(s), 
которая меняет порядок гласных букв в строке на обратный.
"""

def reverse_vowels(s):
    check = 'уеёыаоэяиюУЕЁЫАОЭЯИЮeuioaEUIOA'
    s_list = list(s)

    start = 0
    end = len(s) - 1

    while start < end:
        while start < end and s_list[start] not in check:
            start += 1
        while start < end and s_list[end] not in check:
            end -= 1

        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1

    return "".join(s_list)
