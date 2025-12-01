"""
Реализуйте функцию is_all_unique(lst), которая принимает список lst 
и возвращает True, если все элементы в списке уникальны, и False в противном случае.
"""
def is_all_unique(lst):
    return len(set(lst)) == len(lst)

