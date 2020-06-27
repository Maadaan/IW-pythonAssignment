"""
Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
"""

def func(nums):
    return lambda number : number * nums

mul = func(5)
print(mul(7))