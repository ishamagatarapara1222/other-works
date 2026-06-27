#4.1.3
'''
Implement a program where a UDF accepts a list of integers and returns the square of each integer in a new list using
a list comprehension.
'''

def square_list(nums):
    return [x * x for x in nums]

numbers = [1, 2, 3, 4, 5]
print(square_list(numbers))
