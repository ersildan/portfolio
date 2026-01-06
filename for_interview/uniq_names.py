def unique_usernames(names):
    lst = []
    d = dict()

    for el in names:
        if ' ' in el:
            x = el.replace(' ', '_')
        else:
            x = el

        if x not in lst:
            lst.append(x)
            d[x] = 0
        else:
            d[x] += 1
            lst.append(f"{ x }_{ str(d[x]) }")

    return lst
