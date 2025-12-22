def is_valid_parentheses(s):
    while True:
        if '{}' in s:
            s = s.replace('{}', '')
        elif '[]' in s:
            s = s.replace('[]', '')
        elif '()' in s:
            s = s.replace('()', '')
        else:
            return len(s) == 0


print(is_valid_parentheses("([])]"))
