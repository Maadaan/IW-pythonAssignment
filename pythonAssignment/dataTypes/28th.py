"""
Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""

givenDict = {0: 10, 1: 20}

def func(oldValues , keys , values):
    oldValues[keys] = values
    return oldValues

print(func(givenDict, 2 , 30))

