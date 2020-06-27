"""
Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

strings = 'restart'
wordToBeReplaced = strings.replace(strings[0],'$')
print(strings[0] + wordToBeReplaced[1:])