"""
Write a Python program to remove a key from a dictionary.
"""


dictLists1 = {'a': 1 ,'b': 2 ,'c': 3 , 'd': 4 , 'e' : 5 ,'f' : 6 , 'g' : 7 }

def func(dictItem , key):
    dictItem.pop(key)

func(dictLists1, 'd')
print(dictLists1)