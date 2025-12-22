def longest_unique_subsequence(lst):

    start = 0
    total = 0
    end = len(lst)

    new_lst = list()
    lst_ = list()

    while start != end:
        for i in range(start, end):
            if lst[i] not in lst_:
                lst_.append(lst[i])
                start += 1
            else:
                new_lst.append(lst_)
                total += 1
                start = total
                lst_ = list()
                break
        else:
            new_lst.append(lst_)
            lst_ = []
            total += 1
            start = total

    return max(new_lst, key=len)

print(longest_unique_subsequence([1, 2, 3, 1, 2, 3, 4, 5]))


# def longest_unique_subsequence(lst):
#     if not lst:
#         return []
# 
#     start = 0
#     last_seen = {}
#     max_len = 0
#     best_start = 0
# 
#     for i, num in enumerate(lst):
#         # Если число уже встречалось и его последний индекс >= start,
#         # значит оно в текущем окне, двигаем start
#         if num in last_seen and last_seen[num] >= start:
#             start = last_seen[num] + 1
# 
#         last_seen[num] = i
# 
#         # Проверяем, не стала ли текущая последовательность самой длинной
#         current_len = i - start + 1
#         if current_len > max_len:
#             max_len = current_len
#             best_start = start
# 
#     return lst[best_start:best_start + max_len]