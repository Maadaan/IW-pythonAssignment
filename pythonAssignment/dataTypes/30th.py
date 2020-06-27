"""
Write a Python script to check whether a given key already exists in a
dictionary.
"""

dictLists = {'a': 1 ,'b': 2 ,'c': 3 , 'd': 4 , 'e' : 5 ,'f' : 6 , 'g' : 7 }

def func(lst,key):
    keyList = lst.keys()

    if list(keyList).__contains__(key):
        return True
    else:
        return False

print(func(dictLists , 'b'))

print(func(dictLists , 'm'))
