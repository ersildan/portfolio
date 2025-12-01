'''
Напишите функцию chunked(l, size), которая принимает на вход список l и число size, 
задающее размер чанка и возвращает список из чанков указанной длины.
'''

def chunked(l, size):
    lst, lst_ = [], []

  for el in l:
        lst_.append(el)
      if len(lst_) == size:
          lst.append(lst_)
          lst_ = []
  else:
      if len(lst_) > 0:
          lst.append(lst_)
        
  return lst
