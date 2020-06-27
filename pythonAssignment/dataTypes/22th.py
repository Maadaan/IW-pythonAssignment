"""
Write a program to remove duplicates from a list.
"""


nums = [0,1,2,3,4,5,6,7,8,9,2,6,7,8,9,7,4,5,6,2,5,8,9,6,1,4,7,0,1,7]

num = set(nums)
removingDuplicate = list(num)

print(removingDuplicate)