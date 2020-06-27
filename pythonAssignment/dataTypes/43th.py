"""
Write a Python program to remove an item from a tuple.
"""

lists = ['Python','is', 'a','programming','language','!!!']

tmp = list(lists)

tmp.pop()

tuples = tuple(tmp)
print(tuples)