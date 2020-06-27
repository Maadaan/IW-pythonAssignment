"""
Write a Python program to multiply all the items in a list.
"""

values = [3,6,8,9,4,7]

def func(nums):
    product = 1
    for num in nums:
        product = num * product
    return product

print(func(values))
