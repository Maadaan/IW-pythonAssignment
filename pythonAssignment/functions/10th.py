"""
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def func(nums):
    evenNo = []
    for item in nums:
        if item % 2 == 0:
            evenNo.append(item)
    print(evenNo)


print(func(lists))
