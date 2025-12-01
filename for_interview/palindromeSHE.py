"""
Дана строка, состоящая из больших и маленьких букв латинского алфавита.
Необходимо написать функцию longest_palindrome(s), которая принимает такую строку
единственным параметром, вычисляет длину максимально возможного палиндрома, который
можно составить из букв этой строки, и возвращает его длину. Например, из символов 
строки "abccccdde" можно построить палиндром "ccdadcc", чья длина равняется семи символам. 
То есть результат вызова longest_palindrome("abccccdde") будет 7.
"""

def longest_palindrome(s):
    d = dict()
  
    for el in s:
        if el not in d:
            d[el] = 1
        else:
            d[el] = d[el] + 1
  
    total = 0
    max_digit = 0
  
    for k, v in d.items():
        if v % 2 == 1 and v > max_digit:
            max_digit = v
        elif v % 2 == 0:
            total += v
        
    return total + max_digit
