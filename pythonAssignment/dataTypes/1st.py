"""
Write a Python program to count the number of characters (character
frequency) in a string. Sample String : google.com'

Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""



strings = 'google.com'

countTheWord = {}

for char in strings:
	count = 0
	
	for characters in strings:
		if char == characters:
			count = count + 1
	
	countTheWord[char] = count

print(countTheWord)