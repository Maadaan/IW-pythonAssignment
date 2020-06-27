"""
Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

givenTuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def func(list):
    lengthlist= len(list)
    for index in range(lengthlist):
        for num in range(lengthlist):
            if list[index][1] < list[num][1]:
                tmp = list[num]
                list[num] = list[index]
                list[index] = tmp
    
    return list

print(func(givenTuples))