"""
Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.


Sample String : 'Python'
Expected Result : 'Pyon'
Sample String : 'Py'
Expected Result : 'PyPy'
Sample String : ' w'
Expected Result : Empty String

"""

strings = 'Python'
strings = 'Py'
strings = 'w'

def func(word):
    if len(word) >= 2:
        return word[:2] + word[-2:]
    else:
        return 'Empty String'

resultWord = func(strings)
print(resultWord)