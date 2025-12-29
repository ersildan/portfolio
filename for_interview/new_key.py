def format_key(s, k):

    s = s.replace('-', "").upper()[::-1]
    
    total = 1
    l = list()
    lst = list()

    for el in s:
        l.append(el)

        if total < k:
            total += 1
        else:
            total = 1
            lst.append("".join(l))
            l = []  
            
    if l != []:
        lst.append("".join(l))
    
    return  '-'.join(lst)[::-1]

print(format_key("5F3Z-2e-9-w", 4)) # "5F3Z-2E9W"
print(format_key("2-5g-3-J", 2)) # "2-5G-3J"
print(format_key("fgGHHg-gfhG", 3)) # "F-GGH-HGG-FHG"
