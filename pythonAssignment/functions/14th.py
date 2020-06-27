"""
14. Write a Python program to sort a list of dictionaries using Lambda.
"""

lists = [
    {'name':'ram', 'age':25},
    {'name':'shyam', 'age':16},
    {'name':'hari', 'age':22}
]

lists.sort(key=lambda x:x['age'])
print(lists)