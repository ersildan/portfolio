def increasing_sequence(l):
    start = 0
    total = 0
    end = len(l)

    new_lst = list()
    lst_ = list()

    while start != end:
        for i in range(start, end):
            if l[i] not in lst_ and all(l[i]> el for el in lst_):
                lst_.append(l[i])
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
