"""
Write a Python function to find the Max of three numbers.
"""

def func(a , b , c):
	
	if a > b and a > c:
		return 'A is the greatest !!!'
	
	elif b > a and b >c:
		return 'B is the greatest !!!'

	else:
		return 'C is the greatest !!!'

print(func(1,2,3))

