"""
Write a Python program to get the largest number from a list.
"""

values = [0 , 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95 , 85, 75, 65 , 55 , 45, 35 ,25]

def func(nums):
    num = sorted(nums)
    return num[-1]

print(func(values))
