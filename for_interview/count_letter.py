def max_sequence(word, symbol):

    for i in range(1, len(word)):
        if symbol * i not in word:
            return i-1

    return len(word)

#
# def max_sequence(word, symbol):
#
#     lst = []
#     txt = ''
#
#     for i in range(len(word) - 1):
#         if word[i] == symbol and word[i] == word[i + 1]:
#             txt += symbol
#         else:
#             lst.append(txt)
#             txt = ''
#     lst.append(txt)
#     x = len(max(lst, key=len))
#
#     return [x + 1, 0][x == 0]
#
# print(max_sequence('aaacccbbbbcccccc', 'c'))
