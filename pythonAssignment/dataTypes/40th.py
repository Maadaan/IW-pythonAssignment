"""
Write a Python program to add an item in a tuple.
"""

tuples = (1,2,3,4,5,6,7)

tmp = list(tuples)
tmp.append(8)

result = tuple(tmp)
print(result)