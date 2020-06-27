"""
Write a Python program to filter a list of integers using Lambda.
"""

lists = [2,3,4,5,7,9,10,16,25,36,50,53,74,100,108]

items = list(filter(lambda x:x % 3 != 0 , lists))
print(items)