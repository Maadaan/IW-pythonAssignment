"""
Write a Python script to merge two Python dictionaries.
"""

dictLists1 = {'a': 1 ,'b': 2 ,'c': 3 , 'd': 4 , 'e' : 5 ,'f' : 6 , 'g' : 7 }
dictLists2 = {1:10 , 2: 20 , 3:30 ,4:40 , 5:50 , 6:60 , 7:70 , 8:80 , 9:90 }

dictMerge = {}

dictMerge.update(dictLists1)
dictMerge.update(dictLists2)

print(dictMerge)