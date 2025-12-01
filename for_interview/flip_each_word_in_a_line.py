"""
Напишите функцию words_reverser(str), переворачивающую каждое слово
в строке, не меняя при этом порядок слов.
"""

def words_reverser(str):
   
    lst = str.split()
    lst_= [el[::-1] for el in lst]
    
    return " ".join(lst_)
