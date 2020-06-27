"""
Write a Python program to count the occurrences of each word in a given
sentence.
"""


sentences = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod,tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor  reprehenderit  voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt  culpa qui officia deserunt mollit anim id est laborum'

def func(words):
    listOfWord = words.split(' ')
    countTheWord = {}
    for word in listOfWord:
        count = 0
        for test_word in listOfWord:
            if test_word == word:
                count = count + 1
        countTheWord[word] = count
    return countTheWord

print(func(sentences))