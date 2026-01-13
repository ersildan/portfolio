def less_comm_multiple(a, b):

    digit = 1
    while digit % a != 0 or digit % b != 0:
        digit += 1

    return digit

print(less_comm_multiple(5, 7))
