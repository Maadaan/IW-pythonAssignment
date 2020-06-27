"""
Write a Python program to square and cube every number in a given list of
integers using Lambda.
"""

lists = [2,3,4,5,7,9,10,16,25,36,50,53,74,100,108]

squareNumber = list(map(lambda x:x ** 2 , lists))
print(squareNumber)

cubednumber = list(map(lambda  y : y ** 3 , lists))
print(cubednumber)