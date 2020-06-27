"""
Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

string1 = 'abc'
string2 = 'string'

def func(self,words):

    if words[-3:] == 'ing':
        return words + 'ly'
        
    elif words[-3:] == 'ly':
        return words + 'ing'
    
    else:
        return words

print(func(string1,string2))

