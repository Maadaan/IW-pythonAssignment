"""
Write a Python program to find intersection of two given arrays using
Lambda.
"""

array1 = [0,1,2,3,4,5,6,7,8,9]
array2 = [2,4,6,8,10,12,14,15]

arrayIntersection = filter(lambda x : x in array1 , array2)
print(list(arrayIntersection))