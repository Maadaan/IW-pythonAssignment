"""
Write a Python function to check whether a 
number is in a given range.
"""

def func(start , end , num):
    for i in range(start , end):
        if i == num :
            return True
    return False

print(func(1,20,2))

print(func(20,1,2))