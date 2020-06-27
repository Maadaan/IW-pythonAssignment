"""
Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.
Sample String : 'The quick Brown Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""



sentence = 'The quick Brown Fox'

def func(string):
    tmp = list(string)
    upperCaseCount = 0
    lowerCaseCount = 0

    for item in tmp:
        if item.isupper():
            upperCaseCount = upperCaseCount + 1
        else:
            lowerCaseCount = lowerCaseCount + 1

    return upperCaseCount , lowerCaseCount


upperCount , lowerCount = func(sentence)

print(f'upperCount : {upperCount} ,lowerCount: {lowerCount} ')