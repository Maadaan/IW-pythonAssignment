"""
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""

lists = [8, 2, 3, -1, 7]

def func(item):
    product = 1
    for num in item:
        product = product * num
    return product

print(func(lists))