def correct_spacing(str):
    lst = [el for el in str.split() if el != ' ']
    return " ".join(lst)

print(correct_spacing("  Криминальная бабушка   украла       у мафии      бусы. "))
