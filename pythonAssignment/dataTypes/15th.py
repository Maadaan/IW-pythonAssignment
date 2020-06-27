"""
15. Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""

word = 'PHP'

lists = '{{}}'

def func(strings, text):
    mid = len(strings) // 2
    return (strings[:mid] + text + strings[mid:])

print(func(lists , word))