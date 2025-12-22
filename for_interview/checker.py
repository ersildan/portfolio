def checker(str):
    while True:
        if '{}' in str:
            str = str.replace('{}', '')
        elif '[]' in str:
            str = str.replace('[]', '')
        elif '()' in str:
            str = str.replace('()', '')
        else:
            return len(str) == 0
        