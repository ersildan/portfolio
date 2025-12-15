# def merge_with_sum(a, b):
#     d = dict()
#     mn_d = min(a, b, key=len)
#     mx_d = max(a, b, key=len)
# 
#     for k, v in mx_d.items():
# 
#         d[k] = mx_d.get(k, 0) + mn_d.get(k, 0)
# 
#     for k, v in mn_d.items():
#         if k not in d:
#             d[k] = v
#     return d


def merge_with_sum(a, b):
    d = a
    for k, v in b.items():
        d[k] = d.get(k, 0) + v
    return d


print(merge_with_sum({'яблоки':11,'груши':62}, 
                     {'апельсины':52,'груши':31,'абрикосы':16}))
