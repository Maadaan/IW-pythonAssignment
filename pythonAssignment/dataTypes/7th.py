"""
Write a Python function that takes a list of words and returns the length of
the longest one.
"""

lists = ['python','computer','realmadrid','football' ,'linkinpark']

def func(longestList):
   
    count = 0
    for word in longestList:
        if len(word) > count:
            count = len(word)
    return count

print(func(lists))