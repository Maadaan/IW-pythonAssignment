"""
Write a Python program to find the first appearance of the substring 'not'
and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor'
substring with 'good'. Return the resulting string.

Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""


sentence = 'The lyrics is not that poor!'

def func(word):
    indexNot = word.find('not')
    indexPoor = word.find('poor')
    if indexNot > 0 < indexPoor > 0 :
        return word.replace(word[indexNot : indexPoor + 4], 'good')
    
    else:
        return word

print(func(sentence))

