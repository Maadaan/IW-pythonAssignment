"""
Write a Python program to check whether a given string is number or not
using Lambda.
"""

list2 = '14'
list3 = 'python'

nums = lambda str : str.isnumeric()

print(nums(list2))
print(nums(list3))


