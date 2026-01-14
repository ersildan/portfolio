def greatest_common_divisor(a, b):

    digit = 1
    for el in range(1, max(a, b) + 1):
        if a % el == 0 and b % el == 0:
            digit = el

    return digit

print(greatest_common_divisor(4, 16))
print(greatest_common_divisor(13, 48))
