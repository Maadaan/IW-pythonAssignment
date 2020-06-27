"""
Write a Python function to create the HTML string with tags around the
word(s).
"""


sentence = 'This code is written in Python language.'
tags = 'p'

def func(tag, content):
    return f"<{tag}> {content} </{tag}>"

print(func(tags,sentence))


