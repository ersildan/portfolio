def count_words(text):
    d = dict()
    lst = text.lower().split()
    for el in lst:
        if el not in d:
            d[el] = 1
        else:
            d[el] += 1
    return d

print(count_words("hello world hello"))

# from collections import Counter as c
#
# def count_words(text):
#     return c(text.split())
