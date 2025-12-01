"""
Необходимо реализовать функцию rle_encode, принимающую в аргументах строку,
состоящую из букв, и возвращающую новую строку, в которой повторяющиеся буквы 
заменены количеством повторений.
"""

def rle_encode(message):
    lst = []
    count = 1

    for i in range(1, len(message)):
        if message[i] == message[i - 1]:
            count += 1
        else:
            lst.append(f"{message[i - 1]}{count}")
            count = 1

    lst.append(f"{message[-1]}{count}")
    
    return "".join(lst)
