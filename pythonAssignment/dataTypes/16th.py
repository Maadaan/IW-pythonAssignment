"""
Write a Python program to sum all the items in a list.
"""


items = [34,67,89,354,15,7,78]

def func(lists):
   
    sum = 0
    for list in lists:
        sum = sum + list
    return sum

print(func(items))