"""
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""


strings1 = 'abc'
strings2 = 'xyz'

def func(word1,word2):
    return f"{word2[:2] + word1[2:]}  {word1[:2] + word2[2:]}" 
    
print(func(strings1,strings2))