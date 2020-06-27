"""
Write a Python program to remove the nth
index character from a nonempty string.
"""

string = 'linkein_park'
removingIndex = 4
def func(word,index):
    if len(word) > 0:
        listOfWord = list(word)
        listOfWord.pop(index)
        return ''.join(listOfWord)
    
    else:
        raise AttributeError('String is Empty')

print(func(string,removingIndex))    