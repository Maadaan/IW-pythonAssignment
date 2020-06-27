"""
Write a program to check if the list is empty or not.
"""

list1 = []
list1 = [0,1,2,3,4,5,6,7,8,9]

def func(list):
    if len(list) == 0:
        return "List is  Empty !!!"
    
    else:
        return "List is not Empty !!!"

print(func(list1))
