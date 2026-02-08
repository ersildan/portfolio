def greatest_common_divisor(numbers):

    if len(numbers) == 1:
        return numbers[0]

    lst = []
    mn_value = min(numbers)

    for i in range(1, mn_value + 1):

        if all(el % i == 0 for el in numbers):
            lst.append(i)

    return max(lst)


print(greatest_common_divisor([9, 6, 27, 12])) # 3
print(greatest_common_divisor([5, 10, 15])) # 5
print(greatest_common_divisor([10])) # 10
print(greatest_common_divisor([7, 11])) # 1