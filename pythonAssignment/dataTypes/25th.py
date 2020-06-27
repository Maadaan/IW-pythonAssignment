"""
Write a Python program to check whether all dictionaries in a list are empty or
not.

Sample list : [{},{},{}]
Return value : True

Sample list : [{1,2},{},{}]
Return value : False

"""


# dictList = [{1,2},{},{}]

# dictList = [{},{},{}]

dictList = [{1:2},{},{}]

def func(list):
    isListEmpty = True
    for item in list:
        if len(item.items()) != 0:
            isListEmpty = False
            break
    return isListEmpty

print(func(dictList))