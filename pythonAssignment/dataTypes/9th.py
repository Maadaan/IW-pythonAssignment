"""
Write a Python program to change a given string to a new string where the
first and last chars have been exchanged.
"""

string = 'deal_madrir'

def func(word):
    return word[-1] + word[1:-1] + word[0]

print(func(string))