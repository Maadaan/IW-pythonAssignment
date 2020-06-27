"""
Write a Python program to find if a given string starts with a given
character using Lambda.
"""

word = 'python'

string = lambda char : True if char == word[0] else False

print(string('p'))

print(string('P'))