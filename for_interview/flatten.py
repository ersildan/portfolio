def flatten(array):
    array = str(array)\
            .replace('[', '')\
            .replace(']', '')\
            .replace(' ', '')\
            .replace("'", '')
    
    lst = array.split(',')

    return [int(el) if el.isdigit() == True else el for el in lst]

print(flatten(['a', ['b', ['c', ['d', ['e']]]]]))

# def flatten(array):
#     result = []

#     for i in array:
#         if isinstance(i,list):
#             result.extend(flatten(i))
#         else:
#             result.append(i)

#     return result

