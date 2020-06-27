"""
Write a Python program to insert a given string at the beginning of all
items in a list.
Sample list : [1,2,3,4], string : emp
"""

strings = ['a','b','c','d','e','f','g','h']

def func(list,string):
    
    for index in range(len(list)):
        list[index] = string + str(list[index])
    return list
print(func(strings,'first '))