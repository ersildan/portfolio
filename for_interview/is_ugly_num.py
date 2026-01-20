def is_ugly(num):

    for i in (2, 3, 5):

        while num % i == 0:
            num = num // i

    return num == 1

print(is_ugly(6)) # True, 6 = 2 * 3
print(is_ugly(14)) # False, 14 = 2 * 7
print(is_ugly(1)) # True, число 1 также считается уродливым
