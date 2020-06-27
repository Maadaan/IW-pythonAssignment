"""
Write a Python function that takes a number as a parameter and check the
number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that
has no positive divisors other than 1 and itself.
"""

def func(nums):
    if nums  < 100:
        for i in range(2 , nums):
            if nums % i == 0:
                return f'{nums} is not a prime number !!!'
    
    else:
        for i in range(2 , (nums // 2)):
            if nums % i == 0:
                return f'{nums} is not a prime number !!!'
    return f'{nums} is a prime number !!!'



print(func(0))
print(func(2))
print(func(7))
print(func(10))
print(func(13))
