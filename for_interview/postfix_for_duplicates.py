def postfix_duplicates(str):
    
    cach = dict()
    lst = list()
    
    for el in str.split():
        
        if el in cach:
            cach[el] = cach.get(el, 0) + 1
            lst.append(f"{el}_{cach[el]}")
        else:
            cach[el] = 0
            lst.append(f'{el}')
      
    return " ".join(lst)
