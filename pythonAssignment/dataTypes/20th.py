"""
Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

words = ['abc', 'xyz', 'aba', '1221']

def func(word):
    count = 0
    for item in word:
        if item[0] == item[-1] and len(item) >= 2:
            count = count + 1
    return count

print(func(words))
