"""
Write a Python program to find the index of an item of a tuple.
"""

lists = ['Python','is', 'a','programming','language','!!!']

def func(lists, value):
    return lists.index(value)

print(func(lists,'a'))