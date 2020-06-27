"""
13. Write a Python program to sort a list of tuples using Lambda.
"""

lists = [('e',5),('c',3),('b',2),('g',7),('d',4),('a',1),('f',6) ]
lists.sort(key=lambda x : x[1])
print(lists)