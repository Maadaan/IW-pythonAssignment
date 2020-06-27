"""
32. Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

dictSize = 5

def func(size):
    result = {}
    for item in range(1 , size + 1):
        result[item] = item * item
    return result

print(func(dictSize))


