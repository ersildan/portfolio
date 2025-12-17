def roman_to_integer(s):
    for el in d:
        s = s.replace(el, f"{d[el]},")
    for el in d_:
        s = s.replace(el, f"{d_[el]},")
    s = s[:-1]
    return sum(map(int, s.split(',')))

d = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
    }
d_ = {
    'I': 1, 'V': 5,
    'X': 10,'L': 50,
    'C': 100, 'D': 500,
    'M': 1000
}
