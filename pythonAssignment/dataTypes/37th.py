"""
Write a Python program to multiply all the items in a dictionary.
"""

dictLists1 = {'a': 1 ,'b': 2 ,'c': 3 , 'd': 4 , 'e' : 5 ,'f' : 6 , 'g' : 7 }

product = 1
for item in dictLists1.values():
    product = item * product

print(product)